#Imports
from userui.models import *
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

#End Imports


# Create your views here.

def index(request):
	trails = Trail.obejcts.filter(block=block).order_by('order')
    return render(request, 'index.html',{trails:"trails"})

def submitter(request,block,trial,user):
	user = UserProfile.objects.get(pk=user)
	trial = Trail.objects.get(pk=trial,blockId=block)
	result=saver(request,trail)
	trails = (Trail.obejcts.filter(block=block).values_list('trailsNumber', flat=True))

	answered_trials = (Result.objects.filter(user=user,blockNumber=block,).values_list('trailsNumber', flat=True))
	available_trails = (Trail.objects.filter(block=block).exclude('id__in' = answered_trials)
	print available_trails


	return render(request, 'index.html')




def saver(request,trail):
	answer = request.POST['answer']
	result = Result(user=user,userblock=userblock,trial=trial,answer=answer)
	result.save()
	return result

