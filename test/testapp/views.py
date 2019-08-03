from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def serviceDB(request):
    if request.method == 'POST':
        form = AllServicesForm(request.POST)
        post = form.save(commit=False)
        post.save()
        return redirect('serviceDB')
    else:
        form = AllServicesForm()
        return render(request, 'serviceDB.html', {'form':form})

@login_required
def home(request):
    myServices = SelectedService.objects.all()
    return render(request, 'home.html', {'myServices':myServices})

@login_required
def serviceAll(request):
    services = AllServices.objects.all()
    return render(request, 'serviceAll.html', {'services':services})

@login_required
def detail(request, slug):
    service = AllServices.objects.get(slug=slug)
    return render(request, 'detail.html', {'service':service})

@login_required
def addToMy(request, slug):
    service = get_object_or_404(AllServices, slug=slug)
    selecting, created = SelectedService.objects.get_or_create(
            service = service,
            user = request.user,
            selected = False
        )
    selectQs = Select.objects.filter(
            user=request.user,
            selected=False
        )
    if selectQs.exists():
        select = selectQs[0]
        if select.services.filter(service__slug=service.slug).exists():
             selecting.save()
        else:
            select.services.add(selecting)
    else:
        select = Select.objects.create(user=request.user)
        select.services.add(selecting)
    return redirect('home')

@login_required
def removeFromMy(request, slug):
    service = get_object_or_404(AllServices, slug=slug)
    selectQs = Select.objects.filter(
        user = request.user,
        selected = False
    )
    if selectQs.exists():
        select = selectQs[0]
        if select.services.filter(service__slug=service.slug).exists():
            selecting = SelectedService.objects.filter(
                service = service,
                user = request.user,
                selected = False
            )[0]
            select.services.remove(selecting)
            return redirect('home')
        else:
            return redirect('home') # if문이 여기에 걸림,,,
    else:
        return redirect('home')
     