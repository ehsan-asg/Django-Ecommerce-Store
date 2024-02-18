from kavenegar import *
def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('526C466C722B32733961374E31753451796137666D5A774E544B6C616A5975492F3436435766772F486F673D')
        params = {
            'sender':"",
            'receptor':phone_number,
            'message':f"کد تایید شما: {code}"
        }
        response = api.sms_send(params)
        print(response)

    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
