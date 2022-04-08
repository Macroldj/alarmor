from apscheduler.schedulers.background import BlockingScheduler

from tasks.kubernetes import k8s_tasks

sched = BlockingScheduler()
sched.add_job(k8s_tasks(), 'interval', minutes=3)
sched.start()
