from django.shortcuts import render
from .models import Poll,Option
from django.views.generic import ListView, DetailView,RedirectView
from django.urls import reverse

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
        ctx['option_list']=Option.objects.filter(poll_id=self.object.id)
        return ctx

class PollVote(RedirectView):
    def get_redirect_url(self, request, *args, **kwargs):
        option=Option.objects.get(id=self.kwargs['oid'])
        option.votes+=1
        option.save()
        #return super().get_redirect_url(**args,**kwargs)
        return reverse('poll_view',args=[option.poll_id])
