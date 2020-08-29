from django.shortcuts import render,reverse
from .models import Food,Consume
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):

    if request.method == 'POST':
        food_name = request.POST.get('food')
        food = Food.objects.get(name=food_name)
        consume = Consume(food_consumed=food,user=request.user)
        consume.save()
        foods = Food.objects.all()
        consumed_food = Consume.objects.filter(user=request.user).order_by('-id')
        count = consumed_food.count()
    
    else:
        foods = Food.objects.all()
        consumed_food = Consume.objects.filter(user=request.user).order_by('-id')
        count = consumed_food.count()

    return render(request,'index.html',{'foods':foods,'consumed':consumed_food,'count':count})

def delete_food(request,id):
    consume = Consume.objects.get(id=id)
    if request.method == 'POST':
        consume.delete()
        return HttpResponseRedirect('/')
    return render(request,'delete.html',{'consume':consume})

def delete_all(request):
    if request.method == 'POST':
        Consume.objects.filter(user=request.user).delete()
        return HttpResponseRedirect('/')
    return render(request,'delete_all.html')