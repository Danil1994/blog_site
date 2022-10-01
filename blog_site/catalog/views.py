from django.shortcuts import render


from .models import Author, Post, Comment


def index(request):
    # Генерация главных объектов
    num_posts=Post.objects.all().count()
    num_comments=Comment.objects.count()
    num_authors=Author.objects.count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_posts':num_posts, 'num_comments':num_comments, 'num_authors':num_authors},
    )

from django.views import generic

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

class PostDetailView(generic.DetailView):
    model = Post

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


class CommentCreate(CreateView):

    model = Comment
    fields = ['comment_text', ]

    def get_context_data(self, **kwargs):

        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):

        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):

        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'], })









