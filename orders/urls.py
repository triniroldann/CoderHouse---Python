from django.contrib import admin
from django.urls import path
from orders.views import NewOrderView,OrdersListView,UpdateOrderView,OrderDeleteView

urlpatterns = [
   path('neworder/', NewOrderView.as_view()),
   path('list-orders/', OrdersListView.as_view()),
   path('upgrade-orders/<int:pk>',UpdateOrderView.as_view()),
   path('delete-orders/<int:pk>', OrderDeleteView.as_view()),
   path('admin/', admin.site.urls)
]