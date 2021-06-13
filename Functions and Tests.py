from datetime import *

paymentDateTime = ""
paymentDateTime = str(datetime.now())
paymentDate = paymentDateTime.split(" ")[0]
paymentTime = paymentDateTime.split(" ")[1]

print(paymentDate)
print(paymentTime)