from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.general.models import Subscription
# Create your views here.


@login_required
def pricing(request):
    context={
        'subscriptions':Subscription.objects.all()
    }
    return render(request,'dashboard/pricing/index.html',context)
