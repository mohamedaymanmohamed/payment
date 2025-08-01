# payments/admin.py
from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'payer_email', 'transaction_id', 'created_at')
