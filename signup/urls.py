from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView

from signup.views import signup, login, home, success


urlpatterns = [
    url(r'^$', home, name='home_page'),
    url(r'^signup/', signup, name='signup_page'),
    url(r'^login$', LoginView.as_view(
        template_name="signup/login_page.html"), name='login_page'),
    url(r'logout$', LogoutView.as_view(), name='logout_page'),
    url(r'success$', success, name='success_page')
]
