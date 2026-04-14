from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Category, Product, ContactMessage

def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)[:12]
    context = {'categories': categories, 'products': products}
    return render(request, 'store/home.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_available=True)
    context = {'product': product}
    return render(request, 'store/detail.html', context)

def category_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category, is_available=True)
    categories = Category.objects.all()
    context = {'category': category, 'products': products, 'categories': categories}
    return render(request, 'store/home.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect('store:contact')
    return render(request, 'store/contact.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('store:home')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect('store:home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('store:home')
