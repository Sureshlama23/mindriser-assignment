from django.urls import path
from .views import GuestInfoView,GuestRoomView

urlpatterns = [
    path('guestinfo/',GuestInfoView.as_view({'get':'list','post':'create'}),name="guestinfo"),
    path('guestinfo/<int:pk>/',GuestInfoView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name="guestinfo"),
    path('guestroom/',GuestRoomView.as_view(),name="guestroom"),
]
