import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

# Create your views here.
from boards.forms import PostForm, BidForm, OptionsForm
from boards.models import Post, Bid
from boards.sort import Sort


@login_required
def index(request):
    options_form = OptionsForm(data=request.POST)

    if not options_form.is_valid():
        options_form = OptionsForm()
        post_list = Post.objects.exclude(end_date__lte=timezone.localtime()).order_by('-pub_date')
    else:
        sort_by = request.GET.get('sort_option')
        min_value = request.GET.get('min_value')
        max_value = request.GET.get('max_value')

        if sort_by is not None and (min_value is not None or max_value is not None):
            options_form.add_error('sort_option', "Select one sorting mechanism")

        if min_value is not None and max_value is not None:
            if min_value is not "" and max_value is not "" and min_value > max_value:
                options_form.add_error('max_value', "Enter Valid Budget Range")

        if sort_by is not None:
            sort = Sort()
            post_list = list(Post.objects.exclude(end_date__lte=timezone.localtime()))
            # DAFNY SORTS HERE
            if sort_by == 'most_recent':
                post_list = Post.objects.exclude(end_date__lte=timezone.localtime()).order_by('-pub_date')
            elif sort_by == 'budget_ascending':
                sort.cocktail_budget_ascending(post_list)
            elif sort_by == 'budget_descending':
                sort.bubble_budget_descending(post_list)
            elif sort_by == 'event_date_ascending':
                sort.selection_event_date_ascending(post_list)
            elif sort_by == 'event_date_descending':
                sort.insertion_event_date_descending(post_list)
            elif sort_by == 'this_week':
                today = datetime.datetime.now()
                week = datetime.timedelta(days=7)
                post_list = Post.objects.filter(event_date__lt=(today + week),
                                                    event_date__gte=datetime.datetime.now())
            elif sort_by == 'this_month':
                today = datetime.datetime.now()
                month = datetime.timedelta(days=30)
                post_list = Post.objects.filter(event_date__lt=(today + month),
                                                    event_date__gte=datetime.datetime.now())
            else:
                post_list = Post.objects.exclude(end_date__lte=timezone.localtime()).order_by('-pub_date')
        elif min_value is not None and min_value is not "" and max_value is not None and max_value is not "" and min_value < max_value:
            post_list = Post.objects.exclude(end_date__lte=timezone.localtime()).filter(budget__gte=min_value,
                                            budget__lte=max_value)
        elif min_value is not None and min_value is not "" and (max_value is None or max_value is ""):
            post_list = Post.objects.exclude(end_date__lte=timezone.localtime()).filter(budget__gte=min_value)
        elif max_value is not None and max_value is not "" and (min_value is None or min_value is ""):
            post_list = Post.objects.exclude(end_date__lte=timezone.localtime()).filter(budget__lte=max_value)
        else:
            post_list = Post.objects.exclude(end_date__lte=timezone.localtime()).order_by('-pub_date')

    context = {
        'post_list': post_list,
        'form': options_form
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
        'user': request.user
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
    if request.method == "POST":
        bid = Bid(user=request.user, post=p)
        form = BidForm(instance=bid, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:detail', post_id)
    else:
        form = BidForm()
    return render(request, "boards/new_bid_form.html", {'form': form, 'post_id': post_id})


@login_required
def my_posts(request):
    post_list = Post.objects.filter(user=request.user).order_by('-pub_date')

    return render(request, 'boards/my_posts.html', {'post_list': post_list})


@login_required
def my_bids(request):
    bid_list = Bid.objects.filter(user=request.user).order_by('-post__pub_date')
    return render(request, 'boards/my_bids.html', {'bid_list': bid_list})

@login_required
def search(request):
    search_query = request.GET.get('search_box', None)
    search_results = Post.objects.filter(Q(title__contains=search_query)|Q(location__contains=search_query))
    context = {
        'post_list': search_results,
        'search_term': search_query,
    }
    return render(request, 'boards/search.html', context)

@login_required
def set_winner_selected(request, bid_id):
    # print(bid_id)
    # for bid in Bid.objects.all():
    #     print(bid.id)
    b = get_object_or_404(Bid, pk=bid_id)
    b.post.winner_selected = True
    b.post.status = "ASSIGNED"
    b.post.winning_bid = b.id
    b.post.save()
    b.save()
    context = {
        'post': b.post,
        'bidder': b.id
    }
    return render(request, 'boards/winner_selected.html', context)

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()

    post_list = Post.objects.filter(user=request.user).order_by('-pub_date')
    return render(request, 'boards/my_posts.html', {'post_list': post_list})

@login_required
def delete_bid(request, bid_id):
    bid = Bid.objects.get(pk=bid_id)
    bid.delete()

    bid_list = Bid.objects.filter(user=request.user).order_by('-post__pub_date')
    return render(request, 'boards/my_bids.html', {'bid_list': bid_list})



