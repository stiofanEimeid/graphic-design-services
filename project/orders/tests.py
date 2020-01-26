from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import OrderForm, RevisionsForm, TestimonialForm, DesignAcceptanceForm, DesignSubmissionForm, DesignUpdateForm
from users.models import User
from django.shortcuts import reverse, redirect
from .models import Design, Order, Revision
from .views import submit_design

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

# class TestDesignAcceptanceForm(TestCase):

class TestDesignAcceptanceForm(TestCase):
    def testd_design_acceptance_form_valid(self):
        form = DesignAcceptanceForm({"order_stage": "Design accepted"})
        self.assertTrue(form.is_valid())

# Views

### Create Test Design, Order, User and Superuser

class TestOrdersView(TestCase):
    
    def setUp(self):
        test_admin = User.objects.create_superuser(username='testadmin', email="admin@example.com", password='784fhhv*90')
        test_admin.save()
        self.user = test_admin
        test_user2 = User.objects.create_user(username='testuser2', password='kjsnlkblmbl')
        test_user2.save()
        self.user = test_user2
        self.client = Client()
        
    # def test_order_create_view(self):
    #     login = self.client.login(username='testuser2', password='kjsnlkblmbl')
    #     session = self.client.session
    #     session['basket'] = {}
    #     session['basket']['type'] = "Logo"
    #     session['my_basket']['description'] = "Some text here"
    #     session['my_basket']['revision'] = False
    #     session['my_basket']['price'] = 20
    #     session.save()
        
    def test_orders_view(self):
        page = self.client.get("/orders/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "orders.html")
        
    def order_list_view(self):
        login = self.client.login(username='testadmin', password='784fhhv*90')
        page = self.client.get("/order-list/")
        self.assertEqual(page.status_code, 200)
        
    def test_submit_design_view(self):
        login = self.client.login(username='testadmin', password='784fhhv*90')
        user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        order = Order(
            customer = user,
            type = "Logo",
            description = 'This is a new feature description',
            price = "10")
        order.save()
        response = self.client.get(reverse('submit-design', kwargs={'parameter':order.id}))
        self.assertEqual(response.status_code, 200)
        
    def test_valid_design_submission(self):
        login = self.client.login(username='testadmin', password='784fhhv*90')
        user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        order = Order(
            customer = user,
            type = "Logo",
            description = 'This is a new feature description',
            price = "10")
        order.save()
        response = self.client.post(reverse('submit-design', kwargs={'parameter':order.id,}), {
            'source_code': SimpleUploadedFile("test_source.jpg", b"file_content", content_type="image/jpeg"),
            'preview_image': SimpleUploadedFile("test_preview.jpg", b"file_content", content_type="image/jpeg"),
        })
        self.assertEqual(response.status_code, 200)
        
## request changes


## test submit revision view

    def test_submit_revision_view(self):
            login = self.client.login(username='testadmin', password='784fhhv*90')
            user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
            order = Order(
                customer = user,
                type = "Logo",
                description = 'This is a new feature description',
                price = "10")
            order.save()
            design = Design(
                    customer = user,
                    type = "Logo",
                    description = 'This is a new description',
                    order_number = order
                    )
            design.save()
            revision = Revision(
                customer = user,
                type = "Logo",
                revisions = 'This is a new feature description',
                price = "10",
                design_id = design
                )
            revision.save()
            response = self.client.get(reverse('submit-revision', kwargs={'parameter':design.id}))
            self.assertEqual(response.status_code, 200)

## submit revision
    def test_valid_revision_submission(self):
            login = self.client.login(username='testadmin', password='784fhhv*90')
            user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
            order = Order(
                customer = user,
                type = "Logo",
                description = 'This is a new feature description',
                price = "10")
            order.save()
            design = Design(
                    customer = user,
                    type = "Logo",
                    description = 'This is a new description',
                    order_number = order
                    )
            design.save()
            revision = Revision(
                customer = user,
                type = "Logo",
                revisions = 'This is a new feature description',
                price = "10",
                design_id = design
                )
            revision.save()
            response = self.client.post(reverse('submit-revision', kwargs={'parameter':design.id,}), {
                'source_code': SimpleUploadedFile("test_source.jpg", b"file_content", content_type="image/jpeg"),
                'preview_image': SimpleUploadedFile("test_preview.jpg", b"file_content", content_type="image/jpeg"),
            })
            self.assertEqual(response.status_code, 200)

## submit testimonial

# gallery design detail
 
