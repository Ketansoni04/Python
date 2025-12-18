password = "Sec3P@tt"

Pass_Len = len(password)

if Pass_Len < 6:
    status = "Weak Password"
elif Pass_Len < 10:
    status = "Medium Password"
else:
    status = "Strong Password"

print("Password strength is " + status)
