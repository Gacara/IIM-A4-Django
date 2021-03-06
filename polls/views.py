from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Choice, Question, Contact

class ContactCreate(generic.CreateView):
    template_name = 'polls/contact_forms.html'
    model = Contact
    fields = ["first_name", "last_name", "message", "cv_Img"]
    success_url = reverse_lazy('polls:index')

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_cv_list'

    def get_queryset(self):
        """Return the last 50 published CV."""
        contains = self.request.GET.get('contains')
        if contains is None:
            return Contact.objects.order_by('-pub_date')
        return Contact.objects.order_by('-pub_date').filter(message__contains=contains)[:50]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['skills_contains'] = Contact.objects.all().filter(message__contains="")
        return context

class PollsView(generic.ListView):
    template_name = 'polls/polls.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class CvView(generic.DetailView):
    model = Contact
    template_name = 'polls/cv.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
