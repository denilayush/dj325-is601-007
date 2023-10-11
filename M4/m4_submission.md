<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Denil Jain (dj325)</td></tr>
<tr><td> <em>Generated: </em> 10/11/2023 3:03:49 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/dj325" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T04.20.27image.png.webp?alt=media&token=32da953e-859c-49dd-abcf-c1d8aaab7690"/></td></tr>
<tr><td> <em>Caption:</em> <p>Addition function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T04.21.26image.png.webp?alt=media&token=5d337acb-f1e9-46ea-b6c2-00e36fa4638c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Subtraction function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T04.21.59image.png.webp?alt=media&token=022b9567-2293-451a-8ca3-6008bfbe9649"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication Function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T04.22.24image.png.webp?alt=media&token=12621e25-e45b-40ce-9b00-ac87fe6f3fd0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division Function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T18.53.56image.png.webp?alt=media&token=9154e3bf-e29a-438e-a332-e1f0d5722a7c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases for num add num<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T19.01.28image.png.webp?alt=media&token=a1362417-2f2a-4045-8762-bbd538b1a147"/></td></tr>
<tr><td> <em>Caption:</em> <p>result of conditions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T18.54.33image.png.webp?alt=media&token=57246f4e-35bc-4b2b-8bef-bef75d82c965"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases for &quot;Ans&quot; add number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T19.01.42image.png.webp?alt=media&token=8d9898a7-9754-4434-97b8-1d06e0f5f171"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases passed result<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T18.56.47image.png.webp?alt=media&token=736ae757-46f7-415a-bb7c-48a2e84bd6b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-sub-number test cases code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T19.01.59image.png.webp?alt=media&token=e0772fcc-2070-40c5-a3cd-c7180039165d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases result of passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T18.55.49image.png.webp?alt=media&token=f2c69fd9-1cac-47cc-8dcd-2d9c3d4743a8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases of ans sub num<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T19.02.11image.png.webp?alt=media&token=1cc65f92-2a98-44fe-a375-b841a5fbc7cc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passed test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T18.57.38image.png.webp?alt=media&token=e1cf5246-0097-4ad3-8a65-52511ec9f277"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-mult-number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T19.02.21image.png.webp?alt=media&token=e20c60f1-f43b-4d11-a390-c30f01742fa6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passed test cases of this test<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T18.57.51image.png.webp?alt=media&token=2cd16e82-e1ad-40da-a612-7da640e9003e"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-multi-number test cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T19.03.20image.png.webp?alt=media&token=bed5f446-fbbb-4c0c-b505-391869edb2f7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passed test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T18.58.44image.png.webp?alt=media&token=bb6b9e9a-c9fd-4d54-95cd-df5d799ce92e"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-div-number test Cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T19.03.28image.png.webp?alt=media&token=545dc184-2f1e-48ba-abe9-b2a248a39994"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passes test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T18.58.56image.png.webp?alt=media&token=c2efe9ab-6838-4f86-b783-7ef3c9895394"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-div-num test function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-10-11T19.03.39image.png.webp?alt=media&token=4be0e560-3576-46db-9f76-e79a989dfdf0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>I was getting an error for just MyCal(), I was using MyCal directly<br>while testing test cases and due to that each time a new instance<br>of calculator was created, and value of &quot;ans&quot; was 0 for all of<br>the test cases. This took me 30 mins to debug this silly mistake.<div>Created<br>test cases and used pytest for the first time.</div><div>learned how to handle try<br>and except conditions with Exceptions.</div><div>Other tasks were good.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <p>I have used parameterized test cases for this HW, so parameterized test cases<br>are called from decorators to call the function and run the test cases<br>given as a parameter,<div>Test cases takes the input and expected output as parameters<br>and then process the inputs with the function to check the output of<br>that function with the provided expected output.<br><div>Created multiple test cases for each Mycal()&#39;s<br>public methods.</div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/13">https://github.com/denilayush/dj325-is601-007/pull/13</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/dj325" target="_blank">Grading</a></td></tr></table>