# Graphic Design Services - Testing Details

[Main README.md file](README.md)

## Table of Contents

1. [**Automated Testing**](#automated-testing)
    - [**Validation services**](#validation-services)
2. [**Client Stories Testing**](#client-stories-testing)
    - [**User Stories Testing**](#as-a-user-i-want-to)
    - [**Owner Stories Testing**](#as-an-owner-i-want-to)
3. [**Manual Testing**](#manual-testing)
    - [**Responsiveness**](#responsiveness)
    - [**Browser Compatibility**](#browser-compatibility)
4. [**Bugs discovered**](#bugs-discovered)
    - [**Solved bugs**](#solved-bugs)
    - [**Unsolved bugs**](#unsolved-bugs)
5. [**Further Testing**](#further-testing)

## Automated Testing

### Unit Tests

Automated tests were run for Users, Orders and Pages Apps. The respective tests for each may be found in each apps directory. 

I used coverage py to ensure that I had written tests for most if not all of each app's functionality, beyond built in Django views.
In order to test an app's coverage, I ran the command ```coverage run --source=<appname> manage.py test``` in the terminal. I then ran
```coverage report``` to provide a table of the results of the tests in the terminal, and finally ```coverage html``` to create a page
from which to view the results in the browser.

I also employed the use of the Travis continuation service to ensure each build of the project tested successfully.

### Validation services
The following validation services and linter were used to check the validity of the website code.
- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML.
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.
- [JSHint](https://jshint.com/) was used to validate JavaScript.
- [Esprima](https://esprima.org/demo/validate.html) was used to validate JS syntax.
- [PEP8](http://pep8online.com/) was used to ensure python code is PEP8 compliant.

## Client Stories Testing

I manually tested the project's functionality by signing up as a user and requesting a number of designs, revisions, approving designs and
writing testimonials.

As a user, I tested to see whether I could change my username, password and image across a number of accounts. I also made sure I could not access
admin specific features.

Finally, as an admin, I made sure I could access these admin-specific features including the order list and the ability to submit designs and revisions.

## Manual Testing

### Responsiveness

The application was tested on mobile phone (Oneplus6, iphone), laptop(Macbook Air), tablet(iPad) and desktop(Mac Desktop) in addition to Google Chrome devtools. 

The site is fully responsive - it's mobile, tablet, laptop and desktop-friendly.

### Browser Compatibility

The application was tested on Edge, Firefox, Google Chrome, Opera and Safari.

## Bugs Discovered

### Unsolved Bugs

In order to resize images users submitted as profile pictures, I included the following Pillow function found on a [Stackoverflow thread](https://stackoverflow.com/questions/14680323/django-getting-pil-image-save-method-to-work-with-amazon-s3boto-storage):

```
    # users/models.py

    from PIL import Image

    *******
    
    def save(self, *args, **kwargs):
        """PIL interrupts save process to resize image"""  
        super(Profile, self).save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image)
            if image.height > 300 or image.width > 300:
                size = (300, 300)
                image = Image.open(self.image)
                image.thumbnail(size, Image.ANTIALIAS) 
                fh = storage.open(self.image.name, "w")
                format = 'png' 
                image.save(fh, format)
                fh.close()
                super(Profile, self).save(*args, **kwargs)

```

Unfortunately, this led to a large of automated tests failing, with the error 'required parameter name not set'
appearing in travis although not in testing locally. Until this issue is resolved, I have decided not to include the function. Furthermore,
I understand that a lambda function may in fact be the more appropriate approach to take in light of the fact I am making use of Amazon's Web Services
to serve images.

[**Jump to top &uarr;**](#table-of-contents)