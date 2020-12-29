from django.shortcuts import render, redirect
from predictionModules import image_prediction
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/signin')
def image(request):
    if request.method == 'POST':
        f = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(f.name, f)
        path_url = fs.url(filename)
        path = '.{}'.format(path_url)
        print(path)
        
        image_result = image_prediction.predict(path)
        print(image_result)
       
       
    
        return render(request,'image.html',{'image':path_url,'image_result':image_result})
    
    else:
        return render(request,'image.html')
