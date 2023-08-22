from enum import Enum,IntEnum


######### General Purpose Enums ####


######### Response Enums ########
class ResponseStatus(Enum):
    true = True
    false = False

class ResponseCode(IntEnum):
    # Client Error
    methodNotAllowed = 405
    unathorized = 401
    notFound = 404
    bad = 400
    maximumLimit = 429

    # Okay
    ok = 200
    created = 201

    # Server Error
    internalServer = 500

class ResponseMessage(Enum):
    fetchSucess = "Data fetched successfully"
    saveSuccess = "Profile updated successfully"
    uploadSuccess = "Upload successfully"

    # Method not allowed
    onlyGetAllowed = "Only GET allowed"
    onlyPostAllowed = "Only POST allowed"

    # OTP responses
    sentSuccess = "OTP sent successfully"
    approved = "OTP verified successfully"
    wrongOtp = "Wrong OTP"

    # Auth
    createdSuccessfully = "User created successfully"
    userFound = "User found"
    userNotFound = "User not found"

    # Error messages
    internalServer = "Internal Server Error"

    # OTP mode
    modeNotSupported = "Otp mode not supported"

class OtpMode(Enum):
    email = 0
    mobile = 1