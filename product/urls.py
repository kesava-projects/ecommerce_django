from django.urls import path
from .views import home, add_product, show_products, search_product, add_cart, del_product, edit_product, upd_product, \
    show_cart, delete_from_cart

urlpatterns = [
    path('', home),
    path('add_product', add_product),
    path('show_products', show_products, name="show"),
    path('search_product', search_product),
    path('add_cart/<int:id>', add_cart),
    path('del_product/<int:id>', del_product),
    path('edit_product/<int:id>', edit_product),
    path('upd_product', upd_product),
    path('show_cart', show_cart, name="cart"),
    path('del_from_cart/<int:id>', delete_from_cart)
]