from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('home/<str:user>/', views.home, name ='home'),
    path('menu/<str:user>/', views.menu, name = 'menu'),
    path('book/<str:user>/', views.book, name = 'book'),
    path('cart/<str:user>/', views.cart, name = 'cart'),
    path('add_order/', views.add_order, name = 'add_order'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('<str:user>/order/', views.order, name = 'order'),
    path('<str:user>/order_done/', views.order_done, name = 'order_done'),
    path('order-history/<str:user>', views.history, name='order-history'),
    path('process-cart/<str:item>/<str:user>', views.process_order, name='process-order'),
    path('logout/', views.logout, name='logout')
]
