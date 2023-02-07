from django.shortcuts import render
from orders.models import Order
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.decorators import login_required

class NewOrderView(CreateView):
    model = Order
    template_name = "orders/neworder.html"
    fields= '__all__'
    success_url= '/orders/list-orders/'
class OrdersListView(ListView):
    model = Order
    template_name = "orders/listorders.html"
class UpdateOrderView(UpdateView):
    model = Order
    template_name = "orders/upgradeorder.html"
    success_url= '/orders/list-orders/'
    fields= '__all__'
    
class OrderDeleteView(DeleteView):
    model = Order
    template_name = "orders/orderdelete.html"
    success_url= '/orders/list-orders/'
    



