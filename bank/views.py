from decimal import Decimal, getcontext
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import UserLoginForm
from accounts.models import CustomUser, Transaction
from .forms import AccountTypeForm
from accounts.forms import TransactionForm, TransferForm
from .models import AccType

getcontext().prec = 2



# Create your views here.
@login_required
def transferView(request):
    form = TransferForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['reciepient']
            amount = form.cleaned_data['amount']
            reciepient = CustomUser.objects.get(username=username)
            
            print(request.user.currentBalance)
            print(reciepient.id)

            if request.user.currentBalance >= Decimal(amount):
                request.user.currentBalance = request.user.currentBalance - Decimal(amount)
                request.user.save()
                Transaction.objects.create(amount=amount, activity='transfer', updatedBy=request.user, user=request.user)

                reciepient.currentBalance = reciepient.currentBalance + Decimal(amount)
                reciepient.save()
                Transaction.objects.create(amount=amount, activity='transfer', updatedBy=request.user, user=reciepient)

                return render(request, 'bank/transfer.html',context)
            else:
                messages.error(request, 'Your account balance is insufficient')
                return render(request, 'bank/transfer.html',context)
        else:
            messages.error(request, 'Form not correctly filled')
            return render(request, 'bank/transfer.html',context)
    else:
        return render(request, 'bank/transfer.html',context)


@login_required
def statementView(request, id=None):
    transactions = Transaction.objects.filter(user_id=id).order_by('-id')
    context = {
        'transactions': transactions,
    }
    return render(request, 'bank/statement.html', context)


@login_required
def clientProfileView(request):
    return render(request, 'bank/client_profile.html')


@login_required
def depositeView(request, id=None):   
    form = TransactionForm(initial={'user':request.user , 'updatedBy':request.user})
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            trans = form.save(commit=False)
            trans.save()
            request.user.currentBalance = request.user.currentBalance + trans.amount
            request.user.save()
            messages.success(request, 'Account credited successfully')
            form = TransactionForm()
            return render(request, 'bank/deposite.html', context)
        else:
           context['form'] = form
           messages.error(request, 'Account not credited.')
           return render(request, 'bank/deposite.html', context)
        
    return render(request, 'bank/deposite.html', context)

@login_required
def withdrawalView(request, id=None):
    form = TransactionForm(initial={'user':request.user , 'updatedBy':request.user, 'activity':'withdrawal'})
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            trans = form.save(commit=False)
            trans.save()
            request.user.currentBalance = request.user.currentBalance - trans.amount
            request.user.save()
            messages.success(request, 'Account debited successfully')
            form = TransactionForm()
            return render(request, 'bank/withdrawal.html', context)
        else:
           context['form'] = form
           messages.error(request, 'Account not debited.')
           return render(request, 'bank/withdrawal.html', context)
    return render(request, 'bank/withdrawal.html', context)


def createAccountTypeView(request):
    form = AccountTypeForm()
    context = {
        'form':form,
    }
    if request.method == "POST":
        form = AccountTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account type successfully created')
            return redirect('accountType')
        else:
            messages.error(request, 'Account type was not created')
            context['form'] = form
            return render(request, 'bank/createAccountType.html', context) 
    else:
        return render(request, 'bank/createAccountType.html', context)


def accountTypeView(request):
    accountTypes = AccType.objects.all()
    context = {
        'accountTypes': accountTypes,
    }
    return render(request, 'bank/accountType.html', context)


def home(request):
    form = UserLoginForm()
    context = {
        'form':form,
    }
    return render(request, 'bank/index.html', context)


def clientsView(request):
    clients = CustomUser.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'bank/clients.html', context)


@login_required
def clientDashboardView(request):

    transactions = Transaction.objects.filter(user_id=request.user.id).order_by('-id')
    context = {
        'transactions':transactions,
    }
    return render(request, 'bank/user_dashboard.html', context)


@login_required
def adminDashboardView(request):
    clients = CustomUser.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'bank/admin_dashboard.html', context)