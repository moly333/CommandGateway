from django.views.generic import UpdateView
from GatewayWeb.forms.Admin.UserForm import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin


class UpdateUser(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'GatewayWeb/Admin/updateuser.html'
    form_class = UserForm
    success_url = '/scg/admin/editusers/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser
