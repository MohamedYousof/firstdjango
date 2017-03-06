from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from inventory.models import Item
from .forms import ItemForm


def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'inventory/index.html', {
        'items': items,
    })


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("inventory/index.html")
    context = {'form': form}
    return render(request, 'inventory/item_form.html', context)


def item_details(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        raise Http404('Item is not found')
    return render(request, 'inventory/item_details.html', {
        'item': item,
    })
