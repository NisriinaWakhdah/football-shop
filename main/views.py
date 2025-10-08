import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        product_list = Product.objects.all()
    elif filter_type == "limitedEdition":
        product_list = Product.objects.filter(stock__gt=0, stock__lte=10)
    else:
        product_list = Product.objects.filter(user=request.user)
        
    context = {
            'npm': '2406360445',
            'name': 'Nisriina Wakhdah Haris',
            'class': 'PBP B',
            'appName': 'main',
            'product_list': product_list,
            'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user      
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }
    return render(request, "detail_product.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_viewer,
            'launch_at': product.launch_at.isoformat() if product.launch_at else None,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'size': product.size,
            'brand': product.brand,
            'price': product.price,
            'user': product.user.username if product.user else 'Anonymous',
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_viewer,
            'launch_at': product.launch_at.isoformat() if product.launch_at else None,
            'is_featured': product.is_featured,
            'user':  product.user.username if product.user else 'Anonymous',
            'stock': product.stock,
            'size': product.size,
            'brand': product.brand,
            'price': product.price,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def register_user_ajax(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Validasi sederhana
        if password1 != password2:
            return JsonResponse({
                "status": "error",
                "message": "Password tidak sama!"
            })

        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": "error",
                "message": "Username sudah digunakan!"
            })

        # Buat user baru
        user = User.objects.create_user(username=username, password=password1)
        user.save()

        # Login otomatis (opsional)
        login(request, user)

        return JsonResponse({
            "status": "success",
            "message": "Akun berhasil dibuat! Mengalihkan ke halaman login...",
            "redirect_url": reverse("main:login")
        })

    return JsonResponse({
        "status": "error",
        "message": "Metode request tidak valid."
    })

def login_user(request):
    if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response  
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

@csrf_exempt
def login_user_ajax(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = JsonResponse({
                "status": "success",
                "message": "Login successful!",
                "redirect_url": "/"
            })
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({
                "status": "error",
                "message": "Invalid username or password."
            }, status=401)
    
    return JsonResponse({"status": "error", "message": "Invalid request."}, status=400)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    category = request.POST.get("category")
    price = request.POST.get("price")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    stock = request.POST.get('stock')
    size = request.POST.get('size')
    brand=request.POST.get('brand')
    user = request.user

    new_product = Product(
        name=name, 
        description=description,
        category=category,
        price=price,
        thumbnail=thumbnail,
        is_featured=is_featured,
        stock=stock,
        size=size,
        brand=brand,
        user=user,
    )
    new_product.save()

    return HttpResponse(b"LAUNCH", status=201)

# Tinggal styling login, register, halaman utama, readme.md, dll
