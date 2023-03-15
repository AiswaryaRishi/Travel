from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    ob=Team.objects.all()
    return render(request, "index.html",{'result':obj,'tem':ob})



#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #z=int(x+y)
    #c=int(x-y)
    #d=int(x*y)
    #e=int(x/y)
    #return render(request,'result.html',{'result':z,'sub':c,'mul':d,'div':e});

#def about(request):
    #return render(request, "about.html");


#def contact(request):
    #return HttpResponse("hai.its contact");
