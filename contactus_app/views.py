from django.shortcuts import render ,redirect
from .models import Contactus , Text , About
from detail_post_app.models import Detail, Category


def contactus(request):
    head = Text.objects.all()
    about = About.objects.all()
    detail = Detail.objects.all()
    category = Category.objects.all()
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    text = request.POST.get('text')

    if request.method == 'POST':
        Contactus.objects.create(name=name,email=email,subject=subject,text=text)
        return redirect('contact_us:contact')
    return render(request,'contactus_app/contact.html', context={'head': head,'detail': detail, 'category': category , 'about':about})
