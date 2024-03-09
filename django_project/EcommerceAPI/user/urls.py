from django.urls import path
from .views  import Registration,OwnerCreate,GroupList,login,ChangePasswordView,PasswordResetView,PasswordResetConfirm
urlpatterns = [
    path('registration/',Registration.as_view(),name='registration'),
    path('owner-create/',OwnerCreate.as_view(),name='owner-create'),
    path('group-list/',GroupList,name='group-list'),
    path('login/',login,name='login'),
    path('change-password/',ChangePasswordView.as_view({'put':'update'}),name='change-password'),
    path('password-reset/',PasswordResetView.as_view({'post':'create'}),name='password-reset'),
    path('password-reset/<str:encoded_pk>/<str:token>/',PasswordResetConfirm.as_view({'patch':'partial_update'}),name='password-reset'),
]
