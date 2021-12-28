from django.db import models
from django.contrib.auth.models import User
from phone_field.models import PhoneField
from multiselectfield import MultiSelectField
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png',blank=True, upload_to='profile_images')
    bio = models.TextField(blank=True,max_length=450)
    location = models.CharField(max_length=200,blank=True, verbose_name="adress")
    personel_site = models.URLField(max_length=120,blank=True,  verbose_name='personel')
    linkedin = models.URLField(max_length=120,blank=True,  verbose_name='linkedin')
    facebook = models.URLField(max_length=120,blank=True,  verbose_name='facebook')
    instagram = models.URLField(max_length=120,blank=True,  verbose_name='instagram')
    phone = PhoneField( help_text='İletişim Numarası giriniz.',blank=True, verbose_name= "Tel")
    

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

class Privacy(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    CHILDCARE_REASONS = (
        ('tel_privacy','Telefon Numaramı Göster'),
        ('bio_privacy','Biografimi Göster'),
        ('adress_privacy','Kişisel Adresimi Göster'),
        ('email_privacy','Email Adresimi Göster')
    )
    choices_data = MultiSelectField(choices=CHILDCARE_REASONS,blank=True ,verbose_name='Gizlilik')
    def __str__(self):
        return str(self.user)
