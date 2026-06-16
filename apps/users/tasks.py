from celery import shared_task

@shared_task(bind=True, max_retries=3)
def send_welcome_email(self, user_id):
    try:
        print(f"Welcome user {user_id}")
    except Exception as exc:
        raise self.retry(countdown=5, exc=exc)