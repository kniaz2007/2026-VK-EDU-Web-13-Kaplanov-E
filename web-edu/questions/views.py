from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

QUESTION_LIST = []
for i in range(30):
    QUESTION_LIST. append({
        'id': i + 1,
        'title': f'Вопрос {i + 1}',
        'text': f'Что-то там написал пользователь {i + 1}'
    })
def index(request):
    page_number = request.GET.get('page', 1)
    page = Paginator(QUESTION_LIST, 5)
    page_obj = page.get_page(page_number)
    return render(request, 'questions/index.html', context={'questions': page_obj.object_list, 'page_obj': page_obj})

def hot(request):
    page_number = request.GET.get('page', 1)
    page = Paginator(QUESTION_LIST[:22], 5)
    page_obj = page.get_page(page_number)
    return render(request, 'questions/hot.html', context={'questions': page_obj.object_list, 'page_obj': page_obj})

def add(request):
    return render(request, 'questions/add_question.html')

def reg(request):
    return render(request, 'questions/reg.html')
def login(request):
    return render(request, 'questions/login.html')

def one_question(request):
    return render(request, 'questions/one_question.html')

def setings(request):
    return render(request, 'questions/setings.html')

def tag(request):
    page_number = request.GET.get('page', 1)
    page = Paginator(QUESTION_LIST[:6], 5)
    page_obj = page.get_page(page_number)
    return render(request, 'questions/tag.html', context={'questions': page_obj.object_list, 'page_obj': page_obj})