from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.tort.models import Tort


class TortListView(ListView):
    model = Tort
    template_name = 'torts.html'
    context_object_name = 'tort'
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        tort_list = Tort.objects.all()

        paginator = Paginator(tort_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            tort_product = paginator.page(page)
        except PageNotAnInteger:
            tort_product = paginator.page(1)
        except EmptyPage:
            tort_product = paginator.page(paginator.num_pages)

        context['tort_product'] = tort_product
        return context


class TortDetailView(DetailView):
    model = Tort
    template_name = 'tort_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'tort_detail'

    def get_queryset(self):
        return Tort.objects.all()
