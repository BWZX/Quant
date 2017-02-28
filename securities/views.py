from django.shortcuts import render


def index(request):    
    # template = loader.get_template('index.html')
    context = {
        'latest_question_list': 'oooooo',
    }
    return render(request,'index.html',context)