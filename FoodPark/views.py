#user created file

from django.http import HttpResponse
from django.shortcuts import render
import pyshorteners
def index1(request):

	return render(request,'index.html')
def shortner(request):
	default="https://www.flipkart.com"#/asus-studiobook-pro-core-i9-12th-gen-32-gb-1-tb-ssd-windows-11-home-8-gb-graphics-nvidia-geforce-rtx-3070-h7600zw-l911ws-creator-laptop/p/itm912780a5490cb?pid=COMGGBGRMHRYZYXK&lid=LSTCOMGGBGRMHRYZYXKN7M3RT&marketplace=FLIPKART&store=b5g&srno=b_1_11&otracker=CLP_Filters&fm=search-autosuggest&iid=76a7c31d-456d-4e95-843b-b06ad837c1ae.COMGGBGRMHRYZYXK.SEARCH&ppt=sp&ppn=sp&ssid=wvqm3o9y4g0000001668061802474"
	
	ip_url=request.GET.get('input_url',default)
	print(ip_url)
	obj=pyshorteners.Shortener()
	small_url=obj.tinyurl.short(ip_url)
	return HttpResponse(small_url)