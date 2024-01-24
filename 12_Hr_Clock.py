import time

print("\nCurrent Date & Time: ")

while True:
    # Displays the current date, time, & timezone:
    print(time.strftime('%m/%d/%Y, %a | %I:%M:%S %p (%Z %z)'),  
    end='\r')       # Keeps the printed output on the same line.
    
    time.sleep(1)   # 1 second lag before updating the current date & time.

