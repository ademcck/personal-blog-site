from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'
urlpatterns = [
    path('login/',login_view ,name='login'),
    path('register/',register_view ,name='register'),
    path('logout/',logout_view, name='logout'),
    path('profile/',my_account, name='profile'),
    path('profile/user/<str:username>/',get_user_profile, name='user_profile'),
    path('profile/update/',update_profile, name='profile_update'),
    path('profile/posts/',myposts, name='my_posts'),
    path('profile/delete/',accontdelete, name='accont_delete'),
    path('profile/delete/',accontdelete, name='accont_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


