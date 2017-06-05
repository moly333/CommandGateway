from django.views.generic.edit import CreateView, UpdateView, DeleteView
from GatewayWeb.forms.Admin.UserForm import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from GatewayWeb.forms.Admin.UserForm import UserForm


class CreateUser(UserPassesTestMixin, CreateView):
    template_name = 'GatewayWeb/Admin/createuser.html'
    form_class = UserCreationForm
    success_url = '/scg/admin/editusers/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser


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


class UpdateUser(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'GatewayWeb/Admin/updateuser.html'
    form_class = UserForm
    success_url = '/scg/admin/editusers/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser


class DeleteUser(UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'GatewayWeb/Admin/deleteuser.html'
    success_url = '/scg/admin/editusers/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser
