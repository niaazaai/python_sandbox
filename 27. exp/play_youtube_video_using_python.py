
# importing the module
import pywhatkit
 
# using Exception Handling
# to avoid exceptions
try:
   
  # it plays a random YouTube
  # video of GeeksforGeeks
  # pywhatkit.playonyt("Insider") # Ekeeda
  pywhatkit.playonyt("HelpBnk")
  print("Playing...")
 
except:
   
  # printing the error message
  print("Network Error Occurred")