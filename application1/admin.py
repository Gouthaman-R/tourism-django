# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User # Import your custom User model
# from .models import Product, ProductImage

# # Register the custom User model with the admin site
# admin.site.register(User, UserAdmin)
# # admin.site.register(product)



# class ProductImageInline(admin.TabularInline):  # You can also use admin.StackedInline
#     model = ProductImage
#     extra = 1  # This will display one empty form initially for adding images
#     fields = ['image']

# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductImageInline]  # This will add the ProductImageInline to the Product model in admin
#     list_display = ('title', 'price', 'content')  # You can add fields you want to display in the list view

# admin.site.register(Product, ProductAdmin)











from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, ProductImage

# Custom User Admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('date_joined',)

    fieldsets = (
        ("User Information", {"fields": ("username", "email", "password")}),
        ("Personal Details", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

# Product Images Inline
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image']

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('title', 'price', 'content')
    search_fields = ('title', 'content')
