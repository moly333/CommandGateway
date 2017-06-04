from django import forms
from GatewayWeb.models.Command import Command

class CommandForm(forms.ModelForm):

    class Meta:
        model = Command
        fields = ("name", "detail", "command")