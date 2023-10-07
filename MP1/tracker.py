from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this; use this task reference for the below requirements
    #dj325 01/10/23
    # update lastActivity with the current datetime value
    task['lastActivity'] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    # set the name, description, and due date (all must be provided)
    if name == "" :
        print("Task Name is Missing")
    if due == "":
        print("Task due is Missing")
    if description == "":
        print("Task description is Missing")
    if name == "" or due == "" or description == "":
        print("Please fill all the information")
        return
    try:
        datetime.strptime(due, "%m/%d/%Y %H:%M:%S")
    except ValueError:
        print("Provided Data time is not correct")
        return
    task["name"],task["description"],task["due"] = name,description,due
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    tasks.append(task)
    print("New task was added")
    # output a message confirming the new task was added or if the addition was rejected due to missing data based on the prior checks
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # make sure any checks/conditions clearly display an appropriate message of what failed
    """
    Added current time in lastActivity 
    if any of the data is not provided then I make sure that the user type that
    added a condition to check name, description, and due date are provided,
    provided data is updated to the task array
    the due date must match one of the formats mentioned in str_to_datetime(),
    added the new task to the tasks list,
    Provided a message confirming the new task was added or if the addition was rejected due to missing data,
    included My ucid and date as a comment 
    """
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    #dj325 02/10/2023
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index >= len(tasks) or index<0:
        print("The task which you want to update was not found")
        return
    # show the existing value of each property where the TODOs are marked in the text of the inputs below (replace the TODO related text with the found tasks's data)
    task = tasks[index]
    print( "Task Name:" ,task['name'])
    print("Task Description:" ,task['description'])
    print( "Task Due:" ,task['due'])
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    
    name = input(f"What's the name of this task? (TODO name) \n").strip()
    desc = input(f"What's a brief descriptions of this task? (TODO description) \n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) (TODO due) \n").strip()
    update_task(index, name=name, description=desc, due=due)
    """
    Function Accepts an index argument, used to specify the position of a task within a list or data structure named tasks.
    the provided index is valid for accessing a task within the tasks list. 
    It validates the index by ensuring that it is not negative and is within the bounds of the list. 
    If the index is invalid, an error message is printed, and the function returns without performing any updates.
    If the index is valid, it retrieves the task from the tasks list using the provided index and stores it in the task variable.
    The function then prints the current values of the task's name, description, and due date using the print() function.
    It prompts the user to input new values for the task's name, description, and due date using the input() function. 
    The user's input is stored in the name, desc, and due variables.
    Finally, the function calls an external function named update_task(index, name=name, description=desc, due=due), 
    passing in the provided index along with the updated task information (new name, description, and due date). 
    """

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    #dj325 02/10/23
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index >= len(tasks) or index<0:
        print("The task was not found")
    else:
        task = tasks[index]
        # Not needed because this function is called from previous function and the handling will not allow out of bound index to get in this function.
        # update incoming task data if it's provided (if it's not provided use the original task property value)
        UpdateFlag = False
        if name != "":
            task['name'] = name
            UpdateFlag = True 
        if description != "":
            task['description'] = description 
            UpdateFlag = True 
        if due != "":
            task['due'] = due 
            UpdateFlag = True 
        # update lastActivity with the current datetime value
        if UpdateFlag == True :
            task['lastActivity'] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            # output that the task was updated if any items were changed, otherwise mention task was not updated
            print("Your Task was updated") 
        else:
            print("Your Task was not updated")
        tasks[index] = task
        # make sure save() is still called last in this function
        # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
        save()
        """"
        Code begins by checking if the provided index is within valid bounds for accessing a task within the tasks list. 
        If the index is either negative or greater than or equal to the length of the tasks list, it prints an error message indicating that the task was not found.
        If the index is valid, it retrieves the task from the tasks list using the provided index and stores it in the task variable.
        then checks if new values have been provided for the task's name, description, and due date. 
        If any of these properties have been updated (i.e., the corresponding argument is not an empty string), 
        it updates the task's properties accordingly. 
        It also sets a flag (UpdateFlag) to indicate that at least one property was changed.
        the function updates the lastActivity property of the task with the current date and time using datetime.now().strftime("%m/%d/%Y %H:%M:%S").
        Depending on whether any properties were changed (UpdateFlag == True), the function prints a message indicating whether the task was updated or not.
        After processing the updates, it updates the task within the tasks list with the modified task object.
        """

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # dj325 02/10/2023
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index >= len(tasks) or index<0:
        print("The task was not found")
        return
    task = tasks[index]
    # if it's not currently marked as done, record the current datetime as the value (don't just set it as true)
    if task['done'] == False:
        task['done'] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        print("Task Done")
    # if it is currently done, print a message saying it's already been completed
    else:
        print("It's already been completed")
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    save()
    """
    The function checks whether the provided index is valid for accessing a task within the tasks list. 
    If the index is either negative or greater than or equal to the length of the tasks list, it prints an error message indicating that the task was not found and returns early, 
    ensuring that no further actions are taken.
    If the provided index is valid, it retrieves the task from the tasks list using the provided index and stores it in the task variable.

    Code then checks if the task is currently marked as "done" by examining its done property. 
    If the task is not already marked as done (task['done'] == False), it updates the done property with the current date and time using datetime.now().strftime("%m/%d/%Y %H:%M:%S"). 
    This records the moment when the task was marked as done. It also prints a message confirming that the task has been marked as done.

    if the task is already marked as done, the code prints a message stating that it's already been completed, indicating that no further updates are made.

    """

