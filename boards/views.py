from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from boards.forms import PostForm, BidForm
from boards.models import Post, Bid


@login_required
def index(request):
    post_list = Post.objects.order_by('-pub_date')[:5]
    context = {
        'post_list': post_list
    }
    return render(request, 'boards/index.html', context)


@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if post.end_date > timezone.localtime():
        status = "OPEN"
    elif post.end_date <= timezone.localtime():
        status = "CLOSED"
    elif post.winner_selected:
        status = "ASSIGNED"

    context = {
        'post': post,
        'status': status
    }

    return render(request, 'boards/detail.html', context)


@login_required
def create_post(request):
    if request.method == "POST":
        # use this to add users to DB TABLE TODO
        post = Post(pub_date=timezone.localtime(), winner_selected=False)
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = PostForm()
    return render(request, "boards/new_post_form.html", {'form': form})


@login_required
def create_bid(request):
    if request.method == "POST":
        form = BidForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = BidForm()
    return render(request, "boards/new_bid_form.html", {'form': form})

@login_required
def my_posts(request):
    post_list = Post.objects.filter(user=request.user)
    return render(request, 'boards/my_posts.html', {'post_list': post_list})

@login_required
def my_bids(request):
    post_list = Bid.objects.filter(user=request.user)
    return render(request, 'boards/my_bids.html', {'post_list': post_list})

