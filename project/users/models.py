from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username }Profile'
    
    def save(self, *args, **kwargs):
        """PIL interrupts save process to resize image"""  
        super(Profile, self).save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image)
            if image.height > 300 or image.width > 300:
                size = (300, 300)
                image = Image.open(self.image)
                image.thumbnail(size, Image.ANTIALIAS) 
                fh = storage.open(self.image.name, "w")
                format = 'png' 
                image.save(fh, format)
                fh.close()
        
