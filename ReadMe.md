# Instagram

This python/django web-app was created as a clone of instagram.Developed during Moringa Core. This is Week 9's Independent Project.
Date: 9th November 2018
By: Donald Kiplagat

## Description
This web-app allows a user to create a Profile,add a Location and Post that are all under his username allowing other users to vote for them.

## Setup/Installation Requirements
* Live site can be accessed from the following link https://instagram-donald.herokuapp.com/
* Pre-configured Admin details are:
Password: halowars54611
Username: donaldkiplagat

### Known Bugs
* Elements re-arrange themselves unequally on different screen sizes.
* Panel with users list moves down on homepage when a new post is made

### Behaviour Driven Development
* The program should return all users posts on the home page<br>
Given:All posts<br>
When: Url is changed to home page<br>
Then: All Posts are displayed<br>

* Modal should be displayed when the user clicks on any post and have the post's details<br>
Given:A Post<br>
When: User cicks on the post <br>
Then: A modal with the post's details is displayed<br>

* Admin site should be displayed when "admin/" url is chosen<br>
Given: An admin url<br>
When: User enters admin url in browser<br>
Then: Admin Login is displayed<br>

* User authentication occurs when Admin tries to Login<br>
Given:Admin page is accessed<br>
When: User tries to login<br>
Then: User details are authenticated to confirm if user is an admin<br>

* User session should end when logout url is chosen<br>
Given:Logout option is given<br>
When: User chooses logout option<br>
Then: User session is ended<br>


### Technologies Used
* Atom was the source code editor of choice.
* Git and Github were used as my local and online repositories respectively.
* Django was used as the framework of choice
* Heroku was used in deploying the live site


### Support and contact details
* Contact me through my email: donald.k.kiplagat@gmail.com
* The source code is also contained within the folder containing this ReadMe with comments on the code thus third-party support can be offered.

### License
Moringa School
Copyright (c)2018 **Instagram by Yours Truly-Donald Kiplagat**
