from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Bb
from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    items = Bb.objects.all()
    rubrics = Rubric.objects.all()
    return render(request, 'bboard/index.html', {'items': items, 'rubrics': rubrics})


class indexView(TemplateView):
    template_name = 'bboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['items'] = Bb.objects.all()
        context['rubrics'] = Rubric.objects.all()

        return context


# def by_rubric(request, rubric_id):
#     items = Bb.objects.filter(rubric=rubric_id)
#     rubrics = Rubric.objects.all()
#     current_rubric = Rubric.objects.get(pk=rubric_id)
#     context = {'items': items,
#                'rubrics': rubrics,
#                'current_rubric': current_rubric}
#     return render(request, 'bboard/by_rubric.html', context)


class byRubricView(TemplateView):
    template_name = 'bboard/by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])

        return context


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
