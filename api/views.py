from django.shortcuts import render
from django.http import HttpResponse
from api.model.neural_net import predict
from django.views.decorators.csrf import csrf_exempt
from PIL import Image

# Create your views here.

@csrf_exempt
def home(request):
    result = {}
    if request.method == 'POST':
        img = request.FILES.get('img_field')
        if img == '':
            result = {'error':'Image not provided'} 
        else:
            im = Image.open(img)
            im = im.convert('RGB')
            result = predict(im)
    print(result)
    return HttpResponse(str(result),content_type='text/json')
	
