# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm, CommentFormTwo
from django.contrib.auth.decorators import login_required

def home(request):
    user_count = User.objects.filter(is_active=True).count()
    question_count = Question.objects.all().count()
    return render(request, 'home.html', {'user_count': user_count, 'question_count': question_count})

class QuestionListView(ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'
    ordering = ['-date_created']
    paginate_by = 7  # Number of questions per page

    def get_queryset(self):
        # Get the search input from the request
        search_input = self.request.GET.get('search-area', '')
        
        # Get all questions
        queryset = Question.objects.all()
        
        # Filter questions if search input is present
        if search_input:
            queryset = queryset.filter(title__icontains=search_input)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Include search input in the context for form persistence
        context['search_input'] = self.request.GET.get('search-area', '')
        
        return context
    
    
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'content']
    template_name = 'question_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        print(f"Created Question PK: {self.object.pk}")
        return response

    def get_success_url(self):
        return reverse_lazy('stackbase:questionDetail', kwargs={'pk': self.object.pk})

class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['title', 'content']
    template_name = 'question_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        print(f"Updated Question PK: {self.object.pk}")
        return response

    def get_success_url(self):
        return reverse_lazy('stackbase:questionDetail', kwargs={'pk': self.object.pk})

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.user
    
class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    template_name = 'question_confirm_delete.html'
    success_url = reverse_lazy('stackbase:questionList')  # Redirect to questions page after successful deletion

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.user  # Only allow the user who created the question to delete it

#Comments

class CommentDetailView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'question_form.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form) 
    success_url = reverse_lazy('stackbase:questionDetail')
    
# class AddCommentView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'answer_form.html'

#     def form_valid(self, form):
#         form.instance.question_id = self.kwargs['pk']
#         return super().form_valid(form) 

@login_required
def AddCommentView(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = CommentFormTwo(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = question
            comment.name = request.user.username
            comment.save()
            return redirect('stackbase:questionDetail', pk=question.pk)
    else:
        form = CommentFormTwo()
    return render(request, 'add_comment.html', {'question': question, 'form': form})