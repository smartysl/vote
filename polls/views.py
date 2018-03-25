from django.shortcuts import render,get_object_or_404
from .models import question,answer,User
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .form import Userform
from django.contrib.auth import login,authenticate,logout
def index(request):
    if request.user.is_authenticated:
        last_question_list=question.objects.order_by('-time')[:5]
        out_put='.'.join(q.question_text for q in last_question_list)
        return render(request,'polls/index.html',{'last_question_list':last_question_list})
    else:
        return HttpResponseRedirect('/polls/login/')
def detail(request,question_id):
    questions=get_object_or_404(question,pk=question_id)
    return render(request,'polls/detail.html',{'question':questions})
def result(request,question_id):
    questions=get_object_or_404(question,pk=question_id)
    return render(request,'polls/result.html',{"question":questions})
def vote(request,question_id):
    questions=get_object_or_404(question,pk=question_id)
    try:
        selected_choice=questions.choice.get(pk=request.POST['choice'])
    except(KeyError,answer.DoesNotExist):
        return render(request,"polls/detail.html",{'error_message':"选择失败","question":questions})
    else:
        selected_choice.num=selected_choice.num+1
        selected_choice.save()
        return HttpResponseRedirect(reverse('result',args=(questions.id,)))
def register(request):
    if request.method=="POST":
        userform=Userform(request.POST)
        if userform.is_valid():
            username=userform.cleaned_data['username']
            password=userform.cleaned_data['password']
            email=userform.cleaned_data['email']
            User.objects.create(username=username,password=password,email=email)
            return HttpResponse("注册成功！")
    else:
        userform=Userform()
        return render(request,'polls/regist.html',{'userform':userform})
def Login(request):
    if request.method=="POST":
        userform=Userform(request.POST)
        if userform.is_valid():
            username=userform.cleaned_data['username']
            password=userform.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect('/polls/')
    else:
        userform=Userform()
        return render(request,'polls/login.html',{"userform":userform})
def Logout(request):
    logout(request)
    return HttpResponse("登出成功")




# Create your views here.
