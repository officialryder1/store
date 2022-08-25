from unicodedata import name
from django.urls import path
from .views import Index, detail, category, search, user_profile, upload, user_form, delete_page, delete_message
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', Index, name='home'),
   path('detail/<int:pk>', detail, name='detail'),
   path('category/<str:cat>', category, name='category'),
   path('search', search, name='search'),
   path('cart/add/<int:id>', views.cart_add, name='add'),
   path('cart/item_clear/<int:id>', views.item_clear, name='item_clear'),
   path('cart/item_increment/<int:id>', views.item_increment, name='item_increment'),
   path('cart/item_decrement/<int:id>', views.item_decrement, name='item_decrement'),
   path('cart/cart_clear', views.cart_clear, name='cart_clear'),
   path('cart/cart-detail', views.cart_detail, name='cart_detail'),
   path('profile', user_profile, name='profile'),
   path('upload', upload, name='upload'),
   path('user_update', user_form, name='user_update'),
   path('delete_post', delete_page, name='delete_page'),
   path('delete_message/<int:pk>', delete_message, name='delete_message'),
   path('delete/<int:pk>', views.delete, name="delete"),
   path('edit_page', views.edit_page, name='edit_page'),
   path('edit_upload/<int:pk>', views.edit_upload, name='edit_upload'),
   path('checkout/', views.checkout, name='checkout')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)