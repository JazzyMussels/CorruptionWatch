from django.shortcuts import render

def display_list(request):
    return render(request, 'selection/list.html')
