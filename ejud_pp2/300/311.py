from datetime import datetime,timedelta
date_str=input()
days_to_add=int(input())
date=datetime.strptime(date_str,"%Y-%m-%d")
new_date=date+timedelta(days=days_to_add)
print(new_date.strftime("%Y-%m-%d"))
