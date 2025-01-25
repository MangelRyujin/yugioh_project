from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='/login/')
def paid_order(request):
    return render(request,'dashboard/order/paid_order/index.html')
