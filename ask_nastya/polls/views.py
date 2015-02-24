from django.shortcuts import render

# Create your views here.

def index(request):
    greeting = 'Hello,world'
    get_params = request.GET.items()
    #print get_params
    post_params = request.POST.items()
    return render(request, 'polls/index.html', {'greeting': greeting,
                                                'get_params':get_params,
                                                'post_params':post_params})
