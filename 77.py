from datetime import datetime

age = int(input('Input your age: '))

print(f"We think you were born back in {datetime.now().year - age}")
