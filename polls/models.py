from django.db import models
class question(models.Model):
    question_text=models.CharField(max_length=200)
    time=models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
class answer(models.Model):
    question=models.ForeignKey(question,on_delete=models.CASCADE,related_name="choice")
    answer=models.CharField(max_length=200)
    num=models.IntegerField(default=0)
    def __str__(self):
        return self.answer
class User(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return self.username
# Create your models here.
