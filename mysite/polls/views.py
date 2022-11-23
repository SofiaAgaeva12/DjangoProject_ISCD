from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from .models import Question, Choice, AuthUser
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import SignupForm

from django.shortcuts import render, redirect, get_object_or_404


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'вы не сделали выбор'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class SignupView(generic.CreateView):
    model = AuthUser
    form_class = SignupForm
    template_name = 'polls/signup.html'
    success_url = reverse_lazy('login')
    success_page = "polls"


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = AuthUser


class UpdateUserView(LoginRequiredMixin, generic.UpdateView):
    model = AuthUser
    form_class = SignupForm
    template_name = 'polls/update-user.html'
    success_url = reverse_lazy('user-detail')
    success_page = "polls"

