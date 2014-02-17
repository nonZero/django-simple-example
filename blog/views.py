from django.shortcuts import render
from blog.models import Post


def list_posts(request):
    return render(request, "blog/post_list.html", {
        'object_list': Post.objects.all(),
    })


def show_post(request, post_id):
    return render(request, "blog/post_detail.html", {
        'object': Post.objects.get(id=int(post_id)),
        'object_list': Post.objects.order_by('?')[:5],
    })
