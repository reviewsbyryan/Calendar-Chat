import json
from Google import create_service

taskList_id = "TklyOGR4TDdhX2hRbHZhUg"

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def create_task(title, notes=None, due=None, status='needsAction', deleted=False):

    request_body = {
      'title': title,
      'notes': notes,
      'due': due,
      'status': status,
      'deleted': deleted
    }

    print(json.dumps(request_body))

    service.tasks().insert(tasklist=taskList_id, body=request_body).execute()
    return json.dumps(request_body)

def list_tasks():
    response = service.tasks().list(
        tasklist=taskList_id,
        showCompleted=False,
        showDeleted=False,
        showHidden=False,
      ).execute()
    
    tasks = response['items']

    filtered_tasks = []

    for task in tasks:
        filtered_tasks.append({'id': task['id'], 'title': task['title'],})

    return json.dumps(filtered_tasks)

def delete_task(task_id):
    service.tasks().delete(tasklist=taskList_id, task=task_id).execute()
    return json.dumps(task_id)

def complete_task(task_id):

    response = service.tasks().list(
        tasklist=taskList_id,
        showCompleted=False,
        showDeleted=False,
        showHidden=False,
      ).execute()
    
    task_list = response.get('items')

    for task in task_list:
        if task['id'] == task_id:
            task['status'] = 'completed'
            service.tasks().update(
                tasklist=taskList_id,
                task=task.get('id'),
                body=task,
            ).execute()

    return json.dumps(task_id)