import sched, time

schedule = sched.scheduler(time.time, time.sleep)

def save():
    print('saved')

def on_clcik_start():
    print('completely saved')
    save()
    schedule.enter(5, 1, on_clcik_start, ( ))

schedule.enter(3, 1, on_clcik_start, ())
schedule.run()