from django.shortcuts import render, redirect
from .models import Voters
 
# Create your views here.
#voterid, name, gender, age,place,status
def index(request):
    if 'search' in request.GET:
        search=request.GET['search']
        voter = Voters.objects.filter(voterid_icontains=search)
    else:
        voter = Voters.objects.all()
    members = Voters.objects.all()
    context = {'members': members}
    return render(request, 'index.html', context)
 
def create(request):
    member = Voters(voterid=request.POST['voterid'], name=request.POST['name'], gender=request.POST['gender'],age=request.POST['age'], place=request.POST['place'],status=request.POST['status'])
    member.save()
    return redirect('/')
 
def edit(request, id):
    members = Voters.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)
 
def update(request, id):
    member = Voters.objects.get(id=id)
    member.voterid = request.POST['voterid']
    member.name = request.POST['name']
    member.gender = request.POST['gender']
    member.age = request.POST['age']
    member.place = request.POST['place']
    member.status = request.POST['status']
    member.save()
    return redirect('/')
 
def delete(request, id):
    member = Voters.objects.get(id=id)
    member.delete()
    return redirect('/')