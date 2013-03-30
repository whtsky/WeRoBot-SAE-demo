import os
import sys

root = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(root, 'site-packages'))

import werobot

robot = werobot.WeRoBot(token='tokenhere')


@robot.handler
def echo(message):
    return 'Hello World!'
