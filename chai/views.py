from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'all_chai.html',{'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, id=id)
    return render(request, 'chai_detail.html', {'chai': chai})