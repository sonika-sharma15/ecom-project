from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
app_name = "newapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path ("customer_login/", views.customer_login, name= "customer_login"),
    path("profile/", views.profile, name="profile"),
    path('product_list/', views.product_list, name='product_list'),
    path("search/", views.search, name='search'),
    path('product_details/<int:pk>/', views.product_details, name='product_details'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path('update-cart/<int:pk>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),


    #path("/", views., name = ""),
] 

