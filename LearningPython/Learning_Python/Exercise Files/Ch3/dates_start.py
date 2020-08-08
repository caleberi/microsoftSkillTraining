#
# Example file for working with date information
#

from datetime import date,time,datetime
def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Todays's date is {}".format(today))

  # print out the date's individual components
  print("Date components: ",today.month,today.day,today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("weekday",today.weekday)
  
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  print(datetime.now())

  # Get the current time


  
if __name__ == "__main__":
  main();
  