from datetime import datetime
dt1=datetime.strptime(input(), "%Y-%m-%d %H:%M")
dt2=datetime.strptime(input(),"%Y-%m-%d %H:%M")
diff=dt2-dt1
minutes=diff.total_seconds()//60
print(int(minutes))