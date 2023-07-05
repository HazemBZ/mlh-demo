import json
import os

from celery import Celery

from helpers.common_requests import send_data
from helpers.parsers import AnnouncementParser
from tasks_management.mappers import ScenariosMapper

broker = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

celery = Celery(__name__)
celery.conf.broker_url = broker
celery.conf.result_backend = backend


@celery.task(name="create_task")
def create_task(site, data):
    AnnouncementParser.parse_request(data)
    announcement_url = False
    try:
        scenario = ScenariosMapper.get_scenario(site)()
        announcement_url = scenario.run()
    except Exception as e:
        print(getattr(e, "message", repr(e)))
        return {
            AnnouncementParser.get_id(site): {
                "status": False,
                "errors": str(e),
                "url": announcement_url,
            }
        }
    return {
        AnnouncementParser.get_id(site): {
            "status": True,
            "errors": False,
            "url": announcement_url,
        }
    }


@celery.task(name="notify_post_task")
def notify_post_task(results, target, header):
    print(f"notify_post_task:: result={results},target={target},header={header}")

    logs = {}
    for res in results:
        logs.update(res)
    body = {"X_TOKEN": header.get("X_TOKEN"), "logs": logs}
    print(f"notify_post_task:: request body:: {body}")

    try:
        send_data(
            target,
            json=body,
            headers={**header},
        )
        print("Tasks end notification sent")
    except Exception as e:
        print("Failed to send end notification :: error :: ", e)


@celery.task(name="chord_error_handle")
def error_callback(*args, **kwargs):
    print("[Handling Chord error]")
    print(*args, **kwargs)

    return {"Subject": "chord errors", "args": args, "kwargs": kwargs}
