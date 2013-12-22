# Create your views here.

from django.views.generic import CreateView
from braces.views import LoginRequiredMixin

from .models import Import

class CreateImport(LoginRequiredMixin, CreateView):

    form_class = CreateForm
    model = Import
    context_object_name = 'import'

    def form_valid(self, form):
        # form.instance.submitted_by = self.request.user
        return super(CreateImport, self).form_valid(form)