from django.shortcuts import render

# Create your views here.

def album(request):
    context={'list':[0,1,3,4,56,7,8,9,12,4112,41,0,1,3,4,56,7,8,9,12,4112,41,0,1,3,4,56,7,8,9,12,4112,41]}
    return render(request,'dashboard/album/index.html',context)
