from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import ast
import datetime

isLogined = False
data = []
# Create your views here.


def index(request):
    return render(request, 'index.html') 

def main(request, user):
    return render(request, 'home.html', {'user_name': user}) 

def menu(request, user):
    if not isLogined:
        return redirect('/login') 
    return render(request, 'menu.html', {'user_name': user}) 

def book(request):
    if not isLogined:
        return redirect('/login') 
    return render(request, 'book.html') 

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        passwd = request.POST.get('passwd')
        users = User.objects.filter(name=name)
        if users.exists():
            return render(request, 'register.html', {"data": "fail"})      
        new_user = User(name=name, passwd=passwd)
        new_user.save()
        return redirect('/login')
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        user_name = request.POST.get('name')
        pass_wd = request.POST.get("passwd")
        users = User.objects.filter(name=user_name)

        if users.exists():
            user_lst = list(users.values())
            if user_lst[0]['passwd'] == pass_wd:
                global isLogined
                isLogined = True
                return redirect('/home/{}/' .format(user_name)) 
            
        return render(request, 'login.html', {"status": "fail"})
        
    return render(request, 'login.html')

@csrf_exempt
def add_order(request):
    global data
    user = request.POST.get('user')
    name = request.POST.get('name')
    price = request.POST.get('price')

    names = [item[0] for item in data]
    prices = [item[1] for item in data]
    users = [item[3] for item in data]
    qty = [item[2] for item in data]

    names.append(name)
    prices.append(price)
    users.append(user)
    qty.append("")

    data = list(zip(names, prices, qty, users))
    return JsonResponse({"status": "add food succesfully"})


def cart(request, user):
    if not isLogined:
        return redirect('/login') 

    global data
    names = [item[0] for item in data]
    prices = [item[1] for item in data]
    users = [item[3] for item in data]

    #Process quantity of every food
    names_tmp = [i for i in names if users[names.index(i)] == user]
    prices_tmp = [i for i in prices if users[prices.index(i)] == user]

    names_tmp1 = []
    prices_tmp1 = []
    quantity = []
    user_tmp = []
    for name in names_tmp:
        if name not in names_tmp1:
            names_tmp1.append(name)
            prices_tmp1.append(prices_tmp[names_tmp.index(name)])
            qty = names_tmp.count(name)
            quantity.append(qty)
            user_tmp.append(user)

    data = list(zip(names_tmp1, prices_tmp1, quantity, user_tmp))
    return render(request, "cart.html", {"data": data, "user": user})

def process_order(request, item, user):
    global data
    for itm in data:
        if itm[3] == user and itm[0] == item:
            data.remove(data[data.index(itm)])
    return render(request, "cart.html", {"data": data, "user": user})


def order(request, user):
    if request.method == "POST":
        data = request.POST.get('data')
        data = ast.literal_eval(data)
        time = datetime.datetime.now()
    
        foods = []
        for item in data:
            food = Food.objects.create(name=item[0], price=item[1], quantity=item[2], user=user)    
            foods.append(food)          
            food.save()  

        order = Order.objects.create(time = time)
        order.foods.set(foods)
        order.save()
    # Create the food instance
    return redirect("/" + user +'/order_done/')

def order_done(request, user):
    global data
    names = [item[0] for item in data if item[3] != user]
    prices = [item[1] for item in data if item[3] != user]
    qty = [item[2] for item in data if item[3] != user]
    users = [item[3] for item in data if item[3] != user]
            
    data = list(zip(names, prices, qty, users))
    return render(request, "cart.html", {"status": "success"})

def history(request, user):
    data_lst = []
    isAdded = False
    orders = Order.objects.all()
    for order in orders:
        order_his = list(order.foods.all().values())
        data = {}
        data["info"] = []
        for ord in order_his:
            if ord['user'] == user:
                info = []      
                info.append(ord['name'])
                info.append(ord['price'])
                info.append(ord['quantity'])
                data["info"].append(info)                   
                isAdded = True
        if isAdded:
            data["time"] = order.time  
            data_lst.append(data)
            isAdded = False
    return render(request, 'order_history.html', {"data": data_lst})



def logout(request):
    return render(request, 'index.html')