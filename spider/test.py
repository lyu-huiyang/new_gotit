# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

test_message = """
        <xml>
        <ToUserName><![CDATA[gh_113ae65cd7ed]]></ToUserName>
        <FromUserName><![CDATA[odabgv1gl5U-ZcEmRIJB3vFrw41M]]></FromUserName>
        <CreateTime>1458699029</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[。]]></Content>
        <MsgId>6265064624663882806</MsgId>
        </xml>
        """
root = ET.fromstring(test_message)
to_user_name = root.findall('ToUserName')[0].text
from_user_name = root.findall('FromUserName')[0].text
create_time = root.findall('CreateTime')[0].text
message_type = root.findall('MsgType')[0].text
content = root.findall('Content')[0].text
message_id = root.findall('MsgId')[0].text
return_message = """<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[%s]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>""" % (to_user_name, from_user_name,create_time,message_type,content)

print return_message
