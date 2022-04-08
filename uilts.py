import json

import requests


def send_email_to_gmail():
    pass


def check_message_status(status_code):
    if status_code == 200:
        print("消息发送成功")
    else:
        send_email_to_gmail()


def tt_message(tt_url, message):
    data = {
        "msgtype": "text",
        "text": {
            "content": "运维报警系统:{message}".format(message=message),
        },
        "at": {
            "isAtAll": True
        }
    }
    headers = {'Content-Type': 'application/json'}
    result = requests.post(url=tt_url, data=json.dumps(data), headers=headers)
    check_message_status(result.status_code)


if __name__ == '__main__':
    tt_url = "https://oapi.dingtalk.com/robot/send?access_token" \
             "=4083a42eabd14db185139576142fbff86dcb122a7c4299c3f04f19fd5a005fc3 "
    tt_message(message="lidejin", tt_url=tt_url)