def view_task(index):
    """ View more info about a specific task fetch by index """
    #dj325 02/10/2023
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index >= len(tasks) or index<0:
        print("The task was not found")
        return
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = tasks[index] # <-- replace or update the assignment of this variable, I just used an empty dict so it would run without changes
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))
    """
    function checks whether the provided index is valid for accessing a task within the tasks list.
    If the index is either negative or greater than or equal to the length of the tasks list, it prints an error message indicating that the task was not found and returns early, 
    ensuring that no further actions are taken.
    If the provided index is valid, it retrieves the task from the tasks list using the provided index and stores it in the task variable.
    The code then displays detailed information about the task using the print() function. 
    """


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # dj325 02/10/2023
    # delete/remove task from list by index
    # message should show if it was successful or not
    if index >= len(tasks) or index < 0:
        print("The task was not found")
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    else:
        tasks.pop(index)
        print("Task was deleted Successfully")
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    
    save()
    """
    The function begins by checking whether the provided index is valid for accessing a task within the tasks list. 
    If the index is either negative or greater than or equal to the length of the tasks list, it prints an error message indicating that the task was not found and returns early, ensuring that no further actions are taken.

    Provided the index is valid, it proceeds to delete the task from the tasks list using the pop() method, which removes the task at the specified index.
    After successfully deleting the task, it prints a success message confirming that the task was deleted.
    If the index is invalid (out of bounds), the code will not attempt to delete a task and will print the appropriate error message instead.
    
    """

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    #dj325 02/10/2023
    _tasks = [] # <-- this is a placeholder to populate based on the above requirements
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    for task in tasks:
        if task['done'] == False:
            _tasks.append(task)
    if len(_tasks) < 1:
        print("All tasks are completed")
    else:
        list_tasks(_tasks)
    """
    code starts by creating an empty list named _tasks. 
    This list will be used to store incomplete tasks based on the requirements.

    function then iterates through each task in the tasks list. 
    For each task, it checks whether the done property is False, indicating that the task is not marked as done. 
    If the condition is met, the task is added to the _tasks list.
    After filtering and creating a list of incomplete tasks, the code calls a function named list_tasks(_tasks). 
    This function is assumed to display or list the tasks that are passed to it.
    """

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    #dj325 02/10/2023
    _tasks = [] # <-- this is a placeholder to populate based on the above requirements
    # generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
    current = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    for task in tasks:
        if datetime.strptime(current,"%m/%d/%Y %H:%M:%S") > datetime.strptime(task['due'],"%m/%d/%Y %H:%M:%S") and task['done'] == False :
            _tasks.append(task)
    list_tasks(_tasks)
    """
    code starts by creating an empty list named _tasks. This list will be used to store overdue tasks based on the requirements.
    Function then retrieves the current date and time using datetime.now().strftime("%m/%d/%Y %H:%M:%S") and stores it in the current variable. This current datetime will be used for comparison.

    The function iterates through each task in the tasks list. For each task, it does two checks:

    It converts the task's due date (stored as a string) to a datetime object using datetime.strptime(task['due'], "%m/%d/%Y %H:%M:%S").
    It compares this converted due date with the current datetime (current) to check if the task is overdue.
    It also checks whether the done property of the task is False, indicating that the task is not marked as done.
    If both conditions are met (the task is overdue and not done), the task is added to the _tasks list.
    After filtering and creating a list of overdue tasks, the code calls a function named list_tasks(_tasks). 
    This function is assumed to display or list the tasks that are passed to it.
    """

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing X days, X hours, X minutes, X seconds (time components must be clearly separated)
    # example: 1 day, 0 hours, 0 minutes, 0 seconds remaining
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is overdue (clearly note that it's overdue, values should be positive)
    # example: 0 days, 2 hours, 5 minutes, 10 seconds overdue (note there's no negative values)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #task = {}# <-- this is a placeholder to populate based on the above requirements
    # do your print logic here
    if index >= len(tasks) or index<0:
        print("The task was not found")
    else:
        task = tasks[index]
        current = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        if datetime.strptime(task['due'],"%m/%d/%Y %H:%M:%S") > datetime.strptime(current,"%m/%d/%Y %H:%M:%S") :
            status = "remaining"
            time = datetime.strptime(task['due'],"%m/%d/%Y %H:%M:%S") - datetime.strptime(current,"%m/%d/%Y %H:%M:%S") 
            time = str(time).split(":")
            hours = time[0] + " hours,"
            minutes = time[1] + " minutes,"
            seconds = time[2] + " sec"
        else:
            status = "overdue"
            time = datetime.strptime(current,"%m/%d/%Y %H:%M:%S") - datetime.strptime(task['due'],"%m/%d/%Y %H:%M:%S") 
            time = str(time).split(":")
            hours = time[0] + " hours,"
            minutes = time[1] + " minutes,"
            seconds = time[2] + " sec"
        print(hours,minutes,seconds,status)
        """
        function begins by checking whether the provided index is valid for accessing a task within the tasks list. 
        If the index is either negative or greater than or equal to the length of the tasks list, 
        it prints an error message indicating that the task was not found and returns early, ensuring that no further actions are taken.

        If the provided index is valid, it proceeds to retrieve the task from the tasks list using the provided index and stores it in the task variable.

        then compares the due date of the task with the current date and time to determine whether the task is overdue or has time remaining. 
        It uses datetime.strptime() to convert the due date (stored as a string) and the current date (generated by datetime.now().strftime("%m/%d/%Y %H:%M:%S")) into datetime objects for comparison.

        If the task is not overdue (if datetime.strptime(task['due'], "%m/%d/%Y %H:%M:%S") > datetime.strptime(current,"%m/%d/%Y %H:%M:%S")), 
        it calculates the remaining time by subtracting the current datetime from the task's due date. 
        The result is split into hours, minutes, and seconds components for clear formatting.

        If the task is overdue, it calculates the time that has passed since the due date by subtracting the task's due date from the current datetime. 
        The result is also split into hours, minutes, and seconds components.

        code prints the hours, minutes, and seconds components along with the status ("remaining" or "overdue"). 
        formatting is designed to show the time components clearly, such as "X hours, X minutes, X seconds.
        """

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()