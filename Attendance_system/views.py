from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os



def runApp(request):
    
    path=r"C:\Users\abina\PycharmProjects\face\main.py"
    
    if not os.path.exists(path):
        return HttpResponse(f"Error: File not found at {path}")
    try:
        subprocess.Popen(['python',path])
    except Exception as e:
        return HttpResponse(f"Error:{e}")
    
    return render (request,'myapp/home.html')

    
    