from django.shortcuts import render
from django.http import HttpResponse
from api.model.neural_net import predict
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from django.core.files.base import ContentFile

@csrf_exempt
def home(request):
    result = {}
    if request.method == 'POST':
        result = {}
        """
        # img = ContentFile(request.FILES.get('myFile').read())
        if img == '':
            result = {'error':'Image not provided'} 
        else:
            im = Image.open(img)
            im = im.convert('RGB')
            result = predict(im)
        # print(result)
        # return render(request, 'api/index.html', {'result': int(result), 'stat': True})
    # return render(request, 'api/index.html', {'stat': False})
        """
        img_url = request.POST.get('url_input')
        if img_url == '':
            result = {'error':'Image not provided'}
        else:
            im = Image.open(requests.get(url_input, stream=True).raw)
            im = im.convert('RGB')
            result = predict(im)
     print(result)
     return HttpResponse(str(result),content_type='text/json')


