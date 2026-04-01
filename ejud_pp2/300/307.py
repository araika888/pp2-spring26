from datetime import datetime,timedelta
kun=input()
plus=int(input())
start=datetime.strptime(kun,"%Y-%m-%d")
end=start+timedelta(days=plus)
print(end.strftime("%Y-%m-%d"))