from django.views.generic.edit import CreateView, UpdateView, DeleteView
from GatewayWeb.forms.Admin.CommandForm import CommandForm
from django.contrib.auth.mixins import UserPassesTestMixin
from GatewayWeb.models.Command import Command
from django.views.generic import TemplateView


class CreateCommand(UserPassesTestMixin, CreateView):
    template_name = 'GatewayWeb/Admin/createcommand.html'
    form_class = CommandForm
    success_url = '/scg/admin/editcommands/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser


class DeleteCommand(UserPassesTestMixin, DeleteView):
    model = Command
    template_name = 'GatewayWeb/Admin/deletecommand.html'
    success_url = '/scg/admin/editcommands/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser


class UpdateCommand(UserPassesTestMixin, UpdateView):
    model = Command
    template_name = 'GatewayWeb/Admin/updatecommand.html'
    form_class = CommandForm
    success_url = '/scg/admin/editcommands/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser


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