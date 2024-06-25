from tasks_management.taskmanager import TasksManager
from helpers.parsers import AnnouncementParser
from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/announce")
async def announce(request: Request):
    data = await request.json()
    print("Data reveived --- ", data)

    errors = []
    try:
        AnnouncementParser.parse_request(data=data)
        # TODO: Move validators/validation to their own fork
        # AnnouncementParser.run_validators()
    except Exception as e:
        e_msg = str(e) or repr(e)
        errors.append(e_msg)
        print("Failed to parse announcement request")
        print({"error": e_msg})
    else:
        try:
            TasksManager.load_configs()
        except Exception as e:
            print("Failed to load job manager configs")
            print({"error": str(e) or repr(e)})

        else:
            TasksManager.run_jobs_and_notify(data)
    return {"errors": errors}
