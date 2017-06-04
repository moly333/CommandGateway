from django.views.generic import CreateView
from GatewayWeb.forms.Admin.CommandForm import CommandForm
from django.contrib.auth.mixins import UserPassesTestMixin


class CreateCommand(UserPassesTestMixin, CreateView):
    template_name = 'GatewayWeb/Admin/createcommand.html'
    form_class = CommandForm
    success_url = '/scg/admin/editcommands/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser
