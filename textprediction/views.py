from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from predictionModules import text_prediction
# Create your views here.
@login_required(login_url='/signin')
def text(request):
    if request.method == 'POST':
        f = request.POST['text']
        
        text_result = text_prediction.predict(f)
        print(text_result)
    
        return render(request,'text.html', {'text_result' : text_result})

    else:
        return render(request,'text.html')