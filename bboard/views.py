from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME
from django.shortcuts import render, redirect, get_object_or_404
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
    length = len(items)
    paginator = Paginator(items, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'rubrics': rubrics,
               'page': page,
               'items': page.object_list,
               'length': '{} {}'.format(length, check_word(length))}
    return render(request, 'bboard/index.html', context)


# def by_rubric(request, rubric_id):
#     items = Bb.objects.filter(rubric=rubric_id)
#     rubrics = Rubric.objects.all()
#     current_rubric = Rubric.objects.get(pk=rubric_id)
#     context = {'items': items,
#                'rubrics': rubrics,
#                'current_rubric': current_rubric}
#     return render(request, 'bboard/by_rubric.html', context)

def check_word(number):
    if number == 1:
        number = 'объявление'
    elif number in [2, 3, 4]:
        number = 'объявления'
    else:
        number = 'объявлений'
    return number


class byRubricView(TemplateView):
    template_name = 'bboard/by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
        context['posts'] = check_word(len(context['items']))

        return context


def rubrics(request):
    RubricFormSet = modelformset_factory(Rubric, fields=('name',),
                                         can_order=True, can_delete=True)
    if request.method == 'POST':
        formset = RubricFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    rubric = form.save(commit=False)
                    rubric.order = form.cleaned_data[ORDERING_FIELD_NAME]
                    rubric.save()
            return redirect('home')
    else:
        formset = RubricFormSet()
    context = {'formset': formset}
    return render(request, 'bboard/rubrics.html', context)


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


def detail(request, slug=None):
    post = get_object_or_404(Bb, slug=slug)
    return render(request, 'bboard/bb_detail.html', {'bb': post})


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


def delete_post(request, pk_id):
    post = get_object_or_404(Bb, pk=pk_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'bboard/bb_confirm_delete.html', {'bb': post})


def cancel(request):
    return redirect('home')


def search_posts(request):
    keyword = request.POST['keyword']
    if request.method == 'POST':
        q = Q(title__contains=keyword)
        items = Bb.objects.filter(q)
        length = len(items)
        return render(request, 'bboard/search.html',
                      {'items': items,
                       'keyword': keyword,
                       'length': '{} {}'.format(length, check_word(length))})
    return render(request, 'bboard/search.html', {})
