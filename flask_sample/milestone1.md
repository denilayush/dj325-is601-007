<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Denil Jain (dj325)</td></tr>
<tr><td> <em>Generated: </em> 11/13/2023 6:48:54 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/dj325" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T17.53.35image.png.webp?alt=media&token=8dcebf77-b853-4122-9519-bdeefc1fcd2c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T17.53.51image.png.webp?alt=media&token=e338f178-4074-4074-87d3-9414bf2e3a6b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T17.56.19image.png.webp?alt=media&token=aa56312f-fa61-4fd9-933a-420bec65f6bd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password length validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T17.56.48image.png.webp?alt=media&token=8baa8c91-1b3e-40ec-9526-8346d78e02a1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Already Taken.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T17.57.17image.png.webp?alt=media&token=da22ffd0-2374-4919-81a1-c921e66b0517"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username not Available, Validation.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T17.59.45image.png.webp?alt=media&token=d7af0f9b-bf06-46bb-870c-c9dab6e56b52"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form in the correct format before submission.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T18.04.31image.png.webp?alt=media&token=340a6402-2cc7-401b-bd37-eae689397018"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid user data from Task 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/34">https://github.com/denilayush/dj325-is601-007/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>the form has validation from the frontend as well as in the backend.<br>When the submit button is hit, first frontend validations check if everything is<br>in the correct format including the length of the password, and the length<br>of the username which is min 2. If all validations are checked then<br>the server sends a post request and then in the backend the validations<br>such as checking the format of the email, and checking the username in<br>DB if that username is taken then Flash Error and if the email<br>is already in the DB flash error message. (This will block the DB<br>insert query to execute).<div>Passwords are not directly saved in DB because if DB<br>is compromised all user&#39;s passwords will compromised. So, we use&nbsp;<span style="color: rgb(78, 201,<br>176); background-color: rgb(31, 31, 31); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">bcrypt</span>&nbsp;to Encrypt<br>the user password before saving it in DB, this encryption includes these steps.<br>first, adding salt values to the password and then using a Hash function<br>to generate a new string which can be stored in DB, and whenever<br>a user tries to login bcrypt will use the same hash function to<br>generate a string and then that string is checked with the previously generated<br>string to validated the user password.</div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T18.52.33image.png.webp?alt=media&token=87adffc0-21ff-4f8c-8f2d-8be8b04ff33d"/></td></tr>
<tr><td> <em>Caption:</em> <p>user validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T18.53.15image.png.webp?alt=media&token=c2a5ee57-8b35-46ac-bc21-30c729210d6f"/></td></tr>
<tr><td> <em>Caption:</em> <p>password validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T18.54.36image.png.webp?alt=media&token=ea80f42f-8944-4438-b94a-dbb77be1f252"/></td></tr>
<tr><td> <em>Caption:</em> <p>Login <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/31">https://github.com/denilayush/dj325-is601-007/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>The username is checked in DB and if that username exists in the<br>DB then the password is validated using&nbsp;<span style="color: rgb(78, 201, 176); font-family: Consolas,<br>&quot;Courier New&quot;, monospace; white-space: pre; background-color: rgb(31, 31, 31);">bcrypt.</span>&nbsp;The password is added with<br>a salt value to hash and generate the encrypted string which was created<br>while creating a new user then that string is matched with the value<br>in DB.<div>This is how DB is utilized to store the encrypted password String<br>rather than directly storing the password because if DB is compromised then user<br>passwords can be leaked.</div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T19.06.06image.png.webp?alt=media&token=8fee6495-93d6-41d7-a1e2-21d17def59f7"/></td></tr>
<tr><td> <em>Caption:</em> <p>User Logged Out.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T19.09.51image.png.webp?alt=media&token=1f3c4672-5c61-4873-a9b6-50d2b34c890f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged out users cannot access the landing-page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/31">https://github.com/denilayush/dj325-is601-007/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>Flask-Login is an extension for Flask that manages user sessions. It provides a<br>current_user object, which represents the user currently logged in. This object is accessible<br>throughout the application, and it simplifies the process of managing user sessions, including<br>login and logout.<br></div><div>When a user logs into the application, Flask-Login handles the creation<br>of the current_user object. Typically, this is done by verifying the user's credentials<br>(e.g., username and password) against the application's user database. If the credentials are<br>valid, Flask-Login creates the current_user object and associates it with the current&nbsp;<br>When a<br>user tries to access a protected route or resource, Flask-Login checks if the<br>current_user object exists. If it does, the user is granted access; otherwise, they<br>are redirected to the login page. This ensures that only authenticated users can<br>access certain parts of the application.<br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T19.36.08image.png.webp?alt=media&token=2f49ee21-f9b3-4109-a3a5-cb71822c0ebe"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged-out users cannot access roles page.(We just have this handler)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T19.35.39image.png.webp?alt=media&token=47fdf0a3-e438-418b-9ddb-75ff201f8e62"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged-in user need proper role to access roles/add page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T19.44.31image.png.webp?alt=media&token=4590e780-34a7-446b-8c9e-d3dbb561610a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles DB table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T19.45.50image.png.webp?alt=media&token=29f69cf0-2bd2-42b2-9612-0fcf4c9cae13"/></td></tr>
<tr><td> <em>Caption:</em> <p>UserRoles DB table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T19.48.17image.png.webp?alt=media&token=e15e1703-8e63-472f-8ce3-d88105efa2a4"/></td></tr>
<tr><td> <em>Caption:</em> <p><a href="mailto:&#x64;&#x65;&#x6e;&#x69;&#108;&#x40;&#100;&#101;&#x6e;&#105;&#x6c;&#x2e;&#x63;&#x6f;&#109;">&#x64;&#x65;&#x6e;&#x69;&#108;&#x40;&#100;&#101;&#x6e;&#105;&#x6c;&#x2e;&#x63;&#x6f;&#109;</a><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/34">https://github.com/denilayush/dj325-is601-007/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>The User, user_roles and roles tables are used to verify if a user<br>has any role in the user_roles table and to determine the specific role<br>from the roles table.<br></div><div>so user's sessions are user to check these tables to<br>validate the roles and access to a particular page.</div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>the first user needs to create an account then for the first time<br>the admin role is given Directly form the DB by adding new UserRole.<div>then<br>that admin can handle the other roles and mange the user roles.<br>we are<br>using isActive to make the role activate and deactivate utilizing the same row<br>instead of adding and deleting each time.</div><div>multiple roles can be created from add<br>roles page, only the admin user can add roles to this table.</div><div>after adding<br>admin can assign these roles to users.</div><div>admin should not deactivate its own admin<br>role.<br>_formhelpers.html (in the root templates folder) has been updated to handle checkbox elements<br>via a jinja conditional.<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T20.56.22image.png.webp?alt=media&token=8ffcb7ac-98c7-4210-b434-6f44bfdb727c"/></td></tr>
<tr><td> <em>Caption:</em> <p>List Samples page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T20.59.18image.png.webp?alt=media&token=f5a45124-3c46-4ab8-8b93-ec3895609413"/></td></tr>
<tr><td> <em>Caption:</em> <p>Assign Roles<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T20.59.58image.png.webp?alt=media&token=be006911-d823-4b1a-9dc2-ff5a9c472a20"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T21.00.37image.png.webp?alt=media&token=212eb170-8173-48a6-8299-d80e7d2550e3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation Bar<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/35">https://github.com/denilayush/dj325-is601-007/pull/35</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>we used Bootstrap mostly for the CSS part. tables were created using the<br>bootstrap templates.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T21.09.08image.png.webp?alt=media&token=4352e109-09d4-4f19-9e9e-1494bf8ab0ae"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password do not match<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T21.10.43image.png.webp?alt=media&token=5dccec4c-68ee-41a6-a990-157bbae9cbb7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission Denied page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T21.11.03image.png.webp?alt=media&token=71ec7a69-998e-4618-ac3b-a82651756d45"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T21.42.00image.png.webp?alt=media&token=3bdc7d3c-a182-4947-81c1-3a97b1afbc2e"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid Username<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/35">https://github.com/denilayush/dj325-is601-007/pull/35</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>We are using Flash messages to show what&#39;s wrong, we are checking for<br>validations, and if we have any invalid conditions we just use Flash messages<br>to display it to the users.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T22.09.27image.png.webp?alt=media&token=d6169f8e-673c-4a05-a4f9-efb866677432"/></td></tr>
<tr><td> <em>Caption:</em> <p>Prefilled profile details.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/34">https://github.com/denilayush/dj325-is601-007/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>we are using current_user to retrieve the data and prefill it with the<br>current_user.email and username.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T22.25.46image.png.webp?alt=media&token=a494357a-b3ee-47ac-af28-203526748582"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T22.25.55image.png.webp?alt=media&token=5d17c186-1d39-4c86-a846-0402dd0887bf"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T22.27.13image.png.webp?alt=media&token=91ed4a55-102b-4089-bd34-624d1531314d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T22.27.44image.png.webp?alt=media&token=a80db731-d43f-40ca-b9c6-8cfbf723d224"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T22.29.06image.png.webp?alt=media&token=f5393d3d-16f4-49d8-b974-6660021f7013"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid username format.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T22.31.06image.png.webp?alt=media&token=e4540e24-665d-42b0-a19c-d9b82b8ac6a6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T22.36.14image.png.webp?alt=media&token=58e94211-6f88-41fe-83b1-6896cdefdc79"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-13T22.37.48image.png.webp?alt=media&token=5cb6f9af-7a58-4dcc-8447-19932efac27c"/></td></tr>
<tr><td> <em>Caption:</em> <p>After<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/34">https://github.com/denilayush/dj325-is601-007/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>This checks if we have the correct password for the logged-in user, and<br>checks if the new username exists in the DB but if not then<br>assign and update the users username with new username, same with the email.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>SQL CRUD operations.<div>learned how to use Flask Flash messages to update the info<br>to the user about the status of the requests.</div><div>Learned how to assign roles<br>and how to store this information using SQL tables.</div><div>I was getting errors while<br>uploading this to prod but fixed it, that was an issue because of<br>YML file.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dj325-prod-e4b2f4589d51.herokuapp.com">https://is601-dj325-prod-e4b2f4589d51.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/dj325" target="_blank">Grading</a></td></tr></table>