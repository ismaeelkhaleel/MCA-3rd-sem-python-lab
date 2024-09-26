import secrets
def random_otp():
    otp = secrets.randbelow(1000000)
    return f"{otp:06d}"

otp = random_otp()
print("Your otp is : ", otp)