

def computepay(hour,rate):
    print("In computepay",hour,rate)
    if fh > 40:
        reg = rate * hour
        otp = (hour - 40.0) * (rate * 0.5)
        pay = reg * otp
    else:
        pay = hour * rate
    print("Returning: ", pay)
    return pay


sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay: ",xp)