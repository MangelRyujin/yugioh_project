from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def delivery_pakage(request):
    return render(request,'dashboard/order/delivery_pakage/index.html')
