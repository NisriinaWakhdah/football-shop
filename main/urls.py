from django.urls import path
from main.views import show_main, add_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product_ajax, delete_product, add_product_entry_ajax, login_user_ajax, register_user_ajax, proxy_image, add_product_flutter, my_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product/', add_product, name='add_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('add-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('login-ajax/', login_user_ajax, name='login_user_ajax'),
    path('register-ajax/', register_user_ajax, name='register_user_ajax'),
    path('get-products/', show_json, name='show_json'),
    path('proxy-image/', proxy_image, name='proxy-image'),
    path('add-flutter/', add_product_flutter, name='add_product_flutter'),
    path('my-product/', my_product_flutter, name='my_product_flutter'),
]

