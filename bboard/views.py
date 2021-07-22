from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Bb
from .models import Rubric
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BbForm
from django.urls import reverse_lazy


class indexView(TemplateView):
    template_name = 'bboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['items'] = Bb.objects.all()
        context['rubrics'] = Rubric.objects.all()

        return context

def index(request):
    rubrics = Rubric.objects.all()
    items = Bb.objects.all()
    paginator = Paginator(items, 3)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'rubrics': rubrics, 'page': page, 'items': page.object_list}
    return render(request, 'bboard/index.html', context)

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
        check_word = int(str(len(context['items']))[0])
        if check_word == 1:
            check_word = 'объявление'
        elif check_word in [2, 3, 4]:
            check_word = 'объявления'
        else:
            check_word = 'объявлений'

        context['posts'] = check_word

        return context


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class PostView(DetailView):
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()

        return context


class BbEditview(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView):
    model = Bb
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Bb.objects.all()
        return context
