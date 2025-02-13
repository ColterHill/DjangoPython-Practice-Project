from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from users.models import Profile

# Create your views here.

class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html'
    context_object_name = 'item_list'



def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request, 'food/detail.html', context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

#This is a class based view for creating an item
class CreateItem(CreateView):
    model = Item
    fields =['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        form.instance.last_modified_by = self.request.user
        return super().form_valid(form)


#class based update item
class UpdateItem(UpdateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.last_modified_by = self.request.user
        return super().form_valid(form)


def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item':item})
    

def profile_view(request):
    profile_list = Profile.objects.all()
    context = {'profile_list': profile_list}
    return render(request, 'base.html', context)