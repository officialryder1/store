from cmath import log
from itertools import product
from django.shortcuts import render, redirect
from .models import Product, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .form import UploadProduct, UserForm
from django.contrib.auth.models import User

#HomePage-Detail-Category-Search view
#Basic view of the web application
def Index(request):
    post = Product.objects.all().order_by('?')
    select = Product.objects.filter()[:4]
    cats = Category.objects.all()
    p = Paginator(Product.objects.all(), 3)
    page = request.GET.get('page')
    posts = p.get_page(page)
    num = 'a' * posts.paginator.num_pages
    context = {
        'post':post,
        'cats':cats,
        'select':select,
        'posts':posts,
        'nums':num

    }
    return render(request, 'product/index.html', context)

def detail(request, pk):
    post = Product.objects.get(id=pk)
    context = {
        'post':post
    }
    return render(request, 'product/detail.html', context)

def category(request, cat):
    post = Category.objects.get(name=cat)
    product = Product.objects.filter(category=post)
    context = {
        'post':post,
        'cat':cat,
        'product':product
    }
    return render(request, 'product/category.html', context)

def search(request):
    if request.method == "POST":
        search = request.POST['searched']
        post = Product.objects.filter(name__contains=search)
        context = {
            'search':search,
            'post':post
        }
        return render(request, 'product/search.html', context)
#View for Cart Functionality
#Basic function to add product to cart

@login_required(login_url="/member/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('home')

@login_required(login_url="/member/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product=product)
    return redirect('cart_detail')

@login_required(login_url="/member/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('cart_detail')

@login_required(login_url="/member/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('cart_detail')

@login_required(login_url="/member/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')

@login_required(login_url="/member/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('home')

@login_required(login_url="/member/login")
def cart_detail(request):
   post = Product.objects.all()
   return render(request, 'product/cart_detail.html',{'post':post})

@login_required(login_url="/member/login")
def checkout(request):
   return render(request, 'product/checkout.html', {})

#Profile view
#every action a user can perform are in this view

@login_required(login_url="/member/login")
def user_profile(request):
    post = Product.objects.all()
    post_len = len(post)
    return render(request, 'product/profile.html', {'post_len':post_len, 'post':post})

@login_required(login_url="/member/login")
def upload(request):
    if request.method == "POST":
        form = UploadProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UploadProduct()

    context = {'form':form}
    return render(request, 'product/upload.html', context)

@login_required(login_url="/member/login")
def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserForm()

    context = {'form':form}
    return render(request, 'product/profile_update.html', context)

@login_required(login_url="/member/login")
def delete_page(request):
   product = Product.objects.all()
   context = {
     'post':product
   }
   return render(request, 'product/delete_page.html', context)

@login_required(login_url="/member/login")
def delete_message(request, pk):
    post= Product.objects.get(id=pk)
    return render(request, 'product/delete_message.html', {'post':post})

@login_required(login_url="/member/login")
def delete(request, pk):
   post = Product.objects.get(id=pk)
   post.delete()
   return redirect('home')

@login_required(login_url="/member/login")
def edit_page(request):
   product = Product.objects.all()
   context = {
     'post':product
   }
   return render(request, 'product/edit_page.html', context)

@login_required(login_url="/member/login")
def edit_upload(request, pk):
    post = Product.objects.get(id=pk)
    if request.method =="POST":
        form = UploadProduct(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('edit_page')
    else:
        form = UploadProduct(instance=post)
    
        return render(request, 'product/edit_upload.html', {'form':form})
