from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.order.models import Item
# Create your views here.



@login_required(login_url='/login/')
def unpaid_order(request):
    items= Item.objects.filter(state="1",seller=request.user).order_by("pk")
    context={
        "items":items
    }
    return render(request,'dashboard/order/unpaid_order/index.html',context)
