<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Denil Jain (dj325)</td></tr>
<tr><td> <em>Generated: </em> 11/28/2023 12:17:56 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/dj325" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Which API did you choose?</td></tr>
<tr><td> <em>Response:</em> <p><b><a href="https://rapidapi.com/SAdrian/api/moviesdatabase/details">https://rapidapi.com/SAdrian/api/moviesdatabase/details</a></b><br>I am using MoviesDatabase data API.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Which endpoints will be used?</td></tr>
<tr><td> <em>Response:</em> <div><div><font face="Lato, sans-serif"><span style="text-wrap: nowrap;">EndPoints</span></font></div><ol><li><font face="Lato, sans-serif"><span style="text-wrap: nowrap;">Titles</span></font></li><li><font face="Lato, sans-serif"><span style="text-wrap: nowrap;">Search<br>(I will be using this Endpoint for my Project)</span></font></li><li><font face="Lato, sans-serif"><span style="text-wrap: nowrap;">Actors</span></font></li><li><font<br>face="Lato, sans-serif"><span style="text-wrap: nowrap;">Utils</span></font></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What pieces of data will be used in your app?</td></tr>
<tr><td> <em>Response:</em> <p><font face="Lato, sans-serif"><span style="white-space: pre;"><b>Sample endpoint data output:</b><br>    {<br> <br>    &quot;_id&quot;: &quot;623d7d6a8165d46a516d203b&quot;,<br>      &quot;id&quot;: &quot;tt18969216&quot;,<br><br>     &quot;primaryImage&quot;: null,<br>      &quot;titleType&quot;:<br>{<br>        &quot;text&quot;: &quot;Movie&quot;,<br>   <br>    &quot;id&quot;: &quot;movie&quot;,<br>       <br>&quot;isSeries&quot;: false,<br>        &quot;isEpisode&quot;: false,<br>  <br>     &quot;__typename&quot;: &quot;TitleType&quot;<br>      },<br><br>     &quot;titleText&quot;: {<br>      <br> &quot;text&quot;: &quot;Spiderman unlimited the movie&quot;,<br>       <br>&quot;__typename&quot;: &quot;TitleText&quot;<br>      },<br>     <br>&quot;originalTitleText&quot;: {<br>        &quot;text&quot;: &quot;Spiderman unlimited the<br>movie&quot;,<br>        &quot;__typename&quot;: &quot;TitleText&quot;<br>   <br>  },<br>      &quot;releaseYear&quot;: {<br>   <br>    &quot;year&quot;: 2023,<br>       <br>&quot;endYear&quot;: null,<br>        &quot;__typename&quot;: &quot;YearRange&quot;<br>  <br>   },<br>      &quot;releaseDate&quot;: {<br>  <br>     &quot;day&quot;: 10,<br>      <br> &quot;month&quot;: 11,<br>        &quot;year&quot;: 2023,<br> <br>      &quot;__typename&quot;: &quot;ReleaseDate&quot;<br>     <br>}<br>    }</span></font><br><div><font face="Lato, sans-serif"><span style="white-space: pre;"><br></span></font></div><div><font face="Lato, sans-serif"><span style="white-space: pre;"><b>Fields<br>I will be using :</b></span><br></font></div><div><ul><li><font face="Lato, sans-serif"><span style="white-space: pre;"><b>id    <br>            <br> </b>(<i>To check that data is loaded from API or generated manually</i>)</span></font></li><li><font face="Lato,<br>sans-serif"><span style="white-space: pre;"><b>title          <br>     </b>(<i>This is the field which contains the title<br>or say name of movies or any other category of entertainment</i>)</span></font></li><li><font face="Lato, sans-serif">&lt;span<br>style=&quot;white-space: pre;&quot;&gt;<b>titleType        </b>(<i>This is Category of<br>title</i>)</span></font></li><li><font face="Lato, sans-serif"><span style="white-space: pre;"><b>releaseDate  </b>(<i>I can use this to sort my<br>data and releaseDate is one of the most imported piece of data in<br>terms of any movie or show</i>)</span></font></li><li><font face="Lato, sans-serif"><span style="white-space: pre;"><b>imageUrl   <br>   </b>(<i>This can be used to display images in UI</i>)</span></font></li></ul></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> How will you use the mapped data?</td></tr>
<tr><td> <em>Response:</em> <p>Users can log in and then search for movies they like, they can<br>create a personal list as a watch-later or say favorite.<div>Data will be fetched<br>by Admin Only,</div><div>No fixed but I will try to create a page in<br>which users can request movies to be added to the list.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.06.21image.png.webp?alt=media&token=3e3f2c46-714b-43de-82b0-278b4b194a1d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form With Valid data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.06.39image.png.webp?alt=media&token=167caae8-a2c0-41d3-8017-63a9d3a3c6b3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success Message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.07.58image.png.webp?alt=media&token=987705e4-c4a7-4496-92bf-506d0ece2a43"/></td></tr>
<tr><td> <em>Caption:</em> <p>Duplicate Handling<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.09.17image.png.webp?alt=media&token=b0f8e312-d6ea-473d-b78b-89ed4790d6ff"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.10.12image.png.webp?alt=media&token=13fe19b7-bee8-4d6f-bef0-1d545ccbb1af"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Logic Code, duplicates are handled by checking if data already persists in<br>the database with the given data or not.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.13.49image.png.webp?alt=media&token=7923aca3-2014-475f-b6b6-572d55f8f64f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database With correct data stored in and my UCID is visible<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/43/">https://github.com/denilayush/dj325-is601-007/pull/43/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.24.05image.png.webp?alt=media&token=b04bcb5e-c656-4c39-9416-822946c19255"/></td></tr>
<tr><td> <em>Caption:</em> <p>The first two are custom records and the others are API-Bases, the custom<br>records don&#39;t have API ID<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.27.52image.png.webp?alt=media&token=499d15d0-d5d6-48cb-b9cf-6126a2b6c2b7"/></td></tr>
<tr><td> <em>Caption:</em> <p>filters are Name: tiger, Type: Movie, Sorting: Title( Low to High ) and<br>Limit: 10.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.37.02image.png.webp?alt=media&token=d7771d41-f049-49e0-a36e-e562969378bc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Handled from the server side as well as in forms.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.38.26image.png.webp?alt=media&token=613a57de-3593-4748-ac0b-77fdff7cf096"/></td></tr>
<tr><td> <em>Caption:</em> <p>With proper Links in each row.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.39.05image.png.webp?alt=media&token=1449171d-4e44-4690-935a-df7acbf1c5b8"/></td></tr>
<tr><td> <em>Caption:</em> <p>No Data Found.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/45">https://github.com/denilayush/dj325-is601-007/pull/45</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.43.13image.png.webp?alt=media&token=5c41a9c6-6b13-4d7e-a4a2-92f17f950223"/></td></tr>
<tr><td> <em>Caption:</em> <p>View Page UI.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.43.17image.png.webp?alt=media&token=9837f496-bf34-4bac-93b7-0548cc8b9a7d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error Id<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/46">https://github.com/denilayush/dj325-is601-007/pull/46</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/44">https://github.com/denilayush/dj325-is601-007/pull/44</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.44.58image.png.webp?alt=media&token=c211d6a3-cf0e-4b6c-a71e-0656d8a4f036"/></td></tr>
<tr><td> <em>Caption:</em> <p>Prefilled Values.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.53.24image.png.webp?alt=media&token=48dd7ee8-8dc3-43de-bcdd-129216600f25"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.47.55image.png.webp?alt=media&token=a69829b9-4e15-46cb-9e85-d3a2c0e5f79b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validations.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.48.04image.png.webp?alt=media&token=42f18ef7-b784-4e6e-b774-d92f03b477fb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validations.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.48.10image.png.webp?alt=media&token=ff54d918-de0f-4d72-bb2b-720dec9620c1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validations.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.55.47image.png.webp?alt=media&token=80d74226-c814-42b7-9344-e5e80c811916"/></td></tr>
<tr><td> <em>Caption:</em> <p>Datebase Before.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.55.52image.png.webp?alt=media&token=5741a8f1-8fc4-4063-91d9-4a743dead6a8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Datebase After.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/48">https://github.com/denilayush/dj325-is601-007/pull/48</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T04.58.55image.png.webp?alt=media&token=48ffd629-caac-4be7-bf8e-bfb8ab54ca92"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for this delete logic.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T05.03.10image.png.webp?alt=media&token=bf059ab6-1cda-4c32-9327-42d3fea985b7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T05.03.12image.png.webp?alt=media&token=716f43cf-783d-4179-9283-83df24065883"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deleting.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T05.03.16image.png.webp?alt=media&token=80785624-ebd6-4507-92f1-dd8944b6895a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deletion.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T05.03.21image.png.webp?alt=media&token=b4e44a47-8320-4abb-bbab-a7223c3c0717"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deletion.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/51">https://github.com/denilayush/dj325-is601-007/pull/51</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T05.07.53image.png.webp?alt=media&token=1a0a82c3-1891-47f7-8a47-213e26a37252"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data fetching and insertion logic.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T05.09.19image.png.webp?alt=media&token=c17ef4b8-6499-4535-9d42-175e7de12cc4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sql Unique API id column.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T05.09.22image.png.webp?alt=media&token=69b99392-f5e4-4c26-8b2c-f7e7f11857de"/></td></tr>
<tr><td> <em>Caption:</em> <p>API Setup.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <div><b>Route Definition:</b></div><div>The function is accessed via a GET or POST request to "/fetch".</div><div><br></div><div><b>Permission<br>Check:</b></div><div>This function requires admin permission to execute, which is enforced by the @admin_permission.require(http_exception=403)<br>decorator.</div><div><br></div><div><b>Form Validation:</b></div><div>It first validates a form (movieSearchForm()) submitted through the request.</div><div><br></div><div><b>Movie Data Retrieval:</b></div><div>Utilizes<br>an external module (movies.get_movie) to retrieve movie data based on the submitted form<br>data.</div><div><b><br></b></div><div><b>Processing Retrieved Data:</b></div><div>If movie data is found (result['results']), it formats the data and<br>inserts it into the database using an INSERT statement with an ON DUPLICATE<br>KEY UPDATE clause to avoid duplicates.</div><div><b><br></b></div><div><b>Flash Messages:</b></div><div>Provides flash messages to the user interface<br>based on the outcome of the data retrieval and insertion process.</div><div><b><br></b></div><div><b>Error Handling:</b></div><div>Catches exceptions<br>that might occur during the process and generates appropriate flash messages to indicate<br>any errors.</div><div><b><br></b></div><div><b>Render Template:</b></div><div>Finally, it renders a template (movie_search.html) with the form data to<br>facilitate further user interactions.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/43">https://github.com/denilayush/dj325-is601-007/pull/43</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learning:<div>How to fetch data from API.</div><div>What are the endpoints.</div><div>Data transformation.</div><div>SQL Table Creation. (Understanding<br>the Schema and associations)</div><div>User Control. (Access control to a route or buttons)</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dj325-prod-e4b2f4589d51.herokuapp.com/movies/list">https://is601-dj325-prod-e4b2f4589d51.herokuapp.com/movies/list</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T05.16.46image.png.webp?alt=media&token=6970b971-9892-41b3-b177-fb3a9f96e196"/></td></tr>
<tr><td> <em>Caption:</em> <p>WakaTime<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T05.16.50image.png.webp?alt=media&token=5948c24a-33f3-40a0-a26d-3da23bb99e37"/></td></tr>
<tr><td> <em>Caption:</em> <p>WakaTime bubble chart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-11-28T05.16.54image.png.webp?alt=media&token=f85378ee-fdd7-4740-a11e-8794fa80eccd"/></td></tr>
<tr><td> <em>Caption:</em> <p>WakaTime branch time list.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/dj325" target="_blank">Grading</a></td></tr></table>