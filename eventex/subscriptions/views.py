# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from forms import SubscriptionForm
from models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})
    
    obj = form.save()        
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)

def detail(request, pk):
    obj = get_object_or_404(Subscription, pk=pk)
    return render(request, 'subscriptions/subscription_detail.html', {'subscription': obj})
