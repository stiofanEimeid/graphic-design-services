[![Build Status](https://travis-ci.org/stiofanEimeid/graphic-design-services.svg?branch=master)](https://travis-ci.org/stiofanEimeid/graphic-design-services)

![Python](https://img.shields.io/badge/python-3.6.9-%2333AAFF)

![Django](https://img.shields.io/badge/django-2.2.6-092E20) 

# Agents of Design - A SERVICE FOR ALL THE GRAPHIC DESIGN NEEDS YOU CAN THINK OF AND MORE

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User Goals**](#user-goals)
    - [**User Stories**](#user-stories)
    - [**Design Choices**](#design-choices)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Data Structure**](#data-structure)

4. [**Technologies Used**](#technologies-used)

5. [**Testing**](#testing)

6. [**Deployment**](#deployment)
    - [**How to Run Code Locally**](#how-to-run-code-locally)

7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

## UX

#### Project Goals

'Agents of Design' is an e-commerce site that provides graphic design services. It provides hand-drawn illustrations as well as hand drawn assets for websites to add a dose of creativity and authenticity to a brand. 

This site serves as my submission for the fourth and final milestone of the Code Institutes Full Stack Software Development Diploma, as part the Full Stack Frameworks module.

#### User Goals

This site is targeted at businesses who are in the market for art assets for their website along with users who are interested in purchasing art for their own personal enjoyment. 

User Goals are:

Order a design to their specifications and be able to request revisions to a design if necessary. 

View previous work of the artist. 

Phantistry is the perfect way to meet these needs as it provides the functionality and ease-of-use to request and purchase the right design, while providing a straightforward process was requesting changes should they be necessary.

Users are view the site gallery to see the artist’s previous work to determine whether they would be interested in purchasing a design.


#### User Stories

As a user, I want to be able to:

- view previous work and customer testimonials without having to log in;
- Create a password protected profile with associated username and image;
- Update profile details;
- use a form to order a design to fit my needs;
- view how much my request will cost;
- pay using a secure checkout process;
- Keep track of my purchases and order history from my profile;
- accept the result or request a round of changes.
- write a testimonial for the design. 

As a site owner, I want to:

- showcase prior work to attract potential clients;
- log in as a special user in order to see a list of all orders submitted by customers;
- upload completed work.
- View requested changes to designs submitted by users;
- Upload an updated design to the site viewable by users;
- receive payment for orders and designs. 


### Design Choices

### Name

#### Fonts

#### Icons

#### Colours

| Light Sky Blue | Mint Cream | Eerie Black | Light Carmine Pink | Hansa Yellow | Ube |
| :---: | :---: | :---: |  :---: | :---: | :---: |
| ![#8ECAF9](https://placehold.it/15/8ECAF9/8ECAF9) | ![#F7FFF6](https://placehold.it/15/F7FFF6/F7FFF6) | ![#1D1E18](https://placehold.it/15/1D1E18/1D1E18) | ![#EF626C](https://placehold.it/15/EF626C/EF626C) | ![#E9D758](https://placehold.it/15/E9D758/E9D758) | ![#8377D1](https://placehold.it/15/8377D1/8377D1) |
| #8ECAF9 | #F7FFF6| #1D1E18 | #EF626C |#E9D758| #8377D1 |

#### Format

### Wireframes

Wireframes were created using Balsamiq and may be viewed in the [wireframes folder](https://github.com/stiofanEimeid/graphic-design-services/tree/master/wireframes). 

## Features

### Existing Features

#### Users

Users may register a profile on the site by providing a username, email and password. Upon successfully creating an account they will be able to set a profile picture and update their account details. 

In addition, registered user’s purchase history and associated designs will be available to view from their profile. 


#### Orders

With an account, users may submit a request for an order, revisions to that order, accept a design and write a testimonial for that design. 

In order to submit a request for a design, users must fill out a form. This includes specifying the type of the design they want as well as a description of what it would feature. 

A Javascript calculator displays a quote based on user input using an AJAX call. Once users are happy with their order, they may submit the form and proceed to checkout. Payment functionality has been implemented using the Stripe API. 

#### Design Submission

A list of open orders is available to view by the admin only. From this list, the admin may select an item and be taken to a detailed view of that item. From that detailed view, the admin may then submit a design to fulfil the order, including source code and a preview image. Once these have been submitted, the user may view this submission from their profile. They may either accept the design, in which case the process is considered finished, or they may request a round of changes. 

#### Revisions

If the user is not satisfied with the design, they may fill out a revision form specifying their requested changes to the design. They will be brought to a payment page similar to the payment page for the initial order and charged a small fee that is a fraction of the original cost of the design in order to receive a design with their requested changes.

The admin may view a list revisions requested by users under orders on the order list. Similarly, they may select an individual detail page, from which they may submit an updated version of the design. 

Once this updated design has been submitted, users may view it from their profile. They may accept the design, ending the process, or request another round of changes, restarting the revision process.  

#### Gallery

Once the user has accepted the design, the process ends. A snapshot of the work is then made viewable by everyone in the website gallery and users are given the option of writing a testimonial to be displayed alongside the work. 

#### Order Calculator


#### Navigation

The navbar is accessible from every page of the site although its contents change depending on whether the user is registered and logged into their account. 

If the user is not registered or logged in, the navbar options will be the following:

…

If they are logged in, these options will be supplemented by the following with the option to login/register removed:

…

It will also indicate who the user is logged in as along with a visual identifier or which page the user is currently viewing on the site. 


### Features left to implement 

I would like to implement a reward system for users who write testimonials for completed works in order to incentivise engagement with this aspect of the site. 

This reward will take the form of a discount on the next purchase of a user who completes a testimonial on a purchased design. 

## Technologies Used

### Languages

- This project uses HTML, CSS, JavaScript, and Python programming languages.

### Tools

- [Balsamiq](https://balsamiq.com/?gclid=CjwKCAjw2qHsBRAGEiwAMbPoDGWJ8Vt62S0dfo_Gtqbf5WdHzNWohvOch7nnGT7kxnWNIr85RsS2IxoCmwkQAvD_BwE)
    - **Balsamiq** was used to create the wireframes for this project.
- [Cloud9](https://c9.io) 
    -  **Cloud9** was used as the IDE for building the website.
- [Git](https://git-scm.com/)
    - **Git** was used to handle version control
- [GitHub](https://github.com/)
    - This project uses **GitHub** to store and share all project code remotely. 
- [Heroku](https://www.heroku.com/)
    - The application is hosted on **Heroku**.

## Testing

Information on the testing process may be found in the [testing.md file](https://github.com/stiofanEimeid/graphic-design-services/blob/master/testing.md). 

### Libraries

- [Bootstrap](https://www.bootstrapcdn.com/)
    - The project uses **Bootstrap** to simplify the structure of the website and make the website responsive.


## Deployment

This project was written using the AWS Cloud IDE.

Project code was pushed to Github and Heroku.

### How to Run Code Locally

In order to run this project locally, the following tools are needed.

Using an IDE of your choice, ensure the following are installed, Git, PIP and Python3...

It is recommended that you create a virtual environment that contains the project's dependencies, and keeps those dependencies separate from those of other projects. 


#### Running the Site in your IDE

<!--Create virtual environment with command virtualenv . (Python3)-->

<!--Activate virtual environment with command source bin/activate-->

<!--Run using command python manage.py runserver $IP:$PORT/Add command as string as alias in .bashrc-->


- Save this repository by clicking the clone or download button located at the top of the front page of this repository.
    - Alternatively, having installed Git locally, clone the repository with the command `git clone https://github.com/stiofanEimeid/graphic-design-services.git`

- From the Command Line Interface, navigate to the project directory where the extracted files are located. 

- Create env.py file within the project directory to hold sensitive environment variables such as the secret key. 

- Install project requirements from the requirements.txt file with the command 
`pip –r requirements.txt`.

- Run the server and view a live version of the site with the command python `manage.py runserver`. If you do not have permission to view the site on your local host, add the address to the list of allowed hosts in the settings.py file located in the graphic-design-services app. 

- Next, it will be necessary to populate the database with the proper tables. Run the command `python manage.py makemigrations` followed by the command `python manage.py migrate`. 

- In order to access the admin panel, run the command `python manage.py createsuperuser`. You will be prompted to enter a username, password and email.


#### Deploying the Project to Heroku

- In order to allow Heroku to install this project’s requirements, create a requirements.txt file with the command pip freeze > requirements.txt’ while you are in the project directory i.e. src/project.

- Create a Procfile in order to tell Heroku what type of application is being run. Enter the command `echo:web gunicorn main.wsgi:application > Procfile`.

- Sign in to your account or register a free Heroku account. Create an app and select ‘deploy’ at the top of the app page.

- Under the resources tab of your app, find the Add-ons section and search for Heroku Postgres and select Hobby for the level. This database will replace the locally generated sqlite database. Add the url provided as an environment variable to your env.py file along with the config vars under the settings tab of your app. 

- Add the rest of the environment variables found in your env.py file as config vars. 

- Having connected to a new database, you will be required to rebuild the tables you previously created in the local deployment section. Run the commands ‘python manage.py makemigrations’ and ‘python manage.py migrate’ again.

- Create a new superuser once again using the command ‘python manage.py createsuperuser’ and follow the instructions indicated. 
Upload the project subdirectory using the command `git subtree push --prefix project heroku master` (where project is the name of the folder containing the app) from the root directory.

##### Serving Images 

- Static files cannot be hosted on Heroku. You will therefore need to create an S3 bucket to serve static files and connect this to your project…

##### Stripe Functionality

- Finally, in order to allow for checkout functionality, you will need to include access to the Stripe API I your project…


## Credits

Installing psycopg2 with a virtual environment help found at [goshawknest](https://web.archive.org/web/20140615091953/http://goshawknest.wordpress.com/2011/02/16/how-to-install-psycopg2-under-virtualenv/)

https://stackoverflow.com/questions/31133963/multiple-models-generic-listview-to-template

### Content

### Media

### Code

<!--Custom Cursor by Stefan Kaltenegger found at [codrops](https://tympanus.net/codrops/2019/01/31/custom-cursor-effects/)-->

### Acknowledgements

Heroku fix: https://medium.com/@shalandy/deploy-git-subdirectory-to-heroku-ea05e95fce1f

currently selected page in navbar: https://stackoverflow.com/questions/26819675/navbar-highlight-for-current-page

Preview order modal: https://stackoverflow.com/questions/23775272/bootstrap-modal-before-form-submit

Django Form Dropdown Menu: https://stackoverflow.com/questions/24403075/django-choicefield/24404791

Button style: https://codepen.io/grbav/pen/GZXgVj

### Disclaimer 

The contents of this website are for educational purposes only.

[**Jump to top &uarr;**](#table-of-contents)

