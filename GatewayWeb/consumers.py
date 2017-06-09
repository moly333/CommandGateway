from channels import Group
import json
from GatewayWeb.models.Command import *
from django.core.exceptions import ObjectDoesNotExist
import django.utils.html as dhtml
import subprocess

Executing = False

def get_lines(command):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line

        if not line and proc.poll() is not None:
            break

def send_cmd(cmdline, status):
    cmddict = {
        'cmdline': cmdline,
        'status': status,
    }
    Group("terminal").send({
        "text": json.dumps(cmddict),
    })


def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    global Executing
    data = json.loads(message['text'])
    try:
        Executing = True
        cmd = Command.objects.get(id=data['id'])
        send_cmd(dhtml.escape('[*]' + cmd.name + ' start'), True)

        for line in get_lines(command=cmd.command):
            send_cmd(dhtml.escape(line.decode('utf-8')), True)

        Executing = False
        send_cmd(dhtml.escape('[*] Exec end'), False)

    except ObjectDoesNotExist:
        Executing = False
        cmd = None


# Connected to websocket.connect
def ws_add(message):
    global Executing
    # Accept the incoming connection
    message.reply_channel.send({"accept": True})
    # Add them to the chat group
    Group("terminal").add(message.reply_channel)
    send_cmd(dhtml.escape(''), Executing)

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("terminal").discard(message.reply_channel)