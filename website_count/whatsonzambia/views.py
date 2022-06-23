from itertools import count
from django.shortcuts import render
from .models import Post, Client
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):

    post = Post.objects.all()
    paginator = Paginator(post, 4)
    page = request.GET.get('page')
    print(page)

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = Client(client=ip)
    print(ip)
    result = Client.objects.filter(Q(client__icontains=ip))
    if len(result) == 1:
        print("client exit")
    elif len(result) > 1:
        print("user exist more...")
    else:
        u.save()
        print("user is unique")
    count = Client.objects.all().count()
    print("total user is", count)


    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'count': count,
        'posts': Post.objects.all()
    }
    return render(request, 'whatsonzambia/home.html', context)



def about(request):
    return render(request, 'whatsonzambia/home.html')
