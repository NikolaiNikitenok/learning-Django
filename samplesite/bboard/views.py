from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import BbForm

from .models import Bb, Rubric

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs,
               'rubrics': rubrics
               }
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs,
               'rubrics': rubrics,
               'current_rubric': current_rubric
               }
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    model = Bb
    template_name = "bboard/create.html"  # Файл-шаблон, создающий форму
    form_class = BbForm  # Ссылка на класс формы, связанной с моделью
    success_url = reverse_lazy('index') # Перенаправления после успешного сохранения
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rubrics"] = Rubric.objects.all()
        return context
    

