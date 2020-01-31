[![Build Status](https://travis-ci.org/stiofanEimeid/graphic-design-services.svg?branch=master)](https://travis-ci.org/stiofanEimeid/graphic-design-services)

![Python](https://img.shields.io/badge/python-3.6.9-%2333AAFF)

![Django](https://img.shields.io/badge/django-2.2.6-092E20) 

<div align="center">
 <a href="https://sb-graphic-design-services.herokuapp.com/" target="_blank" rel="noopener"><img src="https://github.com/stiofanEimeid/graphic-design-services/blob/master/project/static/images/AODLogo.png" alt="Agents of Design Logo"/></a>
 
 <h1 align="center">
 Agents of Design
 </h1>
 
</div>

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

'Agents of Design' is an e-commerce site that sells graphic design services. It provides hand-drawn illustrations as well as hand drawn assets for websites to add a dose of creativity and authenticity to a customer's brand.. 

This site is my submission for the fourth and final milestone of the Code Institutes Full Stack Software Development Diploma, as part the Full Stack Frameworks module.

#### User Goals

This site is targeted at businesses who are in the market for art assets for their website along with users who are interested in purchasing art for their own personal enjoyment. 

**User Goals are to**:
- Order a design to their specifications and be able to request revisions to a design if necessary. 
- View previous work of the artist. 

Agents of Design is the perfect way to meet these needs as it provides the functionality and ease-of-use to request and purchase the right design, while providing a straightforward process was requesting changes should they be necessary.

Users are view the site gallery to see the artist’s previous work to determine whether they would be interested in purchasing a design.

#### User Stories

As a user, I want to be able to:

- **_view previous work and customer testimonials without having to log in;_**
- **_Create a password protected profile with associated username and image;_**
- **_Update profile details;_**
- **_use a form to order a design to fit my needs;_**
- **_view how much my request will cost;_**
- **_pay using a secure checkout process;_**
- **_Keep track of my purchases and order history from my profile;_**
- **_accept the result or request a round of changes._**
- **_write a testimonial for the design._**

As a site owner, I want to:

- **_showcase prior work to attract potential clients;_**
- **_log in as a special user in order to see a list of all orders submitted by customers;_**
- **_upload completed work._**
- **_View requested changes to designs submitted by users;_**
- **_Upload an updated design to the site viewable by users;_**
- **_receive payment for orders and designs._**


### Design Choices

 ***
 
#### Name

'Agents of Design' is a concept created for the site in which it is reimagined as a group of secret agents selling their services, in this case illustrations rather than anything espeically nefarious. The idea was to make the brand memorable with a concept that was fun and out of the ordinary.

#### Logo

The logo consists of two hands using fingerguns (index and middle finger extending) coming together to form a picture frame. My intention was to evoke the spy theme, with two individuals involved in a playful shootout, while conveying the purpose of the site: to sell images based on the vision of customers. 

#### Fonts

I used the fonts "Special Elite" and "Roboto". Special Elite is a typewriter font that also ties into the spy theme of the website, giving the user the impression they are reading the header of a special document or the like. Roboto was chosen to compliment the stylised "Special Elite" font. It is clear and easy to read and more approrpriate for users reading large blocks of text.

#### Colours

| Eerie Black | White | Jasmine Carmine | Columbia Blue |
| :---: | :---: | :---: |  :---: | 
| ![#1a1a1a](https://placehold.it/15/1a1a1a/1a1a1a) | ![#FFF](https://placehold.it/15/FFF/FFF) | ![#993333](https://placehold.it/15/993333/993333) | ![#C1CFDA](https://placehold.it/15/C1CFDA/C1CFDA)| 
| #1a1a1a | #FFF| #99333 | #C1CFDA |

### Wireframes

Wireframes were created using Balsamiq and may be viewed in the [wireframes folder](https://github.com/stiofanEimeid/graphic-design-services/tree/master/wireframes). 

## Features

### Existing Features

#### Users

Users may register a profile on the site by providing a username, email and password. Upon successfully creating an account they will be able to set a profile picture and update their account details. 

In addition, registered user’s purchase history and associated designs will be available to view from their profile. 

#### Password Reset

Users may reset their password by clicking the relevant link on the login page. An email is sent to the account with which the user registered their account.

#### Orders

With an account, users may submit a request for an order, revisions to that order, accept a design and write a testimonial for that design. 

In order to submit a request for a design, users must fill out a form. This includes specifying the type of the design they want as well as a description of what it would feature. 

A Javascript calculator displays a quote based on user input using an AJAX call. Once users are happy with their order, they may submit the form and proceed to checkout. Payment functionality has been implemented using the Stripe API. 

#### Order List

The Order List provides a list of all open orders as well as a list of revisions to designs submitted for approval. It is only viewable by the superuser. Clicking on any one of these individual orders will take the superuser to a detailed view of the order and revision and the option to submit a design based on the order or revision.

#### Design Submission

A list of open orders is available to view by the admin only. From this list, the admin may select an item and be taken to a detailed view of that item. From that detailed view, the admin may then submit a design to fulfil the order, including source code and a preview image. Once these have been submitted, the user may view this submission from their profile. They may either accept the design, in which case the process is considered finished, or they may request a round of changes. 

#### Revisions

If the user is not satisfied with the design, they may fill out a revision form specifying their requested changes to the design. They will be brought to a payment page similar to the payment page for the initial order and charged a small fee that is a fraction of the original cost of the design in order to receive a design with their requested changes.

The admin may view a list revisions requested by users under orders on the order list. Similarly, they may select an individual detail page, from which they may submit an updated version of the design. 

Once this updated design has been submitted, users may view it from their profile. They may accept the design, ending the process, or request another round of changes, restarting the revision process.  

#### Gallery

Once the user has accepted the design, the process ends. A snapshot of the work is then made viewable by everyone in the website gallery and users are given the option of writing a testimonial to be displayed alongside the work. 

#### Order Calculator

As the user fills out the order form, a javascript calculator provides a quote. The same formula is used to determine the price on the server so that the price cannot be manipulated by the user.

#### Navigation

The navbar is accessible from every page of the site although its contents change depending on whether the user is registered and logged into their account. 

If the user is not registered or logged in, the navbar options will be the following:

- **Home**
- **Gallery**
- **Order**
- **Login**
- **Register**

If they are logged in, these options will be supplemented by the following with the option to login/register removed:

- **Home**
- **Gallery**
- **Order**
- **Profile**
- **Logout**

It will also indicate who the user is logged in as along with a visual identifier or which page the user is currently viewing on the site. 

When the superuser is logged in, a link to the order list will be added to the navbar. 

- **Order List**

### Features left to implement 

I would like to implement a reward system for users who write testimonials for completed works in order to incentivise engagement with this aspect of the site. 

This reward will take the form of a discount on the next purchase of a user who completes a testimonial on a purchased design. 

I would like to include pagination on the profile page or incorporate ajax calls when a user's list of orders/designs becomes too long.

Additionally, I would also like to give users the option of deleting their profile.

Finally, I would like to incorporate the ability for users to download images directly by clicking on a button for the sake of convenience.

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
- [Clip Art Studio](...)
    - The application Clip Art Studio was used to create art content. Images were created with the aid of a Wacom tablet.

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

Using an IDE of your choice, ensure the following are installed, Git, PIP and Python3.

It is advised that you create and work within a virtual environment in your IDE of choice for this project. 

#### Running the Site in your IDE

It is advised that you create and work within a virtual environment in your IDE of choice for this project.

- Save this repository by clicking the clone or download button located at the top of the front page of this repository.
    - Alternatively, having installed Git locally, clone the repository with the command `git clone https://github.com/stiofanEimeid/graphic-design-services.git`

- From the Command Line Interface, navigate to the project directory where the extracted files are located. 

- Create env.py file within the project directory to hold sensitive environment variables such as the secret key. 

- Install project requirements from the requirements.txt file with the command 
`pip –r requirements.txt`.

- Run the server and view a live version of the site with the command `python manage.py runserver`. If you do not have permission to view the site on your local host, add the address to the list of allowed hosts in the settings.py file located in the graphic-design-services app. 

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

- Static files cannot be hosted on Heroku. You will therefore need to create an S3 bucket to serve static files and connect this to your project. Sign up for a free account at Amazon Web Services by going to .... and following the instructions provided.
- Navigate to the managament console and search for the S3 service (Simple Storage Service).
- Create a new bucket for your project.
- In your newly created bucket, click on the permissions tab and go to CORS configuration (Cross-origin Resource Sharing). Copy and paste the following into the section provided and save.

```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

**_Note about asterisk: Adding an asterisk to the_** `Allowed Origin` **_tag allows access from any domain but you may want to switch this to your final domain name in the future. _**

Next, navigate to IAM and create a new user. Select programmatic access. Give the user permission to access the bucket you have created. Under set permissions, select attach existing policies. Search for an S3 policy in the search bar and select AmazonS3FullAccess. Click next until you can create user. Take the key ID and secret access key and set them as environment variables. 

##### Stripe Functionality

- Finally, in order to allow for checkout functionality, you will need to include access to the Stripe API in your project. Go to [Stripe's website](https://stripe.com) and set up a free account. From the dashboard, find your API keys, the publishable key and the secret key. They will have the format `pk_test_<34-characters>` and `sk_test_<34-characters>` respectively. Set these as environment variables.

Having followed these steps, your project should be ready to deploy.

## Credits

Installing psycopg2 with a virtual environment help found at [goshawknest](https://web.archive.org/web/20140615091953/http://goshawknest.wordpress.com/2011/02/16/how-to-install-psycopg2-under-virtualenv/)

Guidance on how to display multiple models in a list view was found in this [Stackoverflow thread](https://stackoverflow.com/questions/31133963/multiple-models-generic-listview-to-template).

### Content

- The front page images including logo were designed and drawn by me.

### Acknowledgements 

- I found [Corey Schafer's videos](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) on setting up a Django authetification system of great help in this project.

- I also found Free Code Camps videos particularly helpful for understanding how Django operates.

### Code

- The solution to pushing a subdirectory to Heroku was found in this [Medium article](https://medium.com/@shalandy/deploy-git-subdirectory-to-heroku-ea05e95fce1f).

- The code for displaying the currently selected page in my sidebar was found in this [Stackoverflow thread](https://stackoverflow.com/questions/26819675/navbar-highlight-for-current-page).

- The code for the django form dropdown menu was found in another [Stackoverflow thread](https://stackoverflow.com/questions/24403075/django-choicefield/24404791).

- Finally, the styles used for submit buttons was taken from this [codepen](https://codepen.io/grbav/pen/GZXgVj).

- The SVG mouse found at the top of the site was initially found on page one, entry no. 3 of this [css animations page](https://www.creativebloq.com/inspiration/css-animation-examples)
which displayed code this codepen: [SVG mouse](https://codepen.io/matchboxhero/pen/gGdJYo "SVG mouse"). Minor changes were made in relation to positioning on the page.

### Disclaimer 

The contents of this website are for educational purposes only.

[**Jump to top &uarr;**](#table-of-contents)