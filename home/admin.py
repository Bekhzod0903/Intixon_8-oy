from django.contrib import admin
from .models import Transaction,ExpenseCategory,IncomeCategory
# Register your models here.

admin.site.register(Transaction)
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)