from django.shortcuts import render, get_object_or_404, redirect
from .models import Tournment,Teams,Player
from . import forms
from . import models
from django.views.generic import (DetailView,UpdateView,CreateView,)
# Create your views here.
def Tournmentt(request):
    if request.method == 'POST':
        form = forms.Player(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
    my_obj = Tournment.objects.all()
    my_dict = {'data':my_obj}
    return render(request,'Tournment.html',my_dict)

class Team(DetailView):
    context_object_name = 'Tournment_details'
    model = models.Tournment
    template_name = 'Team.html'

class Players(DetailView):
    context_object_name = 'Team_details'
    model = models.Teams
    template_name = 'Players.html'

class TournmentCreateView(CreateView):
    fields = ("__all__")
    model = models.Tournment
    template_name = 'Add_Tournment.html'

def form_Team(request):
    if request.method == 'POST':
        post=Tournment()
        post.name= request.POST.get('name')
        post.save()
    form = forms.Teams()
    my_dict = {'form':form}
    return render(request,'Add_Team.html',my_dict)

def form_Player(request):
    if request.method == 'POST':
        form = forms.Teams(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
    form = forms.Player()
    my_dict = {'form':form}
    return render(request,'Add_Players.html',my_dict)

def Delete_Tournment(request):
    my_obj = Tournment.objects.all()
    my_dict = {'data':my_obj}
    return render(request,'Delete_Tournment.html',my_dict)

class Delete_Team(DetailView):
    context_object_name = 'Tournment_details'
    model = models.Tournment
    template_name = 'Delete_Teams.html'

class Delete_Players(DetailView):
    context_object_name = 'Team_details'
    model = models.Teams
    template_name = 'Delete_Players.html'


def Delete_T(request, pk):
    comment = get_object_or_404(Tournment, pk=pk)
    comment.delete()
    return redirect('Tournment')


def Delete_TM(request, pk):
    comment = get_object_or_404(Teams, pk=pk)
    comment.delete()
    return redirect('Tournment')


def Delete_P(request, pk):
    comment = get_object_or_404(Player, pk=pk)
    comment.delete()
    return redirect('Tournment')

class PlayerUpdate(UpdateView):
    fields = ('runs','wickets')
    model = Player
    template_name = 'PlayerUpdate.html'
# Create your views here.
