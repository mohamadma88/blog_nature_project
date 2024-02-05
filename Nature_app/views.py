from django.shortcuts import render
from .models import Nature
from detail_post_app.models import Detail , Category


def nature(request):
    naturee = Nature.objects.all()
    detail = Detail.objects.all()
    category = Category.objects.all()
    return render(request, 'Nature_app/nature.html',context={'nature': naturee , 'detail':detail,'category': category})