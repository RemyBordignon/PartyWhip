from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from boards.forms import PostForm
from boards.models import Post


@login_required
def index(request):
    post_list = Post.objects.order_by('-pub_date')[:5]
    context = {
        'post_list': post_list
    }
    return render(request, 'boards/index.html', context)


def detail(request, question_id):
    post = get_object_or_404(Post, pk=question_id)
    return render(request, 'boards/detail.html', {'post': post})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def create_post(request):
    if request.method == "POST":
        # use this to add users to DB TABLE TODO
        # post = Post(from_user=request.user)
        post = Post(pub_date=timezone.localtime(), current_lowest_bid=100)
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = PostForm()
    return render(request, "boards/new_post_form.html", {'form': form})
