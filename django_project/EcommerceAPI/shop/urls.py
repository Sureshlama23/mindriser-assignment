from django.urls import path
from .views import ShopDetailView,shopOrderView

urlpatterns = [
    path('seller-orders/',shopOrderView.as_view({'get':'list'}),name='buyer-orders'),
    path('update-order/<uid>',shopOrderView.as_view({'get':'retrieve','put':'update'}),name='update-order'),
    path('shop-detail/',ShopDetailView.as_view({"get":"list","post":"create"}),name='shop-detail'),
    path('shop-update/<uid>',ShopDetailView.as_view({"get":"retrieve","put":"update","delete":"destroy"}),name='shop-update'),
]
