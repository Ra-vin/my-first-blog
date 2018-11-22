from django.shortcuts import render

def post_list(request):
    return render(request, 'page/post_list.html')
