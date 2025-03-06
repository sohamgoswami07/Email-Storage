from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def list(request):
    queryset = EmailTemplate.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(subject__icontains = request.GET.get('search'))

    context = {'emails': queryset}

    return render(request, 'list/list.html', context)

@login_required(login_url="/login/")
def dashboard(request):
    queryset = EmailTemplate.objects.filter(user = request.user)
    count = queryset.count()
    print(count)
    context = {'emails': queryset}

    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url="/login/")
def create(request):
    if request.method == "POST":
        email_subject = request.POST.get('subject')
        email_body = request.POST.get('body')
        attachments = request.FILES.get('attach_files')

        # Check if file exists before saving to avoid errors
        if attachments:
            # Save the new email template
            EmailTemplate.objects.create(
                user = request.user,
                subject = email_subject,
                body = email_body,
                attachments = attachments,
                ratings = 0
            )
        else:
            EmailTemplate.objects.create(
                user = request.user,
                subject = email_subject,
                body = email_body,
                ratings = 0
            )

        return redirect('home')

    return render(request, 'create/create.html')

@login_required(login_url="/login/")
def update(request, id):
    queryset = EmailTemplate.objects.get(id = id)

    if request.method == "POST":
        email_subject = request.POST.get('subject')
        email_body = request.POST.get('body')
        attachments = request.FILES.get('attach_files')

        queryset.subject = email_subject
        queryset.body = email_body
        if attachments:
            queryset.attachments = attachments

        queryset.save()
        return redirect('dashboard')

    context = {'email': queryset}

    return render(request, 'update/update.html', context)

@login_required(login_url="/login/")
def delete(id):
    queryset = EmailTemplate.objects.get(id = id)
    queryset.delete()

    return redirect('dashboard')

def register_page(request):
    if request.method == "POST":
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        if password != repeat_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        else:
            user = User.objects.create(
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                username = request.POST.get('username'),
                email = request.POST.get('email')
            )

            user.set_password(password)
            user.save()
            
            login(request, user)

        return redirect('home')

    return render(request, 'register/register.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists:
            messages.error(request, "Invalid username!")
            return redirect('login')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "Invalid password!")
            return redirect('login')
            
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'login/login.html')

def logout_page(request):
    logout(request)
    return redirect('home')

def details(request, id):
    email = get_object_or_404(EmailTemplate, id = id)
    
    return render(request, 'details/details.html', {'email': email})

@login_required(login_url="/login/")
def profile(request, id):
    queryset = get_object_or_404(User, id = id)  # Ensure user exists or return 404

    if request.method == "POST":
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        username = request.POST.get('username', '').strip()

        # Update user fields
        queryset.first_name = first_name
        queryset.last_name = last_name
        queryset.email = email
        queryset.username = username

        queryset.save()
        messages.success(request, 'Your profile is updated.')
        return redirect('profile', id = id)  # Ensure correct redirection

    context = {'profile_detail': queryset}
    return render(request, 'profile/profile.html', context)

def profile_delete(request, id):
    queryset = get_object_or_404(User, id = id)
    if request.method == "POST":
        queryset.delete()
        return redirect('home')
    return render(request, 'profile_delete/profile_delete.html')

def download_html_template(id):
    email = EmailTemplate.objects.get(id = id)
    email_subject = email.subject
    email_body = email.body

    sample_form = f'''
        <form>
            <q>
                <h1 class="text-2xl font-semibold text-slate-900">{email_subject}</h1>
                <p class="text-slate-900 mt-2">{email_body}</p>
            </q>
        </form>
    '''

    # Parse the form using BeautifulSoup
    soup = BeautifulSoup(sample_form, "html.parser")
    q_tag_content = str(soup.q)  # Extract inner HTML of <q>

    # Generate the downloadable HTML content
    html_content = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Extracted Form Elements</title>
        </head>
        <body>
            {q_tag_content}
        </body>
        </html>
    '''

    # Create HTTP response with file download
    response = HttpResponse(html_content, content_type="text/html")
    response['Content-Disposition'] = 'attachment; filename="downloaded_template.html"'

    return response

# @login_required
# def ratings(request, id):
#     url = request.META.get('HTTP_REFERER', '/')
#     obj = get_object_or_404(EmailTemplate, id = id)  # Fetch object being rated

#     if request.method == "POST":
#         try:
#             rating_value = EmailTemplate.objects.get(user = request.user, email = request.email)  # Check if user has already rated
#             form = RatingsForm(request.POST, instance = rating_value)
#         except EmailTemplate.ratings.DoesNotExist:
#             form = RatingsForm(request.POST)

#         if form.is_valid():
#             data = form.save(commit=False)
#             data.user = request.user
#             data.save()
#             messages.success(request, "Thanks for your review")
#             return redirect(url)

#     else:
#         form = RatingsForm()

#     return render(request, "ratings.html", {"form": form, "obj": obj})