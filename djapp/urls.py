from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('contact/', views.contact, name='contact'),
    path('admin/', views.admin, name='admin'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('update/<str:pk>/', views.update, name='update'),
    path('job_post/', views.job_post, name='job_post'),
    path('update_post/<str:pk>/', views.update_post, name='update_post'),
    path('manage_post/<str:pk>/', views.manage_post, name='manage_post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete_post'),
    path('detail_post/<str:pk>/', views.detail_post, name='detail_post'),
    path('error/', views.error, name='error'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]
