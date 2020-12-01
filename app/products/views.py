from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from .forms import ProductModelForm

from .models import Product

# Create your views here.



def search_view(request, *args, **kwargs):
    context = {'name': 'Lukman'}
    return render(request, 'home.html', context)

def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {'object_list': qs}
    return render(request, 'product/list.html', context)

# def product_create_view(request, *args, **kwargs):
#     # print(request.GET)
#     # print(request.POST)

#     if request.method == 'POST':
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             print(my_form.is_valid())
#             if my_form.is_valid():
#                 # print(my_form.cleaned_data.get('title'))
#                 title_from_input = my_form.cleaned_data.get('title')
#                 Product.objects.create(title=title_from_input)
#                 # print('post data', post_data)
#     return render(request, 'form.html', {})
@login_required
def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # do some stuff
        obj.save()
        # print(request.POST)
        # print(form.cleaned_data)
        # data = form.cleaned_data
        # Product.objects.create(**data)
        form = ProductModelForm()
    return render(request, 'form.html', {'form': form})


def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return HttpResponse(f'Product {pk} Not Found')

    return render(request, 'product/detail.html', {'object': obj})
