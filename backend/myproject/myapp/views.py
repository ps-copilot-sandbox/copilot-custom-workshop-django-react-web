from django.http import JsonResponse
from django.core import serializers
from .models import Cat
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cat_list(request):
    cats = Cat.objects.all()
    cat_list = serializers.serialize('json', cats)
    return JsonResponse(cat_list, safe=False)

# Insert Cat into database with user defined custom parameters.
@csrf_exempt
def insert_cat(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        age = request.POST.get('age')
        cat = Cat(name=name, breed=breed, age=age)
        cat.save()
        return JsonResponse({'message': 'Cat created successfully!',}, status=200)