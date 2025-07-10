from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'all_chai.html',{'chais': chais})

