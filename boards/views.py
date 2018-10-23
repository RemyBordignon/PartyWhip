from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from boards.forms import PostForm, BidForm
from boards.models import Post, Bid


@login_required
def index(request):
    post_list = Post.objects.exclude(end_date__lte=timezone.localtime()).order_by('-pub_date')
    context = {
        'post_list': post_list
    }
    return render(request, 'boards/index.html', context)


@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if post.end_date > timezone.localtime():
        post.status = "OPEN"
    elif post.end_date <= timezone.localtime():
        post.status = "CLOSED"
    if post.winner_selected == True:
        post.status = "ASSIGNED"

    post.save()
    context = {
        'post': post,
        'user': request.user,
    }

    return render(request, 'boards/detail.html', context)

@login_required
def create_post(request):
    if request.method == "POST":
        # use this to add users to DB TABLE TODO
        post = Post(user=request.user, pub_date=timezone.localtime(), winner_selected=False, )
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = PostForm()
    return render(request, "boards/new_post_form.html", {'form': form})


@login_required
def create_bid(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    print(p)
    if request.method == "POST":
        bid = Bid(user=request.user, post=p)
        form = BidForm(instance=bid, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = BidForm()
    return render(request, "boards/new_bid_form.html", {'form': form, 'post_id': post_id})


@login_required
def my_posts(request):
    post_list = Post.objects.filter(user=request.user)

    return render(request, 'boards/my_posts.html', {'post_list': post_list})


@login_required
def my_bids(request):
    bid_list = Bid.objects.filter(user=request.user)
    return render(request, 'boards/my_bids.html', {'bid_list': bid_list})

@login_required
def search(request):
    search_query = request.GET.get('search_box', None)
    search_results = Post.objects.filter(title__contains=search_query)
    context = {
        'post_list': search_results
    }
    return render(request, 'boards/index.html', context)

@login_required
def set_winner_selected(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    p.winner_selected = True
    p.status = "ASSIGNED"
    p.save()
    return redirect('/boards/my_posts', request)


