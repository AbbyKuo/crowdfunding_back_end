# Crowdfunding Back End
Abby Kuo

## Planning:
### Concept/Name
BookWish is a crowdfunding platform designed to bring communities together by enabling people to donate books to organisations in need. Schools, child cares, churches, and local communities can create projects, set a goal for the number of books they need, and connect with individuals who want to help them reach their goal.

### Intended Audience/User Stories
Our platform is designed for community-driven individuals who believe in the power of education and reading. The target audience includes parents, educators, philanthropists, book lovers, charities and anyone passionate about helping schools, child cares, churches, and local communities improve access to reading materials for children and families.

Organisations such as schools or local groups will be able to create a profile, share their mission, and set up specific book donation projects with clear goals. Individuals looking to contribute can browse through various projects, learn about the organisations' needs, and choose how many books they wish to donate. (Donors can track the impact of their contribution and share their involvement to encourage others.)

### Front End Pages/Functionality
- Home
    - Log in to user account 
    - Create a project 
    - Pledge to a project 
- Projects
    - Create a project
    - Pledge to a project
    - Update pledge description 
    - Show all supporters
    - Delete a project 
- Pledges
    - Create a pledge
    - Update a pledge
    - Delete a pledge
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
| /projects/1/ | DELETE | Delete the project with the id of "1". | N/A | 200 | Must be logged in. Must be the project owner. |
| /pledges/ | POST | Create a new pledge | Pledge object | 201 | Must be logged in. |
| /pledges/1/ | GET | Return the pledge with the id of "1" | N/A | 20O | N/A |
| /pledges/1/ | UPDATE | Update the pledge with the id of "1" | Pledge object | 20O | Must be logged in. Must be the pledge owner. |
| /pledges/1/ | DELETE | Delete the pledge with the id of "1" | N/A | 20O | Must be logged in. Must be the pledge owner. |



### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )
```

An example API spec:  
![](./img/table.png)
