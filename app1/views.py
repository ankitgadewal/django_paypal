from django.shortcuts import render, redirect, reverse, get_object_or_404
from decimal import Decimal
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_done(request):
    return render(request, 'done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'canceled.html')

@csrf_exempt
def payment_done(request):
    return render(request, 'done.html')

# Create your views here.
def payment(request):
    order_id = 458745896
    order = 'fish fry'
    host = request.get_host()

    paypal_dict = {
        'business' : settings.PAYPAL_RECEIVER_EMAIL,
        'amount' : 1200,
        'item_name' : order,
        'invoice' : str(order_id),
        'currency_code': 'INR',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment.html', {'order': order, 'form': form})
