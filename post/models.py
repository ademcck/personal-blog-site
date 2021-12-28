from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name
  
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name='Yazar', related_name="posts")
    title = models.CharField(max_length=120, verbose_name='Başlık')
    content = RichTextUploadingField(verbose_name='İçerik')
    pub_date=models.DateTimeField(verbose_name='Yayınlanma Tarihi',auto_now_add=True)
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(unique=True, editable=False,max_length= 130) 
    category = models.CharField(max_length=120, default= 'cyber-security', verbose_name='category')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')

    def __str__(self):
        return self.title
        
    
    def number_of_likes(self):
        return  self.likes.count()

    def my_likes(self,username):
        print('*'*30)
        print(self.likes.objects.get(username=username))
        print('*'*30)
    
    def get_absolute_url(self):
        return reverse('post:detail',kwargs={'slug':self.slug})

  
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post,self).save(*args, **kwargs)

    class Meta:
        ordering = ['pub_date',"id"]

class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='İsim')
    content = models.TextField(verbose_name='Yorum')
    created_date = models.DateTimeField(auto_now_add=True)

