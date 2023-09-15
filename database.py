import datetime
import google_tasks
import google_events
import pytz

current_timezone = pytz.timezone("America/Los_Angeles")

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
    {"role": "user", "content": "Current date and time: " + str(datetime.datetime.now())},
    {"role": "user", "content": "The time zone is: " + str(current_timezone)},
    {"role": "user", "content": "The current list of tasks is: " + google_tasks.list_tasks()},
]

available_functions = {
            "create_task": google_tasks.create_task,
            "delete_task": google_tasks.delete_task,
            "list_tasks": google_tasks.list_tasks,
            "complete_task": google_tasks.complete_task,

            "create_event": google_events.create_event,
            "delete_event": google_events.delete_event,
        }

functions = [
    {
      "name": "create_task",
      "description": 'Create a new task, eg. "Create a task called My Task"',
      "parameters": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the task, eg. 'My Task'"
          },
          "notes": {
            "type": "string",
            "description": 'The notes of the task, eg. "This is my task"'
          },
          "due": {
            "type": "string",
            "description": "Due date of the task, eg. '2023-09-11T12:00:00.000Z'"
          },
          "status": {
            "type": "string",
            "description": "The status of the task. It can be either needsAction or completed, eg. 'needsAction'"
          },
          "deleted": {
            "type": "boolean",
            "description": "The deleted status of the task. It can be either True or False, eg. 'False'"
          },
        },
        "required": ["title"]
      }
    },
    {
        "name": "delete_task",
        "description": 'Delete a task, eg. "Delete task 1"',
        "parameters": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "string",
                    "description": "The ID of the task, eg. '1'"
                },
            },
            "required": ["task_id"]
        },
    },
    {
        "name": "list_tasks",
        "description": 'Get a list of all tasks, eg. "Get all tasks or get a list of all tasks"',
        "parameters": {
            "type": "object",
            "properties": {
            },
            "required": []
        },
    },
    {
        "name": "complete_task",
        "description": 'Complete a task, eg. "Complete task 3"',
        "parameters": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "string",
                    "description": "The id of the task, eg. 'MjA4ODQ0OTUwMQ'"
                },
            },
            "required": ["task_id"]
        },
    },
    {
        "name": "create_event",
        "description": 'Create a new event, eg. "Create an event called My Event"',
        "parameters": {
            "type": "object",
            "properties": {
                "summary": {
                    "type": "string",
                    "description": "The name of the event, eg. 'My Event'"
                },
                "description": {
                    "type": "string",
                    "description": "The description of the event, eg. 'This is my event'"
                },
                "start_time": {
                    "type": "string",
                    "description": "The start time of the event, eg. '2023-09-11T23:00:00.000'"
                },
                "end_time": {
                    "type": "string",
                    "description": "The end time of the event, eg. '2023-09-11T23:00:00.000'"
                },
            },
            "required": ["event_name", "start_time", "end_time"]
        },
    },
    {
        "name": "delete_event",
        "description": 'Delete an event, eg. "Delete event 1"',
        "parameters": {
            "type": "object",
            "properties": {
                "event_id": {
                    "type": "string",
                    "description": "The ID of the event, eg. '1'"
                },
            },
            "required": ["event_id"]
        },
    },
]
