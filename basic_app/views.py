from django.shortcuts import render
from django.http import HttpResponse
from basic_app.models import Bag
from django.views.generic import (ListView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
# Create your views here.

def SearchByDateView(request):
    if request.method=='POST':
        item_date=request.POST['purchase_date']
        result=Bag.objects.filter(purchase_date=item_date)
        context={'bags':result}
        return render(request,'basic_app/bag_list.html',context)


class BagListView(ListView):
    context_object_name='bags'
    model=Bag
    template_name='basic_app/bag_list.html'

class BagCreateView(CreateView):
    model=Bag
    fields=('item_name','item_quantity','item_status','purchase_date')

class BagUpdateView(UpdateView):
    model=Bag
    fields=('item_name','item_quantity','item_status','purchase_date')

class BagDeleteView(DeleteView):
    model=Bag
    success_url=reverse_lazy('list')
