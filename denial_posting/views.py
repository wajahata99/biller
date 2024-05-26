from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def upload(request):
    return render(request, 'upload.html')

def review(request):
    return render(request, 'review.html')