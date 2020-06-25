from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StorageForm, ItemSearchForm
from .models import Storage
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import csv
from django.contrib import messages

def index(request):
	title = 'Inventory Admin'
	context = {
		'title' : title,
	}
	return render(request, 'invapp/index.html', context)

def item_entry(request):
	title = 'Add Items'
	form = StorageForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/item_list')
	context = {
			'title' : title,
			'form' : form
	}
	return render(request, 'invapp/item_entry.html', context)

def item_list(request):
	title = 'The list of all items '
	queryset = Storage.objects.all()
	form = ItemSearchForm(request.POST or None)
	context = {
		'title' : title,
		'queryset' : queryset,
		'form' : form,
	}
	
	if request.method == 'POST':
		queryset = Storage.objects.all().order_by('-timestamp').filter(item__icontains=form['item'].value(), location__icontains=form['location'].value())
		context = {
			'title' : title,
			'queryset' : queryset,
			'form' : form,
		}

		if form['export_to_CSV'].value() == True: 
			response = HttpResponse(content_type='text/csv') 
			response['Content-Disposition'] = 'attachment; filename="Item list.csv"' 
			writer = csv.writer(response) 
			writer.writerow(['item name', 'amount', 'expected_need_in', 'issue_date', 'location']) 
			instance = queryset 
			for row in instance: 
				writer.writerow([row.item, row.amount, row.expected_need_in, row.choices_field.all(), row.issue_date, row.location, row.timestamp]) 
			return response

	return render(request, 'invapp/item_list.html', context)

 
def list_edit(request, id=None):
	instance = get_object_or_404(Storage, id=id)
	form = StorageForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/item_list')
	context = {
		'title' : 'Edit ' + str(instance.item),
		'instance' : instance,
		'form' : form,
	}
	return render(request, 'invapp/item_entry.html', context)

def item_delete(request, id=None):
	instance = get_object_or_404(Storage, id=id)
	instance.delete()
	return redirect('/item_list')

def storagehistory_list(request):
    title = 'Update history'
    queryset = StorageHistory.objects.all()
    context = {
       'title' : title,
       'queryset' : queryset,
    }
    return render(request, 'invapp/item_list.html', context)