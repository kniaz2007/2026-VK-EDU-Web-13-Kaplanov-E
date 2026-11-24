from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.shortcuts import render, get_object_or_404
# Create your views here.

def Paginate(request, questions, per_page=5):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(questions, per_page)
    return paginator.get_page(page_number)
def index(request):
    questions = Question.objects.new()
    page_obj = Paginate(request, questions, 5)
    tags = Tag.objects.popular()
    return render(request, 'questions/index.html', context={'questions': page_obj.object_list, 'page_obj': page_obj, 'popular_tags': tags})

def hot(request):
    questions = Question.objects.best()
    page_obj = Paginate(request, questions, 5)
    tags = Tag.objects.popular()
    return render(request, 'questions/hot.html', context={'questions': page_obj.object_list, 'page_obj': page_obj, 'popular_tags':tags})

def add(request):
    tags = Tag.objects.popular()
    return render(request, 'questions/add_question.html', context = {'popular_tags':tags})

def reg(request):
    return render(request, 'questions/reg.html')

def login(request):
    return render(request, 'questions/login.html')

def one_question(request, question_id):
    question_1 = get_object_or_404(Question, id=question_id, is_active=True)
    answers = Answer.objects.new().filter(question = question_1, is_active = True)
    tags = Tag.objects.popular()
    page_obj = Paginate(request, answers, 5)
    return render(request, 'questions/one_question.html', context = {'question':question_1, 'answers':page_obj.object_list, 'popular_tags':tags, 'page_obj': page_obj})

def setings(request):
    tags = Tag.objects.popular()
    return render(request, 'questions/setings.html', context = {'popular_tags':tags})

def tag(request, tag_name):
    current_tag = get_object_or_404(Tag, name=tag_name)
    questions = Question.objects.by_tag(tag_name)
    page_obj = Paginate(request, questions, 5)
    tags = Tag.objects.popular()
    return render(request, 'questions/tag.html', context={'questions': page_obj.object_list, 'page_obj': page_obj, 'popular_tags':tags, 'tag': current_tag})
