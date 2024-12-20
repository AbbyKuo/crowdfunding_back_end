# Crowdfunding Back End
Abby Kuo

## Planning:
### Concept/Name
BookWish is designed to bring communities together by enabling people to donate books to organisations in need. Schools, child cares, churches, and local communities can create projects, set a goal for the number of books they need, and connect with individuals who want to help them reach their goal.

### Intended Audience/User Stories
- As a user, I want to be able to create an account
- As a user, I want to be able to see my account details
- As a user, I want to be able to create a project
- As a user, I want to be able to pledge to a project
- As a user, I want to be able to update and delete my account 
- As a supporter, I want to be able to see the list of all my pledges
- As a supporter, I want to be able to update my comment and anonymous status 
- As a support, I want to be able to see all the other people that pledged to the project and how many books the organisation has received 
- As a project owner, I want to see my project details 
- As a project owner, I want to be able to update and delete my project
- As a project owner, I want to be able to see how many books I have received 
- As a superuser, I want to be able to see a list of all the user
- As a superuser, I want to be able to see a list of all the pledges 

### Front End Pages/Functionality
- Home page
    - If I'm new, a link to create a user profile
    - A link to my user profile 
    - A link to create a project 
    - A list of the top 6 projects 
    - A list of 3 new projects
- Project details page
    - Has the picture and story/description about the project
    - Has a list of users who pledge to the project 
    - Shows how many books has been received
    - If I'm not the owner, has a way to pledge to the project
    - If I'm the project, has a way to edit the project details and delete the project
- Create project page
    - Has a way to upload a picture
    - Has a place to include project title, story/description and goal
- User profile page
    - My details like name, email
    - A list of all my pledges 
    - Has a way to update my details like email, mobile
    - Has a way to delete my account 
  
### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
| /projects/ | GET | Return all projects. | N/A | 200 | N/A |
| /projects/ | POST | Create a new project | Project object | 201 | Must be logged in. |
| /projects/1/ | GET| Return the project with the id of "1". | N/A | 200 | NA|
| /projects/1/ | PUT | Update the project with the id of "1". | Project object | 200 | Must be logged in. Must be the project owner. |
| /projects/1/ | DELETE | Delete the project with the id of "1". | N/A | 200 | Must be logged in. Must be the project owner or admin user. |
| /pledges/ | POST | Create a new pledge. | Pledge object | 201 | Must be logged in. Must not be the project owner. |
| /pledges/1/ | GET | Return the pledge with the id of "1". | N/A | 20O | N/A |
| /pledges/1/ | UPDATE | Update the pledge with the id of "1". | Pledge object | 20O | Must be logged in. Must be the pledge owner. |
| /pledges/1/ | DELETE | Delete the pledge with the id of "1". | N/A | 20O | Must be logged in. Must be the pledge supporter. |
| /users/ | GET | Return all users. | N/A | 200 | Must be logged in. Must be admin users. |
| /users/ | POST | Create a new user. | N/A | 200 | N/A |
| /users/1/ | GET | Return the user details with the id of "1". | N/A | 200 | Must be logged in.  Must be the account owner or admin users.|
| /users/1/ | PUT | Update the user details with the id of "1". | N/A | 200 | Must be logged in. Must be the account owner or admin user. |
| /users/1/ | DELETE | Delete the user details with the id of "1". | N/A | 200 | Must be logged in. Must be the account owner or admin user.|
| /users/1/pledges/ | GET | Return the user's pledge list with the id of "1". | N/A | 200 | Must be logged in. Must be the supporter of the project. |


### DB Schema
![DB schema](./imgs/erd.png)

### Screenshots
1. A successful GET method
   ![A successful GET method](./imgs/get_user_detail.png)
2. A successful POST method
   ![A successful POST method](./imgs/create_a_project.png)
3. A successful token being returned
   ![A successful token being returned](./imgs/token_return.png)

#### How to register a new user and create a new project
1. Create User
   ![create user](./imgs/create_new_user.png)
2. Sign in User
   ![Sing in user to get a token](./imgs/get_user_token.png)
3. Create Project 
   ![json body for creating a project](./imgs/create_project_body.png)
   ![Auth token for creating a project](./imgs/create_project_token.png)

