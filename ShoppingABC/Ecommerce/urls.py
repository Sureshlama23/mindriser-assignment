"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from home.forms import LoginForm,MyPasswordChangeForm,MyPasswordReset,MyPasswordSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('<slug:slug>',views.home,name='homedata'),
    path('shop/',views.shopView.as_view(),name='shop'),
    path('product-detail/<slug>',views.productDetailView.as_view(),name='product-detail'),
    path('shoppingCart/',views.ShoppingCartView.as_view(),name='shoppingCart'),
    path('shoppingCart/<slug:slug>',views.ShoppingCartView.as_view(),name='shoppingCart'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('registration/',views.CustomerRegistrationView.as_view(),name='customer-registration'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm,next_page='home'),name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.AddressView.as_view(),name='address'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordReset),name='password-reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MyPasswordSet),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
