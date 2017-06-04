from channels import Group
import json
from GatewayWeb.models.Command import *
from django.core.exceptions import ObjectDoesNotExist
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


def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    global Executing
    data = json.loads(message['text'])
    try:
        Executing = True
        cmd = Command.objects.get(id=data['id'])

        cmddict = {
            'cmdline': '',
            'status': True,
        }

        for line in get_lines(command=cmd.command):
            cmddict['cmdline'] = line.decode('utf-8')
            Group("terminal").send({
                "text": json.dumps(cmddict),
            })

        Executing = False
        cmddict['cmdline'] = '[*] Exec end'
        cmddict['status'] = False

        Group("terminal").send({
            "text": json.dumps(cmddict),
        })

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
    cmddict = {
        'cmdline': '',
        'status': Executing,
    }
    Group("terminal").send({
        "text": json.dumps(cmddict),
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("terminal").discard(message.reply_channel)