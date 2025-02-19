from django.db import models

class Post(models.Model):
    person_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    is_sponsored = models.BooleanField(default=False)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.person_name}'s post - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

