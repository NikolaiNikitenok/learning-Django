from django.db import models
from django.contrib.auth.models import User
from PIL import Image

def crop_center(pil_img, crop_width: int, crop_height: int):
            img_width, img_height = pil_img.size
            return pil_img.crop(((img_width - crop_width) // 2,
                                (img_height - crop_height) // 2,
                                (img_width + crop_width) // 2,
                                (img_height + crop_height) // 2))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default-profile.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
                
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            image_size_1, image_size_2 = img.size
            if image_size_1 > image_size_2:
                img = crop_center(img, image_size_2, image_size_2)
                
            else:
                img = crop_center(img, image_size_1, image_size_1)
                
            img.thumbnail(output_size)
            img.save(self.image.path)
