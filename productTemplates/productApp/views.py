from django.shortcuts import render


# Create your views here

def electronics(request):
    products = {
        "product1": "Mac",
        "product2": "IPhone",
        "product3": "Dell"
    }
    return render(request, "productApp/products.html", products)


def toys(request):
    products = {
        "product1": "Remote Care",
        "product2": "Drone",
        "product3": "Rocket Launcher "

    }
    return render (request, 'productApp/products.html', products)


def shoes(request):
    products = {
        "product1": "Nike",
        "product2": "Adidas",
        "product3": "Reebock"
    }
    return render(request, 'productApp/products.html', products)

def index(request):
    return render(request, 'productApp/index.html')
