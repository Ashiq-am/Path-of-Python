from datetime import datetime

current_time = datetime.now().isoformat()

print(datetime.fromisoformat(current_time))
