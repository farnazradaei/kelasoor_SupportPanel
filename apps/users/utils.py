from kavenegar import *
from kavenegar import KavenegarAPI, APIException, HTTPException


def send_otp_sms(phone, message):
    try:
        api = KavenegarAPI('37316A4A677756394D5649486C44516D5557413255517857776F704349536D694B2F5275562F76305569593D')  # کلید API واقعی رو بذار اینجا
        params = {
            'sender': '2000660110',
            'receptor': phone,
            'message': message
        }
        response = api.sms_send(params)
        return True
    except (APIException, HTTPException) as e:
        print(f"Error sending SMS: {e}")
        return False
