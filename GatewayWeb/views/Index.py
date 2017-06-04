from django.views.generic import TemplateView
from GatewayWeb.models.Command import *
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, TemplateView):

    template_name = 'GatewayWeb/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['commands'] = Command.objects.all()
        return context