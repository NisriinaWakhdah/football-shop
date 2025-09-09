from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
            'npm': '2406360445',
            'name': 'Nisriina Wakhdah Haris',
            'class': 'PBP B',
            'appName': 'main'
    }
    return render(request, "main.html", context)
