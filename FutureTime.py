#FutureTime.py
#Name: Miguel Alvarado
#Date: 1/29/2026
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  print("Ask me for hours")
  Hours = int(input("hours:"))
   
  #Ask user for minutes
  print("Ask me for minutes")
  addMinute= int(input("minutes:"))
  #Calculate the time after the user-supplied time has passed.
  futuretime = (currentMinute + addMinute) 
  newMinutes = (futuretime) % 60
  extraHours = (futuretime) // 60
  
  futureHour = (currentHour + Hours + extraHours) % 24
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print("the future time is", str(futureHour).zfill(2) + ":" + str(newMinutes).zfill(2))

if __name__ == '__main__':
  main()
