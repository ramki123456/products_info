from django.shortcuts import render, render_to_response
from myapp.models import Employe, StockDetails

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

def show_welcome(request):
	return HttpResponse('welcome to my app')

def load_login(request):
	return render(request,'login.html')
	# return HttpResponseRedirect('/welcome')
def get_my_record(request):
	obj=Employe.objects.get(company_name='more')
	return render_to_response('show.html',{'data':obj})

def check_login(request):
	# Use Python Debugger module to simulate/test the code what we have written...(Line by Line)
	import pdb
	# To set the tracing use set_trace() method in PDB.
	pdb.set_trace()
	return HttpResponse("Testing the Data")

def load_add_stock_page(request):
	return render(request, 'add_stock.html')

def add_data_to_db(request):
	#import pdb
	#pdb.set_trace()
	data = request.GET
	# Now get mention the data coming from request.GEt in below query.
	obj = StockDetails(product_name=str(data.get('pro_name')),
					   product_bar_no=str(data.get('pro_bar')),
					   price=float(data.get('pro_price')), 
					   quantity=int(data.get('pro_quantity')))
	obj.save()
	return HttpResponseRedirect('/load_add_stock_page/dd')
