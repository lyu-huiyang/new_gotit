# -*- coding: utf-8 -*-
import werobot
from werobot.client import Client

robot = werobot.WeRoBot(token='hehe')
app_id = 'wx35028b78608d38f9'
app_secret = '107da9b468d3cf7427dc439de6405d01'

client = Client(app_id, app_secret)

client.create_menu({
    "button": [
        {
            "type": "view",
            "name": "Test",
            "url": "www.baidu.com"
        }
    ]})


@robot.handler
def echo(message):
    print robot
    return 'http://www.baidu.com'


robot.run(host='0.0.0.0', port=80)
