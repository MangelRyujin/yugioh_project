from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def unpaid_order(request):
    return render(request,'dashboard/order/unpaid_order/index.html')
