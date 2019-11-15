[![Build Status](https://travis-ci.org/stiofanEimeid/graphic-design-services.svg?branch=master)](https://travis-ci.org/stiofanEimeid/graphic-design-services)

![Python](https://img.shields.io/badge/python-3.6.9-%2333AAFF)

![Django](https://img.shields.io/badge/django-2.2.6-092E20) 

# MILESTONE PROJECT 3

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

The goal of the project is to build a site to provide graphic and web design services. 

#### User Goals

As a user, I want to purchase graphical designs to address my needs.

As an owner, I want to showcase my work and earn money for freelance design work.

#### User Stories

As a user, I want to be able to:

- view previous work and customer testimonials;
- use a form to order a design to fit my needs;
- view how much my request will cost and how long it will take;
- accept the result or request a round of changes.

As a site owner, I want to:

- showcase prior work to attract potential clients;
- log in as a special user in order to see a list of all orders;
- upload completed work.

### Design Choices

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

Carousel

Calculator

### Features left to implement 

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

### Content

### Media

### Code

Custom Cursor by Stefan Kaltenegger found at [codrops](https://tympanus.net/codrops/2019/01/31/custom-cursor-effects/)

### Acknowledgements

### Disclaimer 

The contents of this website are for educational purposes only.



[**Jump to top &uarr;**](#table-of-contents)

