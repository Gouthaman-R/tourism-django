
# from django.shortcuts import render, redirect
# from .forms import SignupForm
# from django.contrib.auth.hashers import make_password, check_password
# from .models import User,Product,ProductImage # Ensure you have a User model defined
# from django.contrib.auth import authenticate, login as auth_login
# from django.core.mail import send_mail
# import random
# from django.shortcuts import render, redirect
# from .models import User

# # def adminn(request):
# #     return redirect('adminnn')


# # Global variable to store OTP for verification
# otp_storage = {}

# # Home page view<---------------------------------------------------->
# def home(request):
#     return render(request, 'home.html')

# # Signup view<----------------------------------------------------------->
# def sign(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = make_password(form.cleaned_data['password'])  # Hash the password
#             email = form.cleaned_data['email']
#             age = form.cleaned_data['age']
#             phone_number = form.cleaned_data['phone_number']

#             # Create a new user instance
#             user = User(username=username, password=password, email=email, age=age, phone_number=phone_number)
#             user.save()  # Save the user to the database

#             # Store username in the session (password shouldn't be stored in plain text)
#             request.session['username'] = username

#             return redirect('home')  # Redirect to a success page or homepage
#     else:
#         form = SignupForm()
    
#     return render(request, 'signup.html', {'form': form})

# # Login view<---------------------------------------------------->
# def login_view(request):
#     if request.method == 'POST':
#         login_method = request.POST.get('login_method')
        
#         if login_method == 'username_password':
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             # Authenticate the user using Django's built-in method
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 # Log in the user
#                 auth_login(request, user)
#                 return redirect('userrr')
#             else:
#                 return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
        
#         elif login_method == 'otp':
#             email = request.POST.get('email')
#             try:
#                 user = User.objects.get(email=email)
#                 otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
#                 otp_storage[email] = otp  # Save OTP for verification
#                 send_mail(
#                     'Your OTP Code',
#                     f'Your OTP code is: {otp}',
#                     'gouthamanravi2004@gmail.com',
#                     [email],
#                     fail_silently=False,
#                 )
#                 return redirect('verify_otp')
#             except User.DoesNotExist:
#                 return render(request, 'login.html', {'error_message': 'Email not found.'})
    
#     return render(request, 'login.html')


# # userpage view<------------------------------------>
# def userpage(request,product_id):
#     insert_data=Product.objects.get(id=product_id)
#     images = Product.image.all()
#     return render(request,'userpage.html', {'username': request.user.username,'inst_data':insert_data,'image':images})


# # OTP verification view<----------------------------->
# def verify_otp(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         entered_otp = request.POST.get('otp')
        
#         if otp_storage.get(email) == int(entered_otp):
#             user = User.objects.get(email=email)
#             auth_login(request, user)  # Use the imported login function to log in the user
#             otp_storage.pop(email)  # Clear the OTP after successful login
#             return redirect('home')
#         else:
#             return render(request, 'verify_otp.html', {'error_message': 'Invalid OTP'})
    
#     return render(request, 'verify_otp.html')




from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.hashers import make_password
from .models import User,Product,Favorite,Cart
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
import random
from django.shortcuts import  redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .forms import SignupForm



# Global variable to store OTP for verification
otp_storage = {}

# Home page view
def home(request):
    return render(request, 'home.html')

#------------------------------------------------- Signup view--------------------------------------
# def sign(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = make_password(form.cleaned_data['password'])  # Hash the password
#             email = form.cleaned_data['email']
#             age = form.cleaned_data['age']
#             phone_number = form.cleaned_data['phone_number']

#             # Create a new user instance
#             user = User(username=username, password=password, email=email, age=age, phone_number=phone_number)
#             user.save()  # Save the user to the database

#             # Store username in the session (password shouldn't be stored in plain text)
#             request.session['username'] = username

#             return redirect('home')  # Redirect to a success page or homepage
#     else:
#         form = SignupForm()
    
#     return render(request, 'signup.html', {'form': form})
# -------------------------------------------------------------------------------------------------------






User = get_user_model()  # Ensure we're using the correct User model

