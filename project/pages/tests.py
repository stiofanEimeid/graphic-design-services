from django.test import TestCase

class TestHomeView(TestCase):
    def test_index_view(self):
        page = self.client.get("")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home.html")

class TestGalleryView(TestCase):
    def test_gallery_view(self):
        page = self.client.get("/gallery/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "gallery.html")
        
        
# Error test 403, 404, 500





