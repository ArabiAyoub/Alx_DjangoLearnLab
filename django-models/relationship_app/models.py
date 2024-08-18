#from django.db import models

#class Author(models.Model):
    #name = models.CharField(max_length=100)

#class Book(models.Model):
    #title = models.CharField(max_length=200)
   # author = models.ForeignKey(Author, on_delete=models.CASCADE)

#class Library(models.Model):
   # name = models.CharField(max_length=100)
   # books = models.ManyToManyField(Book)

#class Librarian(models.Model):
    #name = models.CharField(max_length=100)
    #library = models.OneToOneField(Library, on_delete=models.CASCADE)

  #  def __str__(self):
       # return self.name

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signal to automatically create or update a UserProfile when a User is created/updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()