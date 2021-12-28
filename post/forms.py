from django import forms
from .models import Post, Comment , Category
from captcha.fields import ReCaptchaField

# choices = [('cyber-security','Cyber Security'),
#             ('speration system','Operation System'),
#             ('software','Software'),
#             ('about-life','About Life'),
#             ('latest-news','Latest News')
#         ]


choices = Category.objects.all().values_list('name','name')
choices_list = []
for i in choices:
    choices_list.append(i)

class PostForm(forms.ModelForm):
    #captcha = ReCaptchaField()
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'category',
        ]
        widgets = {
            'category': forms.Select(choices=choices_list,attrs={'class': 'form-control'})
        }

class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Comment
        fields = [
            'name',
            'content',
        ]