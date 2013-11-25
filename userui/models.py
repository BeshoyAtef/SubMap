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
            sequence = b.number
            block_order.append(sequence)

        return block_order


    def getUserTrials(self):
        block = self.getUserBlocks()
        print block
        print "hello"
        orderedQuestions = []
        for b in block :
            trials = Trials.objects.filter(blockId = b.number).order_by('order')
            for trial in trials:
                orderedQuestions.append(trial)
        return orderedQuestions




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

    def __unicode__(self):
        # return "Trial_id:%s,Point (%s,%s),BlK_id:%s,Order:%s " % (self.id,self.pointA,self.pointB, self.blockId,self.order)
        return "Trial_TEXT:%s," % (self.task_text)
    class Meta:
        unique_together = ("trialNumber","blockId")

class Results (models.Model):
    uID = models.ForeignKey('UserProfile')
    blockID = models.IntegerField(default = 0)
    trialID = models.IntegerField(default = 0)
    userAnswer = models.CharField(max_length = 30)

    class Meta:
        unique_together = ("uID","blockID","trialID")

