from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.enums import ResponseCode, ResponseMessage, ResponseStatus
from .models import Projects, OtpMaster
from rest_framework.permissions import IsAuthenticated
from django_otp.oath import hotp, totp
import time,json
import base64
import pyotp,os
from dotenv import load_dotenv


import requests
from uuid import uuid4
from django.conf import settings
from .models import MyUser
from .tasks import send_mail_func
from otpmicroservice.settings import EMAIL_HOST, EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.http import JsonResponse
from api.enums import OtpMode
from api.otpVendors import OTPVendors
from api.otpTemplates import MailTemplates

# Load env. variables
load_dotenv()


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(uuid4)

# To send the OTP


class SendOTP(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            userid = request.POST.get('userid')
            apikey = request.POST.get('apikey')
            mode = request.POST.get('mode', 0)
            userid = userid.upper()
            mode = int(mode)
            status = ""
            msg = ""
            data = ""
            statusCode = ""

            # Fetching project
            project = Projects.objects.filter(apiKey=apikey).first()

            # Generating OTP
            if userid==os.getenv("BYPASSUSERID"):
                return bypassSend()
            else:
                keygen = generateKey()
                otpCounter = project.otpCounter
                key = base64.b32encode(keygen.returnValue(
                    userid).encode())  # Key is generated
                OTP = pyotp.HOTP(key, 6)

                # Check mode to send OTP
                if mode != "" and mode == OtpMode.mobile.value:
                    #  Prepare mobile template
                    otp = OTPVendors.fast2sms(mobile=userid,otp=OTP.at(otpCounter))
                    otp = json.loads(otp.text)
                    if otp['return']==True:
                        status = ResponseStatus.true.value
                        msg = ResponseMessage.sentSuccess.value
                        data = {}
                        statusCode = 200
                    else:
                        status = ResponseStatus.false.value
                        msg = otp['message']
                        data = {}
                        statusCode = otp['status_code']
                # Send otp to Email 
                elif mode != "" and mode == OtpMode.email.value:
                    print("email")
                    # Prepare email object
                    from_email = EMAIL_HOST_USER
                    ccMail = []
                    email = EmailMessage(
                        project.name+" OTP for login",
                        MailTemplates.mailTemplate(OTP.at(otpCounter),project.logo,project.name),
                        # mailTemplate(OTP.at(otpCounter)),
                        from_email,
                        [userid],
                        ccMail,
                    )
                    email.content_subtype = 'html'
                    email.send()
                    status = ResponseStatus.true.value
                    msg = ResponseMessage.sentSuccess.value
                    data = {}
                    statusCode = 200
                    # TODO : Shift code to Celery worker
                    # taskid = send_mail_func.delay(mail_body, 'naveen@myndsol.com')
                
                # Else condition
                else:
                    status = ResponseStatus.false.value
                    msg = ResponseMessage.modeNotSupported.value
                    data = {}
                    statusCode = 404
                
                return JsonResponse({
                    "status": status,
                    "msg": msg,
                    "data": data
                },
                    safe=False,
                    status=int(statusCode)
                )

        except Exception as e:
            return JsonResponse({
                "status": ResponseStatus.false.value,
                "msg": ResponseMessage.internalServer.value,
                "data": str(e)
            },
                safe=False,
                status=ResponseCode.internalServer.value
            )

# To verify the OTP
class VerifyOTP(APIView):
    def post(self, request, *args, **kwargs):
        userid = request.POST.get('userid')
        apikey = request.POST.get('apikey')
        otp = request.POST.get('otp')
        
        # Fetching project
        project = Projects.objects.filter(apiKey=apikey).first()

        if userid==os.getenv("BYPASSUSERID") and otp==os.getenv("BYPASSUSERIDOTP"):
            return bypassVerify()
        else:
            keygen = generateKey()
            key = base64.b32encode(keygen.returnValue(
                userid).encode())  # Generating Key
            # OTP = pyotp.HOTP(key)  # HOTP Model
            OTP = pyotp.HOTP(key, 6)
            otpRes = OTP.verify(otp, project.otpCounter)

            if (otpRes is True):
                project.otpCounter += 1
                project.save()
                return JsonResponse({
                    "status": ResponseStatus.true.value,
                    "msg": ResponseMessage.approved.value,
                    "data": {}
                },
                    safe=False,
                    status=ResponseCode.ok.value
                )
            else:
                return JsonResponse({
                    "status": ResponseStatus.false.value,
                    "msg": ResponseMessage.wrongOtp.value,
                    "data": {}
                },
                    safe=False,
                    status=ResponseCode.unathorized.value
                )


# Send otp fake
def bypassSend():
    # Bypassing OTP Send
    print("Bypassing OTP Send")
    return JsonResponse({
    "status": True,
    "msg": "OTP sent successfully",
    "data": {}
},
    safe=False,
    status=200
)

# Verify otp fake
def bypassVerify():
    return JsonResponse({
        "status": True,
        "msg": "OTP verified successfully",
        "data": {}
        },
            safe=False,
            status=200
        )
# class MobileSendOTP(APIView):
