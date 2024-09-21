from django.db import models

# Create your models here.
class LaneImageModel(models.Model):
    caption = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        self.caption