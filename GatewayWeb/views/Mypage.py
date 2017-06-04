from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Mypage(LoginRequiredMixin, TemplateView):

    template_name = 'GatewayWeb/mypage.html'

    def get_context_data(self, **kwargs):
        context = super(Mypage, self).get_context_data(**kwargs)
        return context