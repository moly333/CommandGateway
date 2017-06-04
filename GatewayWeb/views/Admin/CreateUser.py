from django.views.generic import CreateView
from GatewayWeb.forms.Admin.UserForm import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin


class CreateUser(UserPassesTestMixin, CreateView):
    template_name = 'GatewayWeb/Admin/createuser.html'
    form_class = UserCreationForm
    success_url = '/scg/admin/editusers/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser
