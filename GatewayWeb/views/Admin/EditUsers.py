from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User


class EditUsers(UserPassesTestMixin, TemplateView):

    template_name = 'GatewayWeb/Admin/editusers.html'
    permission_required = 'GatewayWeb.views.Admin.EditUsers'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(EditUsers, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

    def test_func(self):
        return self.request.user.is_superuser
