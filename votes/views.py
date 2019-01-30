from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate, Position, Vote
from .forms import PositionModelForm, CandidateModelForm, VoteModelForm

# Create your views here.

def index(request):
    context = {}
    candidate = Candidate.objects.all().order_by('position')
    context['candidates'] = candidate
    return render(request, 'index.html', context)

def position_create(request):
    context = {}
    if request.method == 'POST':
        form = PositionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = PositionModelForm()
            return render(request, 'position_create.html', context)
    else:
        context['form'] = PositionModelForm()
        return render(request, 'position_create.html', context)

def candidate_create(request):
    context = {}
    if request.method == 'POST':
        form = CandidateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = CandidateModelForm()
            return render(request, 'candidate_create.html', context)
    else:
        context['form'] = CandidateModelForm()
        return render(request, 'candidate_create.html', context)

def candidate_detail(request, candidate_id):
    context = {}
    context['candidate'] = Candidate.objects.get(id=candidate_id)
    return render(request, 'candidate_detail.html', context)

def candidate_update(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)
    if request.method == 'POST':
        form = CandidateModelForm(request.POST, instance = candidate)
        if form.is_valid():
            form.save()
            return redirect('votes:candidate_detail', candidate_id=candidate_id )
        else:
            context['form'] = CandidateModelForm(instance=candidate)
            return render(request, 'candidate_update.html', context)
    else:
        context['form'] = CandidateModelForm(instance=candidate)
        return render(request, 'candidate_update.html', context)

def vote(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)
    vote = Vote.objects.create(candidate=candidate)
    return redirect('votes:index')
    # context['form'] = CandidateModelForm(instance=candidate)
    # return render(request, 'candidate_update.html', context)
