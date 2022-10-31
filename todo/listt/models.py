


from django.db import models
import datetime

# Create your models here.
from django.contrib.auth.models import User

class todo(models.Model):
    taskstatus=[
        ('C','C'), 


        ('P','P'),
    ]
    priority=[
        
    ('1','1' ),
    ('2','2' ),
    ('3','3' ),
    ('4','4' ),
    ('5','5' ),
    ('6','6' ),
    ('7','7' ),
    ('8','8' ),
    ('9','9' ),
    ('10','10'),
    ]

    title=models.CharField(max_length=50)
    status=models.CharField(max_length=2,choices=taskstatus)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    deadline_date=models.DateField()
    deadline_time=models.TimeField()
    priority=models.CharField(max_length=2,choices=priority)
    

    def remainingtime(self):
        x = datetime.datetime.now()
   
        start=datetime.datetime(x.year,x.month,x.day,x.hour,x.minute,x.second)

        y=self.deadline_date
        z=self.deadline_time
        
        
        endd=datetime.datetime(y.year,y.month,y.day,z.hour,z.minute,z.second)
        diff=endd-start
        hour=int(diff.total_seconds()/(3600))
        min=int((diff.total_seconds()/60)-(hour*60))
        sec=int((diff.total_seconds())-(hour*3600)-(min*60))
        timee={
        'h':hour,
            'm':min,
             's':sec
         }

        return timee


