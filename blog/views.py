<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog,BlogCategory,BlogComment,BlogTag
from django.db.models import Count
from .forms import CommentForm, ReplyForm
from django.views.generic import ListView
from django.db.models import Count
from django.views.generic import DetailView
=======
from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog,BlogCategory,BlogComment,BlogTag,Blog_details
>>>>>>> ffa80903c789f0f2e8c562fbbadaa7aa4cd6a0a2

class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"
    template_name = "blog.html"
<<<<<<< HEAD
    paginate_by = 3

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        tag_id = self.kwargs.get('tag_id')
        q = self.request.GET.get("q")
        

        if tag_id:
            return Blog.objects.filter(tags__id=tag_id)
        elif category_id:
            return Blog.objects.filter(category__id=category_id)
        if q:
            return Blog.objects.filter(title__icontains=q)

        return Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.annotate(blog_count=Count('blog'))
        context['tags'] = BlogTag.objects.annotate(blog_count=Count('blogs'))
        context['all_blogs_count'] = Blog.objects.count()

        # Add comments
        context['comments'] = BlogComment.objects.select_related('blog').all()

        # Add the latest 3 blogs
        context['recent_blogs'] = Blog.objects.order_by('-created_date').all()[:3]

        if 'category_id' in self.kwargs:
            context['current_category'] = BlogCategory.objects.get(id=self.kwargs['category_id'])
        if 'tag_id' in self.kwargs:
            context['current_tag'] = BlogTag.objects.get(id=self.kwargs['tag_id'])

        return context







# def blog_detail(request, id):
#     blog = get_object_or_404(Blog, id=id)
#     comments = blog.comments.all()  # 'BlogComment' o'rniga 'comments' ishlatildi

#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.blog = blog
#             comment.user = request.user  # Foydalanuvchi login qilgan bo'lishi kerak
#             comment.save()
#             return redirect('blog_detail', id=blog.id)
#     else:
#         comment_form = CommentForm()

#     context = {
#         'blog': blog,
#         'comments': comments,
#         'comment_form': comment_form
#     }
#     return render(request, 'blog-details.html', context)

# def sidebar_recent_posts(request):
#     recent_posts = Blog.objects.order_by('-created_at')[:3]
#     context = {
#         'recent_posts': recent_posts
#     }
#     return context 

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Blog
from .forms import CommentForm

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-details.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = BlogTag.objects.annotate(blog_count=Count('blogs'))
        context['categories'] = BlogCategory.objects.annotate(blog_count=Count('blog'))
        context['comments'] = self.object.comments.filter(parent__isnull=True).prefetch_related('replies')
        context['comment_form'] = CommentForm()
        context['reply_form'] = ReplyForm()
        context['recent_posts'] = Blog.objects.order_by('-created_date')[:3]
        return context

    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        if 'comment_form' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = blog
                comment.user = request.user
                comment.save()
                return redirect('blog_detail', pk=blog.pk)
        elif 'reply_form' in request.POST:
            form = ReplyForm(request.POST)
            if form.is_valid():
                parent_comment = get_object_or_404(BlogComment, pk=request.POST.get('parent_id'))
                comment = form.save(commit=False)
                comment.blog = blog
                comment.user = request.user
                comment.parent = parent_comment
                comment.save()
                return redirect('blog_detail', pk=blog.pk)
        else:
            form = CommentForm()
            reply_form = ReplyForm()
            context = self.get_context_data()
            context['comment_form'] = form
            context['reply_form'] = reply_form
            return self.render_to_response(context)
=======
    paginate_by = 2 
    
class Blog_detailsListView(ListView):
    model = Blog_details
    context_object_name = 'blog_details'
    template_name = 'blog-details.html'
>>>>>>> ffa80903c789f0f2e8c562fbbadaa7aa4cd6a0a2
