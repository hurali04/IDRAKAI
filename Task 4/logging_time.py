import datetime 
current=datetime.datetime.now().strftime("%H:%M:%S %Y-%M-%D")
with open("Logging_Time.txt",'a')as file:
    file.write(f"Logged in Successfully at {current}")
       