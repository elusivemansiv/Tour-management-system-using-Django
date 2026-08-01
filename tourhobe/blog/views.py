from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BlogPost, NewsletterSubscriber

def blog_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)
            messages.success(request, "Successfully subscribed to the newsletter!")
        return redirect('blog_page')

    featured_post = BlogPost.objects.filter(is_featured=True).order_by('-date_posted').first()
    
    top_posts_query = BlogPost.objects.order_by('-date_posted')
    if featured_post:
        top_posts_query = top_posts_query.exclude(id=featured_post.id)
    
    top_posts = top_posts_query[:3]
    
    latest_articles_query = top_posts_query[3:]
    
    return render(request, 'blog/blog.html', {
        'featured_post': featured_post,
        'top_posts': top_posts,
        'latest_articles': latest_articles_query,
    })

def blog_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})
