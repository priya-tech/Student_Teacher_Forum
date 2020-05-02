from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AdduserForm,AddQuestionsForm
from django.urls import reverse
from .models import AdduserModel,AddQuestionsModel,AddAnswersModel,CommentModel
import datetime
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core import mail
from django.conf import settings
# Create your views here.

def home(request,name):
    ctx = {}
    url_parameter = request.GET.get("q")


    if url_parameter:
        questions = AddQuestionsModel.objects.filter(title__icontains=url_parameter)
    else:
        questions = AddQuestionsModel.objects.all()

    ctx["questions"] = questions
    ctx["name"] = name
    if request.is_ajax():
        html = render_to_string(
            template_name = "forumapp/search-results-partial.html", context={"questions":questions , "name":name}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict,safe=False)
    return render(request, 'forumapp/home.html', context=ctx)

def login(request):
    if request.method=='POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        checkname = AdduserModel.objects.filter(name__icontains=name)
        if checkname:
            passwords=[x.password for x in checkname]
            if password in passwords:
                return HttpResponseRedirect(reverse('view_home',kwargs={'name':name}))
            else:
                return HttpResponse('<script>alert("Login error! Password incorrect")</script>')
        else:
            return HttpResponse('<script>alert("Username does not exists!")</script>')
    else:
        return render(request, 'forumapp/login.html')

def check(request,**kwargs):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('psw')
        ques = AddQuestionsModel.objects.get(id=kwargs['id'])
        if ques.name.name == username:
            psw = AdduserModel.objects.get(name=username)
            if password == psw.password:
                if kwargs['action']=='edit':
                    id=kwargs['id']
                    name=kwargs['name']
                    return HttpResponseRedirect(reverse('edit_question',kwargs={'name':name, 'action':'edit','id':id}))
                elif kwargs['action']=='delete':
                    id=kwargs['id']
                    name=kwargs['name']
                    return HttpResponseRedirect(reverse('delete_question',kwargs={'name':name, 'id':id}))
            else:
                return HttpResponse('<script>alert("Login error! Password incorrect")</script>')
        else:
            return HttpResponse('<script>alert("Username does not exists!")</script>')


def register(request):
    if request.method=='POST':
        form=AdduserForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('user_login'))
    else:
        form=AdduserForm()
        return render(request,'forumapp/register.html',{'form':form})


def askquestion(request,name):
    if request.method=='POST':
        s=AddQuestionsModel()
        s.name = AdduserModel.objects.get(name=name)
        s.title = request.POST.get('title')
        s.content = request.POST.get('content')
        s.save()
        return HttpResponseRedirect(reverse('view_home',kwargs={'name':name}))
    else:
        return render(request,'forumapp/askquestions.html', {'profilename':name})


def viewanswers(request,id,name):
    answer = AddQuestionsModel.objects.get(id=id)
    all=AddAnswersModel.objects.filter(question__id=id)
    if request.method=="POST":
        b=AddAnswersModel()
        b.name=request.POST.get('name')
        b.answer=request.POST.get('answer')
        b.question=AddQuestionsModel.objects.get(id=id)
        b.save()
    return render(request, 'forumapp/viewanswers.html', {'ans':answer, 'allanswers':all, 'name':name, 'id':id})

def deletequestion(request,name,id):
    AddQuestionsModel.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('view_home',kwargs={'name':name}))

def editquestion(request,**kwargs):
    if kwargs['action']=='edit':
        question=AddQuestionsModel.objects.get(id=kwargs['id'])
        return render(request, 'forumapp/editquestion.html', {'question':question, 'profilename':kwargs['name']})
    if kwargs['action']=='submit':
        question=AddQuestionsModel.objects.get(id=kwargs['id'])
        name=request.GET.get('name')
        question.name=AdduserModel.objects.get(name=name)
        question.title=request.GET.get('title')
        question.content=request.GET.get('content')
        question.date=datetime.datetime.now()
        question.save()
        return HttpResponseRedirect(reverse('view_home',kwargs={'name':kwargs['name']}))

def comment(request,id,name,qid):
    allcomment=CommentModel.objects.filter(commentfor__id=id)
    if request.method=="POST":
        g=CommentModel()
        g.name = request.POST.get('name')
        g.comment=request.POST.get('comment')
        g.commentfor = AddAnswersModel.objects.get(id=id)
        g.save()
        return HttpResponseRedirect(reverse('view_answers',args=(qid,name)))
    else:
        return render(request,'forumapp/comment.html',{'id':id , 'allcomments':allcomment, 'name':name, 'qid':qid})
