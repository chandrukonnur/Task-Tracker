import argparse
from task_manager import add_task,update_task,delete_task,mark_done,mark_in_progress,list_tasks

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    parser.add_argument("command", choices=[
        "add", "update", "delete", "mark-in-progress", "mark-done", "list"
    ], help="Action to perform")

    parser.add_argument("params", nargs="*", help="Additional parameters")

    args = parser.parse_args()

    if args.command == "add":
        if not args.params:
            print("Error: Task description required!")
        else:
            add_task(" ".join(args.params))

    elif args.command == "update":
        if len(args.params) < 2:
            print("Error: Task ID and new description required!")
        else:
            update_task(int(args.params[0]), " ".join(args.params[1:]))

    elif args.command == "delete":
        if not args.params:
            print("Error: Task ID required!")
        else:
            delete_task(int(args.params[0]))

    elif args.command == "mark-in-progress":
        if not args.params:
            print("Error: Task ID required!")
        else:
            mark_in_progress(int(args.params[0]))

    elif args.command == "mark-done":
        if not args.params:
            print("Error: Task ID required!")
        else:
            mark_done(int(args.params[0]))

    elif args.command == "list":
        status = args.params[0] if args.params else None
        list_tasks(status)

if __name__ == "__main__":
    main()