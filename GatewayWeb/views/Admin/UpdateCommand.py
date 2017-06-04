from django.views.generic import UpdateView
from GatewayWeb.forms.Admin.CommandForm import CommandForm
from GatewayWeb.models.Command import Command
from django.contrib.auth.mixins import UserPassesTestMixin


class UpdateCommand(UserPassesTestMixin, UpdateView):
    model = Command
    template_name = 'GatewayWeb/Admin/updatecommand.html'
    form_class = CommandForm
    success_url = '/scg/admin/editcommands/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser
