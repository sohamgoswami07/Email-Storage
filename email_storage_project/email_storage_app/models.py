from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmailTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    body = models.TextField()
    attachments = models.ImageField(upload_to="assets/", blank=True, null=True)
    ratings = models.PositiveIntegerField(choices=[(i, i) for i in range(0, 6)], null=True, blank=True, default=0) # Rating from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        unique_together = ('user', 'email')  # Ensures one rating per user per email
    
    def __str__(self):
        return self.subject