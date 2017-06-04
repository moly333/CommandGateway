from django.views.generic import TemplateView
from GatewayWeb.models.Command import Command
from django.contrib.auth.mixins import UserPassesTestMixin


class EditCommand(UserPassesTestMixin, TemplateView):

    template_name = 'GatewayWeb/Admin/editcommands.html'
    permission_required = 'GatewayWeb.views.Admin.EditCommands'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(EditCommand, self).get_context_data(**kwargs)
        context['commands'] = Command.objects.all()
        return context

    def test_func(self):
        return self.request.user.is_superuser

