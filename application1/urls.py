# from django.urls import path
# from . import views
# from .views import add_to_favorites, favorites



# urlpatterns = [
#     path("",views.home,name="home"),
#     path("sign/",views.sign,name="signup"),
#     path('login/', views.login_view, name='login'),
#     path('verify-otp/', views.verify_otp, name='verify_otp'),
#     path('favorites/add/<int:item_id>/', add_to_favorites, name='add_to_favorites'),
#     path('favorites/', favorites, name='favorites'),
   
# ]



# application1/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.home, name="home"),
#     path("sign/", views.sign, name="signup"),
#     path('login/', views.login_view, name='login'),
#     path('verify-otp/', views.verify_otp, name='verify_otp'),
#     path('favorites/add/<int:item_id>/', views.add_to_favorites, name='add_to_favorites'),
#     path('favorites/', views.favorites, name='favorites'),
#     path('favorites/remove/<int:favorite_id>/', views.remove_from_favorites, name='remove_from_favorites'),  # URL for removing favorites
#     path('userpage/', views.userpage, name='userpage'), 
# ]

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

urlpatterns = [
    path("", views.home, name="home"),
    path("sign/", views.sign, name="signup"),
    path('login/', views.login_view, name='login'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('userpage/',views.userpage,name='userrr'),
    path('favorites/', views.favorites_view, name='view_favorites'),
    # path('favorites/add/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('add-to-favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    # path('place-order/<int:product_id>/', views.place_order, name='place_order'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    path('place-order/', views.place_order, name='place_order'),
    path('back/',views.back_user,name='back'),
    path('logout/', views.custom_logout, name='logout'),
    


    path(
        'update-password/', 
        PasswordChangeView.as_view(
            template_name='update_password.html', 
            success_url=reverse_lazy('password_change_done')
        ), 
        name='password_change'
    ),
    path(
        'password-change-done/', 
        PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
        name='password_change_done'
    ),
    path('search/', views.search_products, name='search_products'),
     path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    ]




# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)