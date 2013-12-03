from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import utc
import datetime
from datetime import timedelta


#this class inherits AbstractBaseUser (password, login_now) and adds to these 2 fields the fields that i wrote 
#when AbstractBaseUSer is inherited u have to follow 3 min requirments , 1. the class has to have a numeric primary key 
#2.the class has to have a unique identifer which in this case is email and its written in USERNAME_FIELD which is the fields that uniquly identify the user 
#there is also a field called REQIURED fields which is a list of all the fields except the USER_field that are requied for creating the user 
#3.the class should have 2 methods get_full_name and get_short_name which doesnt take paramters and returns an identifyer of the user in my case its email but it can be username , and both can be the same 
#for this class a custom manager is made beause i have different attributes than the USer model built in . this manager is called from the class .
class UserProfile(models.Model):
    date_Of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20 , null=True)
    is_admin = models.BooleanField(default=False)           
    occupation = models.CharField(max_length=30, null = True)
    Notes = models.CharField(max_length=200, null = True)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
     )
    gender = models.CharField(max_length=1, choices=gender_choices , null=True)

    def __unicode__(self):
        return "User ID :%s" % (self.id)

    def getUserBlocks(self):
        block_seq = UserBlocks.objects.filter(user_id = self.id)
        block_order = []
        for b in block_seq:
            answered_trials = (Results.objects.filter(uID=self,blockID=b.number).values_list('trialID', flat=True))
            if len(answered_trials) == len(Trial.objects.filter(blockId=b.number)):
                print "execlude"
            else:
                sequence = b
                block_order.append(sequence.id)
        return block_order


    def getUserTrials(self):
        block = self.getUserBlocks()
        print block
        print block
        available_trails = Trial.objects.filter(blockId__in=block).order_by('order')
        print available_trails
        answered_trials = (Results.objects.filter(uID=self,blockID__in=block).values_list('trialID', flat=True))
        print answered_trials
        if answered_trials :
            available_trails = answered_trials.exclude(trialNumber__in=answered_trials).order_by('order')
            print available_trails
        else:
            available_trails = Trial.objects.filter(blockId__in=block).order_by('order')
            print available_trails
        return available_trails




class UserBlocks(models.Model):
    number = models.CharField(max_length = 1)
    user = models.ForeignKey(UserProfile)

    class Meta:
        unique_together = ("user","number")

    def __unicode__(self):
        return "UserBlocks_id:%s,Number:%s" % (self.id, self.number)


class Trial(models.Model):
    trialNumber = models.IntegerField(default = 0)
    task_text = models.CharField(max_length = 400)
    pointA = models.CharField(max_length = 30)
    pointB = models.CharField(max_length = 30, null = True, blank = True)
    expectedAnswer = models.CharField(max_length = 30)
    blockId = models.IntegerField(default = 0)
    order = models.IntegerField(default=0)
    technique =  models.IntegerField(default=0)
    task = models.IntegerField(default=0)

    def __unicode__(self):
        return "Trial_id:%s,BlK_id:%s,Order:%s,Task:%s,Techni:%s" % (self.id,self.blockId,self.order,self.task,self.technique)
        # return "Trial_TEXT:%s," % (self.task_text)
    class Meta:
        unique_together = ("trialNumber","blockId","order")

class Results (models.Model):
    uID = models.ForeignKey('UserProfile')
    blockID = models.IntegerField(default = 0)
    trialID = models.IntegerField(default = 0)
    userAnswer = models.CharField(max_length = 30)
    time = models.DecimalField(default = 0,max_digits=10, decimal_places=3)
    alts = models.CharField(max_length = 1500)
    class Meta:
        unique_together = ("uID","blockID","trialID")

class Colortest (models.Model):
    uID = models.ForeignKey('UserProfile')
    answer_1 = models.IntegerField(default = 0)
    answer_2 = models.IntegerField(default = 0)
    answer_3 = models.IntegerField(default = 0)
    answer_4 = models.IntegerField(default = 0)
    answer_5 = models.IntegerField(default = 0)
    answer_6 = models.IntegerField(default = 0)




