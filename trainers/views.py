from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from trainers.models import Trainer
from courses.models import Course


# Create your views here.
class TrainerListView(ListView):
    model = Trainer
    template_name = "trainers.html"
    context_object_name = "trainers"
    # queryset = Trainer.objects.all()[:1]

    # def get_queryset(self):
    # return Trainer.objects.all()[:2]

    paginate_by = 3


class TrainerDetailView(DetailView):
    model = Trainer
    template_name = "trainer.html"
    context_object_name = "trainer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.filter(trainer=self.kwargs["pk"])
        return context
