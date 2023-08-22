# OTP Ninja
## _Universal OTP authentication solution_ ##
[![Build Status](https://github.com/NaveenNirban/OTP-Ninja-Django/build-version.svg)](https://github.com/NaveenNirban/OTP-Ninja-Django/build-version.svg)

OTP Ninja is a django backed, multi-tenant, micro-service based, universal otp authentication solution.

## Features
- Microservice architecture based application, having its own standlone apis.
- Powered by latest Django 4.2
- Mulit-tenant based model.(Register mulitple projects)
- UUID4 based secure API_KEYs for registered projects.
- Support mulitple Bulk OTP providers.
- Supports email server configurations.


## Installation( Ubuntu & MacOS-M1 )

```sh
git clone https://github.com/NaveenNirban/OTP-Ninja-Django.git
cd OTP-Ninja-Django/otpmicroservice
python3 -m pip install virtualenv & virtualenv venv & source venv/bin/activate
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
pip install -r requirements.txt
mkdir logs
```
Now create & configure .env File using the Article just below Installation.
```
python manage.py runserver
```
If everything seems fine, then _Migrate_ database tables
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Environment Variables

I know environment variable list is bit large, will consize in near future.
P.S - Fast2Sms env. variables are not mandatory.
[https://gist.github.com/NaveenNirban/c219bbcdcbdbfdb0e49e2a71de91a24b] - Sample .env file for direct download

| Variables Key | Value | Description |
| ------ | ------ | ------ |
| PROD | {True or False} |
| SECRET_KEY | {Django project secret key} |
| FAST2SMS_API  | { Fast2SMS API key} | Ask your Fast2Sms vendor to for this, can be found in portal dashboard|
| FAST2SMS_ROUTE | {dlt / quick otp } | found in portal dashboard |
| FAST2SMS_SENDER_ID | {Sender id} | check dashboard |
| FAST2SMS_MESSAGE_ID | {Sender id} | check dashboard |
| BYPASSUSERID | {123456789} | Use your own mobile no, if you want to bypass otp verification for a specific mobile no.|
| BYPASSUSERIDOTP | {123456} | Use your complex own otp to verification bypass |
| EMAIL_HOST | {mymail.somemailserverdomain.com} | Find your email host from email server |
| EMAIL_PORT | {587} | Check with email server config, 587 for gmail usually. |
| EMAIL_USE_TLS | {True} | Usually True |
| EMAIL_HOST_USER | {noreply@naveenKaMailDomain.com} | Email user from which uses will be recieving emails |
| EMAIL_HOST_PASSWORD | {supersecret} | Password of email account |
| PROD_DB_USER | {admin} | Database user name |
| PROD_DB_PASS | {password} | Database password | 
| PROD_DB_HOST | {3.15.789.45} | Your database host public IP or domain name | 
| PROD_DB_PORT | {3306} | 3306 for MYSQL, can differ incase of db drivers |
| PROD_DB_NAME | {default} | Database name that will be used for your project | 
| DEV_DB_USER | {admin} | Database user name |
| DEV_DB_PASS | {password} | Database password | 
| DEV_DB_HOST | {3.15.789.45} | Your database host public IP or domain name | 
| DEV_DB_PORT | {3306} | 3306 for MYSQL, can differ incase of db drivers |
| DEV_DB_NAME | {default} | Database name that will be used for your project | 


## References
MYSQL Installation issues in Ubuntu - https://askubuntu.com/a/1482193/1142651

## Endpoints

| Endpoint | Method | Request(Form-data) | Response |
| ------ | ------ | ------ | ------ |
| /sendOTP | POST | userid - 1234567890, apikey - e286b536-0e06-45d6-a610-1dgf4f2ce665, mode -1 | {"status": true,"msg": "OTP sent successfully","data": {}} |
| /verifyOTP | POST | userid - 1234567890, apikey - e286b536-0e06-45d6-a610-1dgf4f2ce665, otp -123456 | {"status": true,"msg": "OTP verified successfully","data": {}} |

## Contact Info
Feel free to ping me at any handle, I'll be happy to connect. Don't hesitate in any query, I'll be happy to help you out buddy.
Email me - Naveennirbanyadav08@gmail.com
Linkedin - https://linkedin.com/in/naveennirban
Stackoverflow - https://stackoverflow.com/users/8585150/christopher-nolan

## Future plans & collaborations
1. Add more Bulk SMS providers templates.
2. Implement Celery Message Queue using Redis/RabbitMQ. (_Working on_)
3. Docker & Docker-compose support. (_Working on_)
4. License updations for code. Code will open-source for sure & free to use.
5. Any improvements/features suggested by community.

## License

MIT

**Free Software, Hell Yeah!**