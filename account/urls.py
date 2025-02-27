from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),

    # Input and output urls
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password change url
    #path('password-change/', auth_views.PasswordChangeView.as_view(),
         #name='password_change'),
    #path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
         #name='password_change_done'),

    # Password reset url
    #path('password-reset/',auth_views.PasswordResetView.as_view(),
         #name='password_reset'),
    #path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
         #name='password_reset_done'),
    #path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         #name='password_reset_confirm'),
    #path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(),
         #name='password_reset_complete'),

    # Authentication URL
    path('', include('django.contrib.auth.urls')),
    path('', views.neobank, name='neobank'),
    path('register/', views.register, name='register'),
    # URL for editing personal information by users
    path('edit/', views.edit, name='edit'),
]