from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction, IncomeCategory, ExpenseCategory
from .forms import IncomeForm, ExpenseForm


@login_required
def home(request):
    transactions = Transaction.objects.filter(user=request.user)
    total_sum = sum(t.amount if t.category == 'income' else -t.amount for t in transactions)

    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        Transaction.objects.create(user=request.user, amount=amount, category=category)
        return redirect('home')

    return render(request, 'home.html', {'total_sum': total_sum})

@login_required
def income_view(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            amount = form.cleaned_data['amount']
            Transaction.objects.create(user=request.user, amount=amount, category=category.name, transaction_type='income')
            return redirect('home')
    else:
        form = IncomeForm()
    return render(request, 'income.html', {'form': form})

@login_required
def expense_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            amount = form.cleaned_data['amount']
            Transaction.objects.create(user=request.user, amount=amount, category=category.name)
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'expense.html', {'form': form})
