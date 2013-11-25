#Imports
from userui.models import *
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

#End Imports


# Create your views here.
def test2(request):
    available_trails = Trial.objects.all().order_by('order')
    return render(request,'testTrial.html',{'trial': available_trails[0]})

def test(request):
    available_trails = Trial.objects.all().order_by('order')
    return render(request,'testTrial.html',{'trial': available_trails[0]})
    return render(request,'testTrial2.html')

def index(request):
    available_trails = Trial.objects.all().order_by('order')
    return render(request,'index.html',{'trials': available_trails})


def renderer(request,user,block,trial):
    user = UserProfile.objects.get(pk=user)
    
    answered_trials = (Results.objects.filter(uID=user,blockID=1).values_list('trialID', flat=True))
    if answered_trials :
        available_trails = Trial.objects.filter(blockId=1).exclude(trialNumber=answered_trials).order_by('order')
    else:
        available_trails = Trial.objects.filter(blockId=1).order_by('order')
    return render(request,'index.html',{'trials': available_trails})

def submitter(request,user,block,trial):
    flag=saver(request,user,block,trial)
    user = UserProfile.objects.get(pk=user)
    
    answered_trials = (Results.objects.filter(uID=user,blockID=1).values_list('trialID', flat=True))
    if answered_trials :
        available_trails = Trial.objects.filter(blockId=1).exclude(trialNumber=answered_trials).order_by('order')
    else:
        available_trails = Trial.objects.filter(blockId=1).order_by('order')
    return render(request,'index.html',{'trials': available_trails})




def saver(request,user,block,trial):
    user = UserProfile.objects.get(pk=user)
    answer = request.POST['answer']
    result = Results(uID=user,blockID=block,trialID=trial,userAnswer=answer)
    result.save()
    return True

