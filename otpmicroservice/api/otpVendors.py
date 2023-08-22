import requests
import os
from dotenv import load_dotenv
load_dotenv()

class OTPVendors():
    def __init__(self):
        pass

    def fast2sms(mobile, otp):
        print("mobile")
        otp = requests.post("https://www.fast2sms.com/dev/bulkV2",
                            headers={"content-type": "application/json; charset=UTF-8",
                                     'Authorization': os.getenv('FAST2SMS_API')},
                            json={
                                "route": os.getenv('FAST2SMS_ROUTE'),
                                "sender_id": os.getenv('FAST2SMS_SENDER_ID'),
                                "message": os.getenv('FAST2SMS_MESSAGE_ID'),
                                "variables_values": otp,
                                "flash": 0,
                                "numbers": mobile
                            })
        print(otp.text)
        return otp
