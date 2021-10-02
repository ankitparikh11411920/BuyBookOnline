from django.shortcuts import render, redirect
from .models import Category, Book, Order
from django.contrib import sessions, messages
from django.contrib.auth.models import User, auth
import datetime as date


# Create your views here.

class OrderDetails:
    def __init__(self, book, orderedOn, address):
        self.book = book
        self.orderedOn = orderedOn
        self.address = address


def home(request):
    if checkSession(request):
        categories = Category.objects.all()
        user = auth.get_user(request)
        name = User.get_short_name(user)
        return render(request, 'home.html', {'Categories': categories, 'Username': name})
    else:
        return redirect('/buybookonline/account/login/')


def category(request):
    if checkSession(request):
        name = request.GET['category']
        books = Book.objects.filter(genre=name)
        return render(request, 'category.html', {'Books': books, 'category': name})
    else:
        return redirect('/buybookonline/account/login/')


def allProducts(request):
    if checkSession(request):
        books = Book.objects.all()
        return render(request, 'allproducts.html', {'Books': books})
    else:
        return redirect('/buybookonline/account/login/')


def logout(request):
    request.session['username'] = None
    return redirect('/buybookonline/account/login/')


def order(request):
    if checkSession(request):
        if request.method == 'POST':
            book_id = request.POST['book_id']
            user_id = request.POST['user_id']
            address = request.POST['address']
            price = request.POST['price']
            user = auth.get_user(request)
            name = User.get_short_name(user)
            orderedOn = date.date.today()
            if address:
                book = Book.objects.get(id=book_id)
                book.quantity -= 1
                book.save()
                order1 = Order(name=name, book_id=book_id, user_id=user_id, address=address, amount=price,
                               orderedOn=orderedOn)
                order1.save()
                return redirect('/buybookonline/home')
            else:
                messages.info(request, "Address field cannot be empty")
                return redirect('/buybookonline/home/order/?id=' + book_id)

        book_id = request.GET['id']
        book = Book.objects.get(id=book_id)
        username = request.session['username']
        return render(request, 'order.html', {'book': book, 'Username': username})
    else:
        return redirect('/buybookonline/account/login/')


def yourorders(request):
    if checkSession(request):
        username = request.session['username']
        order1 = Order.objects.filter(user_id=username)
        books = []
        for order2 in order1:
            book = Book.objects.get(id=order2.book_id)
            item = OrderDetails(book, order2.orderedOn, order2.address)
            books.append(item)
        return render(request, 'yourorders.html', {'books': books})
    else:
        return redirect('/buybookonline/account/login')

def checkSession(request):
    username = request.session['username']
    if username:
        return True
    else:
        return False
