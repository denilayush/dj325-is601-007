<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Denil Jain (dj325)</td></tr>
<tr><td> <em>Generated: </em> 10/7/2023 2:52:11 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/dj325" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.53.54image.png.webp?alt=media&token=e38c0b0a-c26c-4716-b393-2538514cfbca"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for add_task function, which includes all the needed Deliverables. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-06T22.17.09image.png.webp?alt=media&token=8344c79d-afae-43e0-8c7c-70322b638fdc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure of add_task() function if any of the input is empty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-06T22.19.28image.png.webp?alt=media&token=ccc361ea-d5f8-416e-b599-403f99ffa342"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result after adding a new Task correctly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div>&nbsp;updated lastActivity with the current datetime value in the correct format,</div><div>&nbsp;added a condition<br>to check name, description, and due date are provided,</div><div>&nbsp;the due date must match<br>one of the formats mentioned in str_to_datetime(),</div><div>&nbsp;added the new task to the tasks<br>list,</div><div>&nbsp;Provided a message confirming the new task was added or if the addition<br>was rejected due to missing data,</div><div>&nbsp;included My ucid and date as a comment&nbsp;</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T04.59.10image.png.webp?alt=media&token=2eab4ee3-fa48-4496-84c4-8497894b29b1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated Code for Update task function.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div>Function Accepts an index argument, used to specify the position of a task<br>within a list or data structure named tasks.</div><div>the provided index is valid for<br>accessing a task within the tasks list.&nbsp;</div><div>It validates the index by ensuring that<br>it is not negative and is within the bounds of the list.&nbsp;</div><div>If the<br>index is invalid, an error message is printed, and the function returns without<br>performing any updates.</div><div>If the index is valid, it retrieves the task from the<br>tasks list using the provided index and stores it in the task variable.</div><div>The<br>function then prints the current values of the task's name, description, and due<br>date using the print() function.</div><div>It prompts the user to input new values for<br>the task's name, description, and due date using the input() function.&nbsp;</div><div>The user's input<br>is stored in the name, desc, and due variables.</div><div>Finally, the function calls an<br>external function named update_task(index, name=name, description=desc, due=due),&nbsp;</div><div>passing in the provided index along with<br>the updated task information (new name, description, and due date).&nbsp;</div><div>&nbsp; &nbsp;&nbsp;</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.08.05image.png.webp?alt=media&token=75bc7b19-0c1e-4146-a10b-bb695d54b27c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of Update Task by index with the new provided values<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.19.48image.png.webp?alt=media&token=bd398a65-9fa9-4f29-8a8e-3aa9a6a16093"/></td></tr>
<tr><td> <em>Caption:</em> <p>Explanation of the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.13.07image.png.webp?alt=media&token=2235360c-1f83-4d3d-9393-aacc112f45f7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.13.51image.png.webp?alt=media&token=b69410d1-1449-458a-903b-39140c029e04"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div>Code begins by checking if the provided index is within valid bounds for<br>accessing a task within the tasks list.&nbsp;</div><div>If the index is either negative or<br>greater than or equal to the length of the tasks list, it prints<br>an error message indicating that the task was not found.</div><div>If the index is<br>valid, it retrieves the task from the tasks list using the provided index<br>and stores it in the task variable.<br></div><div>then checks if new values have been<br>provided for the task's name, description, and due date.&nbsp;</div><div>If any of these properties<br>have been updated (i.e., the corresponding argument is not an empty string),&nbsp;</div><div>it updates<br>the task's properties accordingly.&nbsp;</div><div>It also sets a flag (UpdateFlag) to indicate that at<br>least one property was changed.<br></div><div>the function updates the lastActivity property of the task<br>with the current date and time using datetime.now().strftime("%m/%d/%Y %H:%M:%S").<br></div><div>Depending on whether any properties<br>were changed (UpdateFlag == True), the function prints a message indicating whether the<br>task was updated or not.<br></div><div>After processing the updates, it updates the task within<br>the tasks list with the modified task object.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.21.24image.png.webp?alt=media&token=6d0dea90-ac7f-4ef0-ae61-adfbaf2f67a6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mark as done function logic<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.27.59image.png.webp?alt=media&token=42a39951-e643-4d42-9c33-cdd93d33ffae"/></td></tr>
<tr><td> <em>Caption:</em> <p>Explanation of the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.22.54image.png.webp?alt=media&token=31cf1c4c-55e6-4d47-b6db-c2a422c691fe"/></td></tr>
<tr><td> <em>Caption:</em> <p>Both success and failure is mentioned<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div>The function checks whether the provided index is valid for accessing a task<br>within the tasks list.&nbsp;</div><div>If the index is either negative or greater than or<br>equal to the length of the tasks list, it prints an error message<br>indicating that the task was not found and returns early, ensuring that no<br>further actions are taken.</div><div>If the provided index is valid, it retrieves the task<br>from the tasks list using the provided index and stores it in the<br>task variable.<br></div><div><br></div><div>Code then checks if the task is currently marked as "done" by<br>examining its done property.&nbsp;</div><div>If the task is not already marked as done (task['done']<br>== False), it updates the done property with the current date and time<br>using datetime.now().strftime("%m/%d/%Y %H:%M:%S").&nbsp;</div><div>This records the moment when the task was marked as done.<br>It also prints a message confirming that the task has been marked as<br>done.</div><div><br></div><div>if the task is already marked as done, the code prints a message<br>stating that it's already been completed, indicating that no further updates are made.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.28.52image.png.webp?alt=media&token=cea7d51c-6179-491b-a185-6f2b6ddbafd1"/></td></tr>
<tr><td> <em>Caption:</em> <p>View task code <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.33.55image.png.webp?alt=media&token=bd785f53-de30-44cd-b700-0db7eeac2c72"/></td></tr>
<tr><td> <em>Caption:</em> <p>Explanation of the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.35.29image.png.webp?alt=media&token=5df896cf-1738-4007-a373-a8285409d0c6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure and success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.38.48image.png.webp?alt=media&token=6a181496-b08e-42e0-ac08-69bcf60d14de"/></td></tr>
<tr><td> <em>Caption:</em> <p>Examples<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.42.24image.png.webp?alt=media&token=9d71d96f-e7a7-4118-87ad-9ec6787f5a65"/></td></tr>
<tr><td> <em>Caption:</em> <p>code with all the deliverables<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T05.55.48image.png.webp?alt=media&token=aa28659a-86d8-4574-baf5-09c587d4d65f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Both success and failure conditions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div>The function begins by checking whether the provided index is valid for accessing<br>a task within the tasks list.&nbsp;</div><div>If the index is either negative or greater<br>than or equal to the length of the tasks list, it prints an<br>error message indicating that the task was not found and returns early, ensuring<br>that no further actions are taken.</div><div><br></div><div>Provided the index is valid, it proceeds to<br>delete the task from the tasks list using the pop() method, which removes<br>the task at the specified index.</div><div>After successfully deleting the task, it prints a<br>success message confirming that the task was deleted.<br></div><div>If the index is invalid (out<br>of bounds), the code will not attempt to delete a task and will<br>print the appropriate error message instead.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T06.03.22image.png.webp?alt=media&token=d8c4be2c-4a10-4aca-8472-5126acd49cb4"/></td></tr>
<tr><td> <em>Caption:</em> <p>function that checks for incomplete task <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T06.08.34image.png.webp?alt=media&token=7ebb3729-fb45-4424-9dfe-16ea8d474439"/></td></tr>
<tr><td> <em>Caption:</em> <p>listed the tasks and marked all as done, then listed the incomplete task<br>again, which shows all tasks are done <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>code starts by creating an empty list named _tasks.&nbsp;</div><div>This list will be used<br>to store incomplete tasks based on the requirements.</div><div><br></div><div>function then iterates through each task<br>in the tasks list.&nbsp;</div><div>For each task, it checks whether the done property is<br>False, indicating that the task is not marked as done.&nbsp;</div><div>If the condition is<br>met, the task is added to the _tasks list.</div><div>After filtering and creating a<br>list of incomplete tasks, the code calls a function named list_tasks(_tasks).&nbsp;</div><div>This function is<br>assumed to display or list the tasks that are passed to it.<br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T06.12.43image.png.webp?alt=media&token=149a4709-ee52-4492-b359-175c9cd4cd9c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for the over due function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T06.19.08image.png.webp?alt=media&token=e82a3b12-1297-4b62-9a95-aaf377674959"/></td></tr>
<tr><td> <em>Caption:</em> <p>success and failure both<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>code starts by creating an empty list named _tasks. This list will be<br>used to store overdue tasks based on the requirements.</div><div>Function then retrieves the current<br>date and time using datetime.now().strftime("%m/%d/%Y %H:%M:%S") and stores it in the current variable.<br>This current datetime will be used for comparison.<br></div><div><br></div><div>The function iterates through each task<br>in the tasks list. For each task, it does two checks:<br></div><div><br></div><div>It converts the<br>task's due date (stored as a string) to a datetime object using datetime.strptime(task['due'],<br>"%m/%d/%Y %H:%M:%S").</div><div>It compares this converted due date with the current datetime (current) to<br>check if the task is overdue.</div><div>It also checks whether the done property of<br>the task is False, indicating that the task is not marked as done.</div><div>If<br>both conditions are met (the task is overdue and not done), the task<br>is added to the _tasks list.</div><div>After filtering and creating a list of overdue<br>tasks, the code calls a function named list_tasks(_tasks).&nbsp;</div><div>This function is assumed to display<br>or list the tasks that are passed to it.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T06.28.36image.png.webp?alt=media&token=128251a7-3d5c-4be6-a147-18df4c133d3d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Remaining function code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T06.28.40image.png.webp?alt=media&token=6a7d7095-ce5e-44c8-b526-bdae2758bf5a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T06.22.54image.png.webp?alt=media&token=0613d206-0dc1-49be-b506-c02e553a25e0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Both overdue and remaining time<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <div>function begins by checking whether the provided index is valid for accessing a<br>task within the tasks list.&nbsp;</div><div>If the index is either negative or greater than<br>or equal to the length of the tasks list,&nbsp;</div><div>it prints an error message<br>indicating that the task was not found and returns early, ensuring that no<br>further actions are taken.</div><div><br></div><div>If the provided index is valid, it proceeds to retrieve<br>the task from the tasks list using the provided index and stores it<br>in the task variable.</div><div><br></div><div>then compares the due date of the task with the<br>current date and time to determine whether the task is overdue or has<br>time remaining.&nbsp;</div><div>It uses datetime.strptime() to convert the due date (stored as a string)<br>and the current date (generated by datetime.now().strftime("%m/%d/%Y %H:%M:%S")) into datetime objects for comparison.</div><div><br></div><div>If<br>the task is not overdue (if datetime.strptime(task['due'], "%m/%d/%Y %H:%M:%S") &gt; datetime.strptime(current,"%m/%d/%Y %H:%M:%S")),&nbsp;</div><div>it calculates<br>the remaining time by subtracting the current datetime from the task's due date.&nbsp;</div><div>The<br>result is split into hours, minutes, and seconds components for clear formatting.</div><div><br></div><div>If the<br>task is overdue, it calculates the time that has passed since the due<br>date by subtracting the task's due date from the current datetime.&nbsp;</div><div>The result is<br>also split into hours, minutes, and seconds components.</div><div><br></div><div>code prints the hours, minutes, and<br>seconds components along with the status ("remaining" or "overdue").&nbsp;</div><div>formatting is designed to show<br>the time components clearly, such as "X hours, X minutes, X seconds."</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T06.35.26image.png.webp?alt=media&token=e54d9c8e-3ee0-4388-a76f-d4fdc78f2426"/></td></tr>
<tr><td> <em>Caption:</em> <p>Examples of the code working<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-07T06.36.47image.png.webp?alt=media&token=598f3b47-d655-4ff5-a335-ad96e658d650"/></td></tr>
<tr><td> <em>Caption:</em> <p>Some different outputs<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <div>Handling date and time data was a little tricky,</div><div>comparing the dates and conditions<br>as per the given tasks</div><div>I was getting too many errors while changing the<br>format from str to time and time to str.</div><div>but I was using the<br>wrong syntax then googled the correct syntax.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/8">https://github.com/denilayush/dj325-is601-007/pull/8</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/dj325" target="_blank">Grading</a></td></tr></table>