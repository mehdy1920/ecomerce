from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render, get_object_or_404
from .models import Category, Product,BGImagesModel
from cart.form import CartAddProductForm
from django.contrib.auth.decorators import login_required







def product_list(request, category_slug=None):
    category = None 
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

@login_required(login_url="/accounts/login/")
def article_create(request):
    return render(request,'shop/product/article_create.html')



def images(request):
context['data'] = {image1: "url"}   
 return render(request, 'shop/base.html', context)