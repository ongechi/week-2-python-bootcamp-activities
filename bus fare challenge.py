#bus fare challenge program
import datetime
import time
from datetime import date
# date
today=date.today()
print("Date:",today)
print("Day:",datetime.date.today().strftime("%a"))
#date and time
day=time.strftime("%a")
week = set(["Mon","Tue","Wed","Thur","Fri"])
Sat = set(["Sat"])
Sun = set(["Sun"])
#printing day time and the fare
if day in week:
    print("Fare: 100")
elif day in Sat :
    print("Fare: 60")

elif day in Sun:
    print("Fare: 80")



