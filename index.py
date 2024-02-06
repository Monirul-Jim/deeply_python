
from datetime import datetime
current_time = datetime.now().time()
if current_time >= datetime.strptime("00:00", "%H:%M").time() and current_time <= datetime.strptime("11:59", "%H:%M").time():
    print("Good morning!")
else:
    print("Good night!")
