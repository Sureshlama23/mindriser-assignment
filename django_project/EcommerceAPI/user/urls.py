from django.urls import path
from .views  import Registration,OwnerCreate,GroupList,login,ChangePasswordView
urlpatterns = [
    path('registration/',Registration.as_view(),name='registration'),
    path('owner-create/',OwnerCreate.as_view(),name='owner-create'),
    path('group-list/',GroupList,name='group-list'),
    path('login/',login,name='login'),
    path('change-password/',ChangePasswordView.as_view({'put':'update'}),name='change-password')
]
