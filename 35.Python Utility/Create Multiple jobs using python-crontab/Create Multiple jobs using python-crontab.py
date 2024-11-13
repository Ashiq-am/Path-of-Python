from crontab import CronTab

cron=CronTab(user="aayussss2101")

job1=cron.new(command="python3 test1.py")
job1.minute.every(2)

job2=cron.new(command="python3 test2.py")
job2.minute.every(1)

cron.write()
