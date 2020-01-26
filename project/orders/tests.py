from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import OrderForm, RevisionsForm, TestimonialForm, DesignAcceptanceForm, DesignSubmissionForm, DesignUpdateForm
from users.models import User
from .models import Design, Order

# Create your tests here.

# Forms 

## Order Form
class TestOrderForm(TestCase):
    def test_order_form_valid(self):
        form = OrderForm({"type": "Icon",
                          "description": "description text here",
                        })
        self.assertTrue(form.is_valid())
        
    def test_order_form_invalid_type(self):
        form = OrderForm({"type": "",
                          "description": "description text here",
                        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["type"], [u"This field is required."])
        
    def test_order_form_invalid_description(self):
        form = OrderForm({"type": "",
                          "description": "",
                        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["description"], [u"This field is required."])
            
## Revision Form
            
class TestRevisionForm(TestCase):
    def test_revision_form_valid(self):
        form = RevisionsForm({"revisions": "revision text here"})
        self.assertTrue(form.is_valid())
    
    def test_revision_form_invalid(self):
        form = RevisionsForm({"revisions": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["revisions"], [u"This field is required."])
    
# class TestTestimonialForm(TestCase):

class TestTestimonialForm(TestCase):
    def test_testimonial_form_valid(self):
        form = TestimonialForm({"testimonial_text": "testimonial text here"})
        self.assertTrue(form.is_valid())
    
    def test_testimonial_form_invalid(self):
        form = TestimonialForm({"testimonial_text": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["testimonial_text"], [u"This field is required."])

# class TestDesignSubmissionForm(TestCase):

## File Upload

# class TestDesignUpdateForm(TestCase):

## File Upload

# class TestDesignAcceptanceForm(TestCase):

class TestDesignAcceptanceForm(TestCase):
    def testd_design_acceptance_form_valid(self):
        form = DesignAcceptanceForm({"order_stage": "Design accepted"})
        self.assertTrue(form.is_valid())

# Views

    

### Create Test Design Object?

class TestOrdersView(TestCase):

        
    def test_orders_view(self):
        page = self.client.get("/orders/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "orders.html")
        
## design detail

### needs parameter

# def test_design_detail(self):
#         user = User.objects.get(username='testuser')
#         feature = Feature(
#             title='Feature test title', 
#             description='This is a new feature description',
#             author_id=user.id)
#         feature.save()
#         response = self.client.get('/features/{}'.format(feature.pk))
#         self.assertEqual(response.status_code, 301)

## order detail

### needs parameter

## order list

## superuser only

## request changes

### needs parameter

## revision detail

### needs parameter

## submit design

### needs parameter

## submit revision

### needs parameter

## submit testimonial

    # def test_testimonial_view(self):
    #     page = self.client.get("/testimonial/")
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "testimonial.html")
