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

### Create Test Design, Order, User and Superuser

class TestOrdersView(TestCase):
    
    def set_up(self):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()
        test_admin = User.objects.create_superuser(username="testadmin", email="admin@example.com", password="784fhhv*90")
        test_admin.save()
        test_order = Order.objects.create(
            customer = "testuser1",
            type = "Logo",
            description = 'This is a new feature description',
            price = "10"
            )
        test_design = Design.objects.create(
            type='Logo', 
            description='This is a new feature description',
            customer= "testuser1",
            order_stage = "Design pending approval",
            source_code= SimpleUploadedFile("test_source.jpg", b"file_content", content_type="image/jpeg"),
            preview_image= SimpleUploadedFile("test__preview_image.jpg", b"file_content", content_type="image/jpeg"),
            order_number = Order.objects.get(customer='testuser1')
           )
        
    def test_orders_view(self):
        page = self.client.get("/orders/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "orders.html")
        
# gallery design detail
    # def test_gallery_view(self):
    #     design = Design.objects.get(customer = "testuser1")
    #     page = self.client.get("gallery-design-detail/{}".format(design.pk))
    #     self.assertEqual(page.status_code, 302)
    


### needs parameter


## order list
    # def order_list_view(self):
    #     login = self.client.login(username='testadmin', password='784fhhv*90')
    #     page = self.client.get("/order-list/")
    #     self.assertEqual(page.status_code, 200)

## request changes

### needs parameter

## revision detail

### needs parameter

## submit design
        
### needs parameter

## submit revision

### needs parameter

## submit testimonial
