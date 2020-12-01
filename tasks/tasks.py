from .celery import app
import celery
import time
from django.core.mail import send_mail, BadHeaderError


class CallbackSendEmail(celery.Task):
    def on_success(self, retval, task_id, args, kwargs):
        return task_id + ' Send email seccess'

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('falseeeeeeeeeeeeee')
        pass
    pass


@app.task()
def run_in_10s():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)
    print("hello world")


@app.task(bind=True, name='send_email_tasks', base=CallbackSendEmail, track_started=True)
def send_email(self, subject, data, receiver):
    try:
        self.update_state(state="PROGRESS", meta={'progress': 50})
        # holding time 1s
        time.sleep(1)
        a = send_mail(subject, data, '1751010127tai@ou.edu.vn', [receiver],)
        self.update_state(state="PROGRESS", meta={'progress': 90})
        if a < 0:
            return "User can not receive email"
        return 'Email send success'
    except BadHeaderError:
        return 'bad header'


@app.task()
def show_log(data):
    print("Status " + data)
