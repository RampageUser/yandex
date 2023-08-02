from django.shortcuts import render


def get_main_page(request):
    template = 'index.html'
    return render(request, template)
    
def get_group(request):
    template = 'group_list.html'
    return render(request, template)
