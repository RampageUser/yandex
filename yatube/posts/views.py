from django.shortcuts import render


def get_main_page(request):
    template = 'index.html'
    return render(request, template)
    
