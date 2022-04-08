from apscheduler.schedulers.background import BlockingScheduler


sched = BlockingScheduler()
sched.add_job(check_status, 'interval', minutes=3)
sched.start()
