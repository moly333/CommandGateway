from django.conf.urls import url
from GatewayWeb.views.Index import Index
from GatewayWeb.views.Mypage import Mypage
from GatewayWeb.views.Admin.UpdateCommand import UpdateCommand
from GatewayWeb.views.Admin.CreateCommand import CreateCommand
from GatewayWeb.views.Admin.EditCommands import EditCommand
from GatewayWeb.views.Admin.EditUsers import EditUsers
from GatewayWeb.views.Admin.CreateUser import CreateUser
from GatewayWeb.views.Admin.UpdateUser import UpdateUser
from django.contrib.auth.views import login, logout, password_change
from GatewayWeb.forms.accounts.forms import LoginForm

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^mypage/', Mypage.as_view(), name='mypage'),
    url(r'^admin/createcommand/', CreateCommand.as_view(), name='createcommand'),
    url(r'^admin/editcommands/', EditCommand.as_view(), name='editcommands'),
    url(r'^admin/updatecommand/(?P<pk>\d+)$', UpdateCommand.as_view(), name='updatecommand'),
    url(r'^admin/editusers/', EditUsers.as_view(), name='editusers'),
    url(r'^admin/createuser/', CreateUser.as_view(), name='createuser'),
    url(r'^admin/updateuser/(?P<pk>\d+)$', UpdateUser.as_view(), name='updateuser'),
    url(r'^login/$', login,
        {'template_name': 'GatewayWeb/accounts/login.html', 'authentication_form': LoginForm, 'redirect_authenticated_user': True}, name='login'),
    url(r'^logout/$', logout,
        {'template_name': 'GatewayWeb/accounts/logout.html'}, name='logout'),
    url(r'^changepasswd/$', password_change,
        {'template_name': 'GatewayWeb/accounts/changepasswd.html', 'post_change_redirect': '/scg/mypage/'}, name='changepasswd'),
]
