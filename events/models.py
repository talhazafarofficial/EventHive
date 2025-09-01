from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# ✅ Your Event Model
class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Music', 'Music'),
        ('Business', 'Business'),
        ('Food', 'Food'),
    ]

    title = models.CharField(max_length=200)
    image_url = models.URLField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    seats_available = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Technology')  # ✅ NEW FIELD

    def __str__(self):
        return self.title

# ✅ Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"

# ✅ Profile Model (outside of Booking — correct!)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

# ✅ Automatically create or update Profile when User is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()