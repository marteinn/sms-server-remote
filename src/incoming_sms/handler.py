from __future__ import print_function

import sys
import os
import json
import logging
import re
from cStringIO import StringIO


# Add vendored to sys path
handler_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(handler_path))
sys.path.append(os.path.join(handler_path, "vendored"))


import fabric

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)


def handler(event, context):
    logger.debug("Received event {}".format(json.dumps(event)))

    cmd = event.get('body').lower()
    from_ = event.get('from')

    # if from_ != '':
        # return _response("Error: Invalid phone number")

    sys.stdout = StringIO()

    try:
        from config import fabfile
    except Exception:
        return _response('Error: Missing fabfile')

    tasks = cmd.split(' ')
    for task_name in tasks:
        try:
            task = getattr(fabfile, task_name)
        except Exception as e:
            return _response('Error: {}'.format(e))

        task()

    out = sys.stdout.getvalue()
    out = _format_out(out)

    fabric.network.disconnect_all()

    return _response(out)


def _response(value):
    template = ('<?xml version="1.0" encoding="UTF-8"?>'
                '<Response>'
                '<Message>'
                '<Body><![CDATA[{}]]></Body>'
                '</Message>'
                '</Response>').format(value)

    return template


def _format_out(value):
    lines = value.splitlines()
    formatted = []
    for line in lines:
        line = re.sub("^\[.*?\].(run|out)\:(.*)$", "\\2", line)
        line = line.strip()
        formatted.append(line)

    out = '\n'.join(formatted)
    out = out.strip()
    return out
