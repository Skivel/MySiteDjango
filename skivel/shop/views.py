from django.shortcuts import render
from django.views.generic import DetailView
from .models import CPU, Smartphone


def shop_home(request):
    return render(request, 'shop/index.html')


class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'cpu': CPU,
        'smartphone': Smartphone
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'products'
    template_name = 'shop/product_detail.html'
    slug_url_kwarg = 'slug'
