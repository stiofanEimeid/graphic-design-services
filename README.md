[![Build Status](https://travis-ci.org/stiofanEimeid/graphic-design-services.svg?branch=master)](https://travis-ci.org/stiofanEimeid/graphic-design-services)

![Python](https://img.shields.io/badge/python-3.6.9-%2333AAFF)

![Django](https://img.shields.io/badge/django-2.2.6-092E20) 

# Phantistry - A SERVICE FOR ALL THE GRAPHIC DESIGN NEEDS YOU CAN THINK OF AND MORE

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

Phantistry is an e-commerce site that provides graphic design services. It provides hand-drawn illustrations as well as hand drawn assets for websites to add a dose of creativity and authenticity to a brand. 

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

Light Sky Blue #8ECAF9
Mint Cream #F7FFF6
Eerie Black #1D1E18
Light Carmine Pink #EF626C
Hansa Yellow # E9D758
Ube #8377D1

#### Format

### Wireframes

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

The carousel was built using the JS library, Swiper.js. Each slide takes the form of a side of a block. The block may be rotated to view more sides or slides. Each slide represents a different type of work, icon, logo or illustration. Each side is comprised of three images laid alongside one another that may be clicked on viewed on a individual detail page, along with details of the image and a testimonial if a user has made one available. 


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

#### Cloning from Github

In order to run a repository locally, the repository must be cloned. To clone the repository
:
1. Follow the link to the [Graphic Design Services repository](https://github.com/stiofanEimeid/graphic-design-services).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your preferred IDE, open the terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.
```console
git clone https://github.com/USERNAME/REPOSITORY
```
7. Press Enter. Your local clone will be created.

Further reading and troubleshooting on how to clone a repository from GitHub may be found [here](https://help.github.com/en/articles/cloning-a-repository).

To cut ties with this repository, type ```git remote rm origin``` into the terminal of your editor. In order to verify the terminal has been removed, type ```git remote -v``` to determine which remotes are still connected. 

#### Running the Site in your IDE

Create virtual environment with command virtualenv . (Python3)

Activate virtual environment with command source bin/activate

Install django (version?)

Create directory 'src' with mkdir src command

Navigate to src directory with cd src command

Create project with django-admin startproject graphic_design_services  . command

Add server to allowed hosts in settings.py

Run using command python manage.py runserver $IP:$PORT

Add command as string as alias in .bashrc

Run

#### Deploying the Project to Heroku

Login to Heroku through the CLI

Create an app.

Create a PostgresSQL database.

Add environment variables.

Add the Heroku App Domain name to the list of allowed hosts in settings.py

Upload the project subdirectory using the command ```git subtree push --prefix project heroku master``` (where project is the name of the folder containing the app) from the root directory.

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

### Disclaimer 

The contents of this website are for educational purposes only.



[**Jump to top &uarr;**](#table-of-contents)