def sign(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            phone_number = form.cleaned_data['phone_number']

            # Create a new user with create_user() to handle password hashing
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password  # Automatically hashed by create_user()
            )
            user.age = age
            user.phone_number = phone_number
            user.save()  # Save the extra fields

            # Store username in the session (password shouldn't be stored in plain text)
            request.session['username'] = username

            return redirect('home')  # Redirect to a success page or homepage
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})







# Login view
def login_view(request):
    if request.method == 'POST':
        login_method = request.POST.get('login_method')
        
        if login_method == 'username_password':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate the user using Django's built-in method
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log in the user
                auth_login(request, user)
                return redirect('userrr')
            else:
                return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
        
        elif login_method == 'otp':
            email = request.POST.get('email')
            try:
                user = User.objects.get(email=email)
                otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
                otp_storage[email] = otp  # Save OTP for verification
                send_mail(
                    'Your OTP Code',
                    f'Your OTP code is: {otp}',
                    'gouthamanravi2004@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return redirect('verify_otp')
            except User.DoesNotExist:
                return render(request, 'login.html', {'error_message': 'Email not found.'})
    
    return render(request, 'login.html')


# Userpage view
# def userpage(request):
#     products = Product.objects.all()
#     return render(request, 'userpage.html', {'products': products,'username':request.user.username})



# OTP verification view
def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        entered_otp = request.POST.get('otp')
        
        if otp_storage.get(email) == int(entered_otp):
            user = User.objects.get(email=email)
            auth_login(request, user)  # Use the imported login function to log in the user
            otp_storage.pop(email)  # Clear the OTP after successful login
            return redirect('userrr')
        else:
            return render(request, 'verify_otp.html', {'error_message': 'Invalid OTP'})


    return render(request, 'verify_otp.html')


# @login_required
# def userpage(request):
#     products = Product.objects.all()
#     # Get the IDs of the user's favorite products
#     favorite_product_ids = Favorite.objects.filter(user=request.user).values_list('product_id', flat=True)
#     return render(request, 'userpage.html', {
#         'products': products,
#         'favorite_product_ids': favorite_product_ids,
#         'username':request.user.username
#     })

@login_required
def userpage(request):
    products = Product.objects.all()
    favorite_product_ids = Favorite.objects.filter(user=request.user).values_list('product_id', flat=True)
    
    # Check for payment success parameter
    payment_success = request.GET.get('payment_success')
    if payment_success == 'true':
        # Send payment success email
        send_mail(
            'Payment Successful',
            'Your payment has been processed successfully.',
            'gouthamanravi2004@gmail.com',  # Sender email
            [request.user.email],       # Recipient email
            fail_silently=False,
        )

    return render(request, 'userpage.html', {
        'products': products,
        'favorite_product_ids': favorite_product_ids,
        'username': request.user.username,
        'payment_success': payment_success
    })



def add_to_favorites(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        
        # Check if the product is already in favorites
        favorite = Favorite.objects.filter(user=request.user, product=product).first()
        
        if favorite:
            # If it's already in favorites, remove it
            favorite.delete()
            return JsonResponse({'success': True, 'message': 'Removed from favorites'})
        else:
            # If it's not in favorites, add it
            Favorite.objects.create(user=request.user, product=product)
            return JsonResponse({'success': True, 'message': 'Added to favorites'})
    return JsonResponse({'success': False, 'message': 'User not authenticated'})

# @login_required
# def view_favorites(request):
#     favorites = Favorite.objects.filter(user=request.user).select_related('product')
#     return render(request, 'myfav.html', {'favorites': favorites})
def favorites_view(request):
    favorites = Favorite.objects.filter(user=request.user)
    
    # You can get the first image associated with each product
    favorites_with_images = [
        {
            'product': favorite.product,
            'image': favorite.product.images.first().image.url if favorite.product.images.exists() else None
        }
        for favorite in favorites
    ]
    
    return render(request, 'myfav.html', {'favorites': favorites_with_images})


# Add to Cart view
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    # Check if the product is already in the cart
    if not Cart.objects.filter(user=request.user, product=product).exists():
        Cart.objects.create(user=request.user, product=product)
        return JsonResponse({'success': True, 'message': 'Added to Cart'})
    else:
        return JsonResponse({'success': False, 'message': 'Already in Cart'})

# Cart page view
@login_required
def view_cart(request):
    # Fetch all products in the user's cart
    cart_items = Cart.objects.filter(user=request.user)
    products = [cart_item.product for cart_item in cart_items]
    return render(request, 'cart.html', {'products': products})


# Remove a product from the cart
@login_required
def remove_from_cart(request, product_id):
    # Get the product to remove
    try:
        cart_item = Cart.objects.get(user=request.user, product_id=product_id)
        cart_item.delete()  # Remove the product from the cart
    except Cart.DoesNotExist:
        pass  # Product not in cart, nothing to remove
    return redirect('view_cart')  # Redirect back to the cart page


# ----------------------------------------------------------------------------------------------------------------#

 # Checkout view
# def checkout(request, product_id):
#     # Get the product based on the ID passed in the URL
#     product = get_object_or_404(Product, id=product_id)

#     # Calculate the total price based on the number of persons entered by the user
#     total_price = product.price

#     if request.method == 'POST':
#         # Handle the order creation logic here
#         return HttpResponseRedirect('/order-confirmation')

#     # Pass product details and calculated price to the template for rendering
#     context = {
#         'product': product,
#         'total_price': total_price  # Total price is calculated here
#     }
#     return render(request, 'checkout.html', context)




# # Place Order view
# def place_order(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
    
#     # Here, you can calculate the total price based on user input (for example, from the number of persons).
#     # For now, we just calculate it based on the product price.
#     total_price = product.price

#     if request.method == 'POST':
#         # Here, you would typically handle order processing (e.g., create an Order model, process payment, etc.)
#         # For now, let's just return a simple confirmation page
        
#         return render(request, 'order_confirmation.html', {'product': product, 'total_price': total_price})
    
#     return HttpResponseRedirect('/')  # Redirect to home page if method is not POST



# ------------------------------------------------------------------------------------------------------------------------#



def checkout(request, product_id):
    product = Product.objects.get(id=product_id)

    # Get the number of persons from the query parameters or default to 1
    number_of_persons = int(request.GET.get('num-persons',1))

    # Calculate total price
    total_price = product.price * number_of_persons

    # Store the calculated total price and product ID in session
    request.session['total_price'] = total_price
    request.session['product_id'] = product.id

    # Pass the product and total price to the template
    context = {
        'product': product,
        'total_price': total_price,
    }

    return render(request, 'checkout.html', context)







# def place_order(request):
#     # Retrieve product and total price from session
#     product_id = request.session.get('product_id')
#     total_price = request.session.get('total_price')

#     if not product_id or total_price is None:
#         # If session values are not found, redirect back to checkout
#         return redirect('checkout', product_id=product_id)

#     # Get the product instance from the database
#     product = get_object_or_404(Product, id=product_id)

#     # Render the order confirmation page with product and total price
#     context = {
#         'product': product,
#         'total_price': total_price,
#     }

#     return render(request, 'order_confirmation.html', context)







from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def place_order(request):
    if request.method == 'POST':
        payment_mode = request.POST.get('payment_mode')
        product_id = request.session.get('product_id')
        total_price = request.session.get('total_price')

        if not product_id or total_price is None:
            return redirect('checkout', product_id=product_id)

        product = get_object_or_404(Product, id=product_id)

        if payment_mode == 'cash-on-delivery':
            # Send a payment success email
            send_mail(
                'Payment Successful',
                f'Your order for {product.title} has been placed successfully with Cash on Delivery.',
                'gouthamanravi2004@gmail.com',
                [request.user.email],
                fail_silently=False,
            )
            return redirect('/userpage/?payment_success=true')

        else:
            return render(request, 'order_confirmation.html', {
                'product': product,
                'total_price': total_price,
                'error_message': "Selected payment mode is not supported yet."
            })
    
    return redirect('/')







# ------------------------------------------------------------------------------------------//

def back_user(request):
    return redirect('userrr')

def custom_logout(request):
    logout(request)
    return redirect('/') 



def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(title__icontains=query) if query else []
    product_data = [{"id": product.id, "title": product.title} for product in products]
    return JsonResponse(product_data, safe=False)



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


