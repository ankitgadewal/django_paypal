from django.urls import path, include
from . import views
app_name = 'payment'
urlpatterns = [
    path('', views.payment),
    path('done/', views.payment_done, name="done"),
    path('canceled/', views.payment_canceled, name="canceled"),
    # path('', views.payment),

]
