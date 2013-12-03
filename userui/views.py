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

def colortest_view(request):
    return render(request,'colortest.html')

def submit_colortest(request):
    x= Colortest(
        uID = UserProfile.objects.get(pk=request.POST["participant_num"]),
        answer_1 = request.POST["1"],
        answer_2 = request.POST["2"],
        answer_3 = request.POST["3"],
        answer_4 = request.POST["4"],
        answer_5 = request.POST["5"],
        answer_6 = request.POST["6"])
    x.save()
    if x.answer_1 == 2 and x.answer_2 == 10 and x.answer_3 == 16 and x.answer_4 == 29 and x.answer_5 == 5 and x.answer_6 == 7:
        print "Passed"
        return render(request,'index.html',{'Pass': True})
    else:
        print "Failed"
        return render(request,'index.html',{'Pass': False})

def renderer(request,user,block):
    print user
    print block
    user = UserProfile.objects.get(pk=user)   
    block=user.getUserBlocks()[0].id
    answered_trials = (Results.objects.filter(uID=user,blockID=block).values_list('trialID', flat=True))
    if answered_trials :
        available_trails = Trial.objects.filter(blockId=block).exclude(trialNumber__in=answered_trials).order_by('order')
    else:
        available_trails = Trial.objects.filter(blockId=block).order_by('order')
    if available_trails:
        return {'u':user.id,'trial': available_trails[0]}
    else :
        render(request,'index.html',{'Pass': True})


def submitter(request,user,block,trial):
    flag=saver(request,user,block,trial)
    user = UserProfile.objects.get(pk=user)
    # place for old stuff
    next_trial=renderer(request,user,block)['trial']   
    if next_trial.technique == 1:
        return render(request,'testTrial.html',{'u':user.id,'trial': next_trial})
    elif next_trial.technique == 2:
        return render(request,'testTrial2.html',{'u':user.id,'trial': next_trial})
    else :
        return render(request,'testTrial3.html',{'u':user.id,'trial': next_trial})

    # answered_trials = (Results.objects.filter(uID=user,blockID=block).values_list('trialID', flat=True))
    # print str(len(answered_trials))+":"+str(len(Trial.objects.filter(blockId=block)))
    # print answered_trials
    # if answered_trials :
    #     available_trails = Trial.objects.filter(blockId=block).exclude(trialNumber__in=answered_trials).order_by('order')
    #     print available_trails
    # else:
    #     available_trails = Trial.objects.filter(blockId=block).order_by('order')


def saver(request,user,block,trial):
    user = UserProfile.objects.get(pk=user)
    answer = request.POST['answer']
    result = Results(uID=user,blockID=block,trialID=trial,userAnswer=answer)
    result.save()
    return True

def checker(request):
    return True 
