from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
from .utils import get_video_duration

class VidStream(models.Model):
    streamer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    upload_date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='')
    duration = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse("video-detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        if not self.duration and self.video_file:
            self.duration = get_video_duration(self.video_file.path)
        super(VidStream, self).save(*args, **kwargs)

