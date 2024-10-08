from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def app_data(request):
    return HttpResponse("<h1>This is App1 data</h1>")

def template_data(request):
    name = 'CMRIT'
    return render(request, 'template1.html', {"backend_data": name,"array":['ABC','DEF','GHI']})

def api_data(request):
    data = [
    {
        "Name": "Somu",
        "Payment": {
            "Total": 600
        },
        "Transaction": {
            "price": 400
        }
    },
    {
        "Name": "John",
        "Payment": {
            "Total": 500
        },
        "Transaction": {
            "price": 350
        }
    },
    {
        "Name": "Alice",
        "Payment": {
            "Total": 700
        },
        "Transaction": {
            "price": 250
        }
    },
    {
        "Name": "Somu",
        "Payment": {
            "Total": 300
        },
        "Transaction": {
            "price": 450
        }
    }
    ]
    return render(request,'template2.html',{"data":data})