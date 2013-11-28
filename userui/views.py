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
    pnum = request.GET['participant_num']
    current_participant = UserProfile.objects.get(id=pnum)
    participants_blocks = current_participant.getUserBlocks()
    next_trial=renderer(request,pnum,participants_blocks[0].number)
    d = {'participants_blocks': participants_blocks}
    if next_trial["trial"].technique == 1:
        return render(request,'testTrial.html',next_trial)
    elif next_trial["trial"].technique == 2:
        return render(request,'testTrial2.html',next_trial)
    else :
        return render(request,'testTrial3.html',next_trial)

def index(request):
    return render(request,'index.html')


def renderer(request,user,block):
    print user
    print block
    user = UserProfile.objects.get(pk=user)    
    answered_trials = (Results.objects.filter(uID=user,blockID=block).values_list('trialID', flat=True))
    print answered_trials
    if answered_trials :
        available_trails = Trial.objects.filter(blockId=block).exclude(trialNumber__in=answered_trials).order_by('order')
    else:
        available_trails = Trial.objects.filter(blockId=block).order_by('order')
        print available_trails
        print available_trails[0]
    return {'u':user.id,'trial': available_trails[0]}

def submitter(request,user,block,trial):
    print request.POST["d2"]
    flag=saver(request,user,block,trial)
    user = UserProfile.objects.get(pk=user)
    answered_trials = (Results.objects.filter(uID=user,blockID=block).values_list('trialID', flat=True))
    print answered_trials
    if answered_trials :
        available_trails = Trial.objects.filter(blockId=block).exclude(trialNumber__in=answered_trials).order_by('order')
        print available_trails
    else:
        available_trails = Trial.objects.filter(blockId=block).order_by('order')
        print available_trails
    next_trial=available_trails[0]    
    if next_trial.technique == 1:
        return render(request,'testTrial.html',{'trial': next_trial})
    elif next_trial.technique == 2:
        return render(request,'testTrial2.html',{'trial': next_trial})
    else :
        return render(request,'testTrial3.html',{'trial': next_trial})




def saver(request,user,block,trial):
    user = UserProfile.objects.get(pk=user)
    answer = request.POST['answer']
    result = Results(uID=user,blockID=block,trialID=trial,userAnswer=answer)
    result.save()
    return True

def checker(request):
    return True 
