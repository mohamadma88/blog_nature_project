from django.shortcuts import render
from detail_post_app.models import Detail , Main , Category


def home(request):
    detail = Detail.objects.all()
    main = Main.objects.all()
    recently_post = Detail.objects.all().order_by('-created')
    category = Category.objects.all()

    return render(request,'home_app/index.html', context={'detail': detail, 'main':main , 'recently_post':recently_post , 'category':category})