from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from drugs.forms import AddForm

# Create your views here.

class AddView(LoginRequiredMixin,CreateView):
    template_name='drugs/add.html'
    form_class=AddForm
    
    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        #context['profile'] = self.request.user.profile
        #context['count_gelcaps_of_box']=context['num_gelcaps']
        return context