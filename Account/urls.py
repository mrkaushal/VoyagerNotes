from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('account/signup/', views.signup, name='signup'),
    path('account/login/', LoginView.as_view(template_name='Account/registration/login.html', redirect_authenticated_user=True), name='login'),
    path('account/logout/', views.logout_view, name='logout'),
    path('account/change_password/', views.change_password, name='change_password'),
    path('account/', include('django.contrib.auth.urls')),
]
