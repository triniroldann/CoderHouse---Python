from django.shortcuts import render
from orders.models import Order
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin

def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper

@superuser_required()
class NewOrderView(CreateView):
    model = Order
    template_name = "orders/neworder.html"
    fields= '__all__'
    success_url= '/orders/list-orders/'
@superuser_required()
class OrdersListView(ListView):
    model = Order
    template_name = "orders/listorders.html"
@superuser_required()
class UpdateOrderView(UpdateView):
    model = Order
    template_name = "orders/upgradeorder.html"
    success_url= '/orders/list-orders/'
    fields= '__all__' 
@superuser_required()
class OrderDeleteView( DeleteView ):
    model = Order
    template_name = "orders/orderdelete.html"
    success_url= '/orders/list-orders/'
    



