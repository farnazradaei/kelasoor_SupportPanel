from kavenegar import *

def send_otp(phone_number, code):
    try:
        api = KavenegarAPI('API_KEY_TORO_INJA_BEZAR')
        params = {
            'receptor': phone_number,
            'template': 'YourTemplateName',
            'token': code,
            'type': 'sms',
        }   
        response = api.verify_lookup(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
