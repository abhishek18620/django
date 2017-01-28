import datetime
from django.db import models
import mysql.connector as cm
try:
    from .settings import any_keys
except:
    print("error cannt import settings")

class sample(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    publisher = models.CharField

    def fill(self , txt , pub):
        self.question_text = txt
        self.pub_date = datetime.datetime.now()
        self.publisher = pub
    
    # def save(self, *args, **kwargs):
    #     if self.question_text is not None and self.pub_date is not None and self.publisher is not None:
    #         self.question_text = "nothing"
    #         self.pub_date = datetime.datetime.now()
    #         self.publisher = "abhishek"
    #     super(sample,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.question_text
        
class user_info(models.Model):
    uname = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    password = models.BooleanField()
    # field of int.( 1 = project , 2 = compcoding , 3 = dev)
    foi = models.IntegerField()

# # making connection     
# conn = cm.connect (host = "localhost",
# user = "root",
# passwd = 'grandma',
# db = "users")
# cursor = conn.cursor ()
# cursor.execute ("select * from info ")
# row = cursor.fetchone ()
# while row != None:
#     print ("Hello {0}!and ur name is  {0}!".format(row[0]))
#     row = cursor.fetchone ()
# cursor.close ()
# conn.close ()

#class sens_info():
