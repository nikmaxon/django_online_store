from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, generate_new_password, activate_account, ActivationOk, \
    ActivationFailed

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='genpassword'),
    path('verify/<str:uidb64>/', activate_account, name='email_verification'),
    path('success', ActivationOk.as_view(), name='activation_ok'),
    path('failed', ActivationFailed.as_view(), name='activation_failed'),
]