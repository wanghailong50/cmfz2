import requests

class Message(object):
    def __init__(self,api_key):
        self.api_key=api_key
        self.url= "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_message(self,mobile,code):
        param={
            "apikey":self.api_key,
            "mobile":mobile,
            "text":"【毛信宇test】您的验证码是{code}".format(code=code)
        }

        rep=requests.post(url=self.url,data=param)
        print(rep)


if __name__ == '__main__':
    message=Message("40d6180426417bfc57d0744a362dc108")
    message.send_message("18381137831","520")
