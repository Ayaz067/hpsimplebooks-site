from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    email = models.EmailField()
    social_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name}'