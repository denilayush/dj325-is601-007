<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 API Project</td></tr>
<tr><td> <em>Student: </em> Denil Jain (dj325)</td></tr>
<tr><td> <em>Generated: </em> 12/2/2023 6:41:02 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/dj325" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Data Association </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> How will this data relate to the User</td></tr>
<tr><td> <em>Response:</em> <p>I am using <b>Movie API</b>,&nbsp;<div>Users will able to perform these tasks:<br><ul><li>See the list<br>of movies</li><li>Filter the list with their name, and release date, user can LIMIT<br>the list.</li><li>Users will have a page to check movies that they have added<br>to their watchlist</li><li>Admin will have a page to see relations and Admin can<br>add and remove the movies from any user&#39;s watchlist.</li></ul></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Data changes</td></tr>
<tr><td> <em>Response:</em> <p>Yes, it automatically &quot;updates&quot;, When Movie data is changed, all the users will<br>see the new data.<div>It is a &quot;one-to-many&quot; relationship, one movie can be on<br>many people&#39;s watchlists.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how/where the user can associate the data with themselves</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T20.32.41image.png.webp?alt=media&token=4ae6677c-ea1d-4c5a-b623-f12398688e0a"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the page from users can check the list of movies.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T20.32.46image.png.webp?alt=media&token=21b7770c-15e2-4ee3-b4b3-3c71f9389574"/></td></tr>
<tr><td> <em>Caption:</em> <p>After that users are redirected to this page then they can add that<br>movie to their watchlist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T22.18.17image.png.webp?alt=media&token=aae851a6-189b-45d6-ba77-ac1975fce835"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for the associate(this will insert movie_id and user_id in the DB).<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> List Associated Entities to the logged in user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the page where a user can list related/associated entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T22.25.33image.png.webp?alt=media&token=24f1dca9-fc42-4978-944f-ef4be745d5bb"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is logged in the user&#39;s watchlist (without filter).<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T22.25.57image.png.webp?alt=media&token=8a43b093-a65f-4b94-a823-27fe1db53131"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is logged in the user&#39;s watchlist (with filter).<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T22.26.23image.png.webp?alt=media&token=763c7314-a722-42bf-8f31-11eb7c804047"/></td></tr>
<tr><td> <em>Caption:</em> <p>table heading with a total count of associations of the user, the count<br>of movies listed on a page, and a button to remove all the<br>watchlist items.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T22.26.42image.png.webp?alt=media&token=9832c3cd-822c-4464-b58e-36346bf59a8d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users can remove individual movies from the list.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/62">https://github.com/denilayush/dj325-is601-007/pull/62</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List entities associated with users </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a page that lists entities that are associated with at least 1 user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T23.00.58image.png.webp?alt=media&token=2d480284-2c4b-4804-9e98-387e9443f9b4"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is admin only page to list all the associations (Without any filter).<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T23.02.34image.png.webp?alt=media&token=3bb845f8-c27d-4408-ab78-bb4002f1a520"/></td></tr>
<tr><td> <em>Caption:</em> <p>Applied filter on title and limit.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T23.03.20image.png.webp?alt=media&token=82ce284a-cb9a-4281-9f5a-5452a89b6f99"/></td></tr>
<tr><td> <em>Caption:</em> <p>Applied filter on username.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T23.00.09image.png.webp?alt=media&token=2e222426-6520-4b10-8193-93e86020cac9"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is with both username and title.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/63">https://github.com/denilayush/dj325-is601-007/pull/63</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin Association Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Admin page to search for users and entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T23.06.30image.png.webp?alt=media&token=eb169a31-16b1-49c2-89d8-142b6aed92d6"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the page for admin with two search fields (partial match) Admin<br>can associate any movie with any user (that can be adding a movie<br>to a watch list or removing from a list).<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T23.06.53image.png.webp?alt=media&token=a7c8cba4-01cd-4e8e-8e4b-750f394b77c3"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a flash message after assigning the movie &quot;She-Hulk&quot; to user &quot;Jay&quot;.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/63">https://github.com/denilayush/dj325-is601-007/pull/63</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Project Related Screens not yet shown </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of other pages not yet shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T23.10.27image.png.webp?alt=media&token=7d08b050-09c7-4bc6-afc5-346a9fde3339"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin can view all user&#39;s profiles which will show these fields of a<br>user &quot;username&quot;, &quot;created&quot; and &quot;modified&quot;.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fdj325%2F2023-12-02T23.12.33image.png.webp?alt=media&token=5a060b84-6c75-498e-bfe2-a4e03f152c6e"/></td></tr>
<tr><td> <em>Caption:</em> <p>The movie&#39;s detailed view page will display the details and a button to<br>add or remove this movie from his watchlist according to the user&#39;s watchlist.<br>if it is already in the watch list then the user will see<br>a button to remove it or else a button to add it.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain each screen shown above</td></tr>
<tr><td> <em>Response:</em> <div><b>Associate:</b></div><div><b>Functionality</b>: Allows users to associate movies with their account's watchlist.</div><div><b>Logic:</b></div><div><ul><li>Displays a list of<br>movies available for association.</li><li>He can view the detailed page for it</li><li>which will redirect<br>the user to the movies view page which will have these functionalities:</li><ul><li>Users can<br>select movies to add or remove them from their watchlist.</li><li>Admin can delete from<br>this page or can go to edit route</li></ul></ul></div><div><b>Watch Page:</b></div><div><b>Functionality:</b> Displays the user's watchlist<br>of associated movies.</div><div><b>Logic:</b></div><div><ul><li>Lists movies associated with the user's account.</li><li>Provides filtering options (like title,<br>type, and release date) to refine the watchlist.</li><li>this page has a button to<br>remove all the movies from the watch list and a button to remove<br>a single movie at a time.</li><li>page shows the total movies in the list<br>as well as on the page.</li></ul><div><br></div><b>Associated and Not Associated Pages:</b></div><div><b>Associated Page Logic:</b></div><div><ul><li>Admin only</li><li>Lists<br>movies associated with users.</li><li>Includes details about each association, such as movie title, username,<br>count, etc.</li><li>by clicking username admin can see the user's data.<br></li><li><div><blockquote style="margin: 0 0<br>0 40px; border: none; padding: 0px;"><b>View Profile Page:<br></b><b>Functionality:</b>&nbsp;Displays user profile information.<br><b>Logic:</b></blockquote></div><div><ul><ul><li>Shows user details<br>like username, creation date, modification date, etc.</li><li>Typically used by admins to view user-specific<br>information.</li></ul></ul></div></li><li>admin can remove the particular association of the user.</li></ul></div><div><b>Not Associated Page Logic:</b></div><div><ul><li>Admin Only</li><li>Lists<br>movies that have no associations with any user accounts.</li><li>Provides options for filtering movies<br>based on criteria like title, type, date, etc.</li></ul><b>Assign Page:</b></div><div><b>Functionality:</b> Allows admin to assign<br>movies to specific users.</div><div><b>Logic:</b></div><div><ul><li>Provides a form to select users and movies for assignment.</li><li>Admins<br>can choose users and movies and associate them.</li><li>users are listed using a partial<br>filter by username and then it lists all the movies associated with it<br>and whether they are active or not.</li></ul></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/65">https://github.com/denilayush/dj325-is601-007/pull/65</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/64">https://github.com/denilayush/dj325-is601-007/pull/64</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/63">https://github.com/denilayush/dj325-is601-007/pull/63</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/denilayush/dj325-is601-007/pull/62">https://github.com/denilayush/dj325-is601-007/pull/62</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I was not getting the WTforms error on the edit movie page, because<br>after clicking on the submit button it loaded a new form instead of<br>the last submitted form. So, I spent some time in the documentation of<br>WTforms, but after some trials, I asked the professor on Discord, and he<br>mentioned that each time that form is reloaded, I added a condition to<br>not load a new page if that submitted form has an error on<br>validation.<div><br></div><div>I spent my time making the back button&#39;s routes work perfectly, so if<br>the user clicks on the back button then it should go to the<br>page from where he accessed that page, this was mostly for the movie<br>view page because users had access to this page multiple routes.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/dj325" target="_blank">Grading</a></td></tr></table>