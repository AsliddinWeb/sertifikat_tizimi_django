from datetime import date
today = date.today().strftime("%d.%m.%Y")
print(len(today.split(".")))