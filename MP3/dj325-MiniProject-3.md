<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Denil Jain (dj325)</td></tr>
<tr><td> <em>Generated: </em> 11/14/2023 5:09:28 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/dj325" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T20.26.15image.png.webp?alt=media&token=16823d4e-f425-4119-a2ba-68efd1245284"/></td></tr>
<tr><td> <em>Caption:</em> <p>Prod Heroku<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T20.25.22image.png.webp?alt=media&token=8ef8bf5a-7af4-4a06-b5e8-e3a65df583ea"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of index.html<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T20.38.25image.png.webp?alt=media&token=1c046945-7578-4486-98b2-f406e85b1c18"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI updates in NAVIGATION<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T20.38.36image.png.webp?alt=media&token=884bd0f8-cbc9-41a2-92a5-51e5955cd471"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code with updated urls<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T20.40.53image.png.webp?alt=media&token=7e904dc8-2053-422e-90b0-7f77a5d9db1a"/></td></tr>
<tr><td> <em>Caption:</em> <p>.csv File Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T20.42.34image.png.webp?alt=media&token=ead9cca3-5018-4492-9639-499dc1d27d8f"/></td></tr>
<tr><td> <em>Caption:</em> <p>After updating DB.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T20.52.30image.png.webp?alt=media&token=6c120d87-90ec-426a-b14e-e55c375ec5d8"/></td></tr>
<tr><td> <em>Caption:</em> <p>.csv file validation code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T20.46.48image.png.webp?alt=media&token=cd076eae-4cb9-40a8-a774-8ca76c375515"/></td></tr>
<tr><td> <em>Caption:</em> <p>Reading as a dict.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T20.58.33image.png.webp?alt=media&token=62af69f8-c574-4b88-a75a-623c8bfda3ee"/></td></tr>
<tr><td> <em>Caption:</em> <p>Firstname Lastname split code.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.04.00image.png.webp?alt=media&token=2d95d72a-f349-4c06-9861-317336144314"/></td></tr>
<tr><td> <em>Caption:</em> <p>add route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.04.10image.png.webp?alt=media&token=a377fc78-90ab-4356-ae45-2c9b0cc401c3"/></td></tr>
<tr><td> <em>Caption:</em> <p>add route code query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.05.51image.png.webp?alt=media&token=22455712-e6c9-416a-a875-8c0e00034bd7"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.06.00image.png.webp?alt=media&token=9c6aa770-da2c-49ec-befb-3ef7b2b5950e"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.06.06image.png.webp?alt=media&token=cadcf0d4-1eeb-4280-9942-7c27b0e12e0a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.08.09image.png.webp?alt=media&token=9ee40c20-9b1e-41b2-9984-32f85bf8ee95"/></td></tr>
<tr><td> <em>Caption:</em> <p>create donation page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.08.26image.png.webp?alt=media&token=207e23f5-6906-43b6-8015-7f848e51de2a"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit donation page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.11.16image.png.webp?alt=media&token=9c97bfdd-d44c-4d61-8153-3adc85cf0bbd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donation search page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.12.31image.png.webp?alt=media&token=0a358f3d-a12f-4bef-9aed-da94b161ac17"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donation Search page with organization name filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.25.21image.png.webp?alt=media&token=858fd289-c982-43b1-9f8d-8c77753c1c7a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donation HTML<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.14.21image.png.webp?alt=media&token=14bda7f9-189f-4f18-a47d-024052cdcb8f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search page code <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.14.30image.png.webp?alt=media&token=bd7aa164-2342-45ad-8031-0473b87446c0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search page code <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.22.09image.png.webp?alt=media&token=ed9852f1-15e1-4a42-818c-4f1e89779846"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of search route filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.22.14image.png.webp?alt=media&token=ebf55040-8814-4c7e-8e9c-cabec115f6a4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of search route filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.22.19image.png.webp?alt=media&token=50426d3f-13a7-4923-82f1-eb2902557ce6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of search route filters<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.26.43image.png.webp?alt=media&token=12b37a17-beb8-4851-8172-6394d05048ae"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.26.41image.png.webp?alt=media&token=211d1ebc-d6e1-423a-a6f3-d75e6b90ad2f"/></td></tr>
<tr><td> <em>Caption:</em> <p>add route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.30.10image.png.webp?alt=media&token=657d7c5a-5338-4445-b60d-6f98a4ce0d71"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit page route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.30.05image.png.webp?alt=media&token=e9ad1e90-a33e-4921-86dc-2e2ca7557289"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit page route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.30.02image.png.webp?alt=media&token=e2d0cf6c-b810-429a-a9a6-51710992f647"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit page route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.31.43image.png.webp?alt=media&token=98cec9e7-ae94-4fbc-b48c-e7f00f110df0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete route code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.48.24image.png.webp?alt=media&token=a32e61f8-cd85-4359-9999-32336b510138"/></td></tr>
<tr><td> <em>Caption:</em> <p>Organization search page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.48.33image.png.webp?alt=media&token=fe1b8923-39c4-468b-97e1-c90e5b2dcc10"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.48.36image.png.webp?alt=media&token=97944710-85a5-4722-ae54-2ca5b46ad1e1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.51.28image.png.webp?alt=media&token=9b232e33-b955-4501-be22-981fcdee1884"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.51.30image.png.webp?alt=media&token=0c450810-aeb9-42d5-84d2-1d6fa8f0c75c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.51.32image.png.webp?alt=media&token=51eed2c4-8dfe-40aa-92fa-859d3ac320ef"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.52.47image.png.webp?alt=media&token=c98a6ae7-ac79-4983-9360-4b2f465aeada"/></td></tr>
<tr><td> <em>Caption:</em> <p>Organization Search page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.54.13image.png.webp?alt=media&token=c1fad38c-cdbc-4e75-acf7-63a06d29a6dc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.56.02image.png.webp?alt=media&token=c42a51c2-6a65-4d9e-9ed1-11440f7a8895"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.56.04image.png.webp?alt=media&token=aa4d3a6b-d9fd-4d97-be4e-81bd6450f79d"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T22.05.14image.png.webp?alt=media&token=b822d157-829a-446b-854f-1442c6b68921"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization search route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T22.05.12image.png.webp?alt=media&token=2e32b381-e296-44fc-85a0-3818fab7d296"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization search route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T22.05.18image.png.webp?alt=media&token=e5fe3f46-980d-4dd8-948e-0aa310901f7e"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization search route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T22.03.51image.png.webp?alt=media&token=55bfff66-3453-4927-b8ac-0c0da64da83c"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization add route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T22.03.48image.png.webp?alt=media&token=16db074b-fec1-48ec-a0ef-650b798ab4f1"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization add route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T22.03.37image.png.webp?alt=media&token=90da2e19-5a16-4e27-826f-a9854a2947a1"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization add route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T22.01.32image.png.webp?alt=media&token=2860c3ac-b694-4f6e-8f82-dc6f028969c7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T22.01.29image.png.webp?alt=media&token=8195a394-42b0-4b55-9e34-820a2d4298a6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T22.01.27image.png.webp?alt=media&token=a0e2241e-f935-4447-85bd-afa3682ccef7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T22.00.52image.png.webp?alt=media&token=13d1262b-6867-49b2-a9e6-a1b99b295185"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete route code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.46.36image.png.webp?alt=media&token=10ee4e24-b73a-493a-b428-aee2180dcdf0"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_donations.py all test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.45.16image.png.webp?alt=media&token=fef1fccb-dcf6-4a3d-bc6e-e68c20a856b6"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_organizations.py all 11 test cases passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.44.27image.png.webp?alt=media&token=e364c682-84ae-477f-bc02-575f4dba7b62"/></td></tr>
<tr><td> <em>Caption:</em> <p>Upload.py test case passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.43.17image.png.webp?alt=media&token=bbe6f360-ae1d-4973-a2b3-f372eba2526c"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_index.py All 3 test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p><b>Yes</b>, All test cases passed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/32">https://github.com/denilayush/dj325-is601-007/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.35.56image.png.webp?alt=media&token=c4ea5a8c-b4a8-4e1b-b51a-f46e39d5268d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Commit History<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.36.49image.png.webp?alt=media&token=4d4e4024-e4a9-47d3-b2b9-a2e4c30c9a45"/></td></tr>
<tr><td> <em>Caption:</em> <p>wakatime dashboard<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.36.55image.png.webp?alt=media&token=6232c493-ae55-493c-ad30-0401e866160f"/></td></tr>
<tr><td> <em>Caption:</em> <p>wakatime dashboard<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-14T21.37.10image.png.webp?alt=media&token=55779fc2-e006-4f2d-aacf-1d676656bbed"/></td></tr>
<tr><td> <em>Caption:</em> <p>wakatime dashboard<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-dj325-td-dee4fd95089e.herokuapp.com/">https://is601-007-dj325-td-dee4fd95089e.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/dj325" target="_blank">Grading</a></td></tr></table>