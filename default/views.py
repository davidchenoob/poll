from django.shortcuts import render
from .models import Poll,Option
from django.views.generic import ListView, DetailView,RedirectView,CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
class PollCreate(LoginRequiredMixin, CreateView):
    model=Poll
    fields='__all__'#['subject', 'desc']
    success_url=reverse_lazy('poll_list')
class PollEdit(UpdateView):
    model=Poll
    fields='__all__'#['subject', 'desc']

    #稱恭候要去的路徑不˙固定，則需要定義get_success_url()方法來回應
    def get_success_url(self):
        return reverse_lazy('poll_view',kwargs={'pk':self.object.id})
    
class OptionCreate(CreateView):
    model=Option
    fields=['title']
    def form_invalid(self, form):
        form.instance.poll_id=self.kwargs['pid']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('poll_view',kwargs={'pk':self.kwargs['pid']})
    
class OptionEdit(UpdateView):
    model=Option
    fields=['title']
    pk_url_kwarg='oid'
    def get_success_url(self):
        return reverse_lazy('poll_view',kwargs={'pk':self._object.poll_id})
    
class PollDelete(DeleteView):
    model=Poll
    success_url=reverse_lazy('poll_list')
class OptionDelete(DeleteView):
    model=Option
    def get_success_url(self):
        return reverse_lazy('poll_view',kwargs={'pk':self._object.poll_id})