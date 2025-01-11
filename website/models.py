from django.db import models

# Create your models here.
class PostModel(models.Model):
    username = models.CharField(max_length=30)
    grade = models.SmallIntegerField()
    text = models.CharField(max_length=2000)
    img = models.ImageField(null=True, blank=True, upload_to="post_images/")
    pfp = models.ImageField()

    def __str__(self):
        return self.username
    
class ProfileModel(models.Model):
    username = models.CharField(max_length=300)
    grade = models.SmallIntegerField()
    pfp = models.ImageField(null=True, blank=True, upload_to="profile_picture/")

    def __str__(self):
        return self.username