from django.shortcuts import render
from .models import Poll,option
from django.views.generic import ListView, DetailView,RedirectView
# Create your views here.
def poll_list(req):
    polls=Poll.objects.all()
    return render(req,'default/list.html',{'poll_list':polls,'msg':'Hello!'})


class PollList(ListView):
    model=Poll

    #


class PollView(DetailView):
    model=Poll

    def get_context_data(self, **kwargs):

        ctx= super().get_context_data(**kwargs)
        option_list=option.objects.filter(poll_id=self.object.id)

class pollVote(RedirectView):
    pass  
