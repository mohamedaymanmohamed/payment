# payments/views.py
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
import json
from .models import Order

def home(request):
    return render(request, 'payments/home.html', {
        'paypal_client_id': settings.PAYPAL_CLIENT_ID
    })

@csrf_exempt
def save_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        order = Order.objects.create(
            amount=data['amount'],
            transaction_id=data['transaction_id'],
            payer_email=data['payer_email']
        )
        return JsonResponse({"message": "Order saved successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)
