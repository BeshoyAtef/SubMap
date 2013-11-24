#Imports
from userui.models import *
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

#End Imports


# Create your views here.

def index(request):
    available_trails = Trial.objects.all().order_by('order')
    return render(request,'index.html',{'trials': available_trails})


def submitter(request,block,trial,user):
    user = UserProfile.objects.get(pk=user)
    
    answered_trials = (Results.objects.filter(uID=user,blockID=1).values_list('trialID', flat=True))
    if answered_trials :
        available_trails = Trial.objects.filter(blockId=1).exclude(trialNumber=answered_trials).order_by('order')
    else:
        available_trails = Trial.objects.filter(blockId=1).order_by('order')
    return render(request,'index.html',{'trials': available_trails})



def saver(request,trail):
    answer = request.POST['answer']
    result = Result(user=user,userblock=userblock,trial=trial,answer=answer)
    result.save()
    return result

