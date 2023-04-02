
# --------------------------------------
# File Name: 24_Hr_Clock.py
# --------------------------------------
# Date Finished: 07-21-2022
# --------------------------------------
# Description:
# This is a simple 24-hour format console 
# clock that shows the current date, time, 
# & timezone used continuously.  
# --------------------------------------

import time

print("\nCurrent Date & Time: ")

while True:
    # Displays the current date, time, & timezone:
    print(time.strftime('%m/%d/%Y, %a | %H:%M:%S %p (%Z %z)'),  
    end='\r')       # Keeps the printed output on the same line.
    
    time.sleep(1)   # 1 second lag before updating the current date & time.