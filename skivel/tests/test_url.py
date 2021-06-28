from django.test import SimpleTestCase
from django.urls import reverse, resolve
from skivel.shop.views import shop_home, ProductDetailView


class TestUrls(SimpleTestCase):

    def test_shop_home_url_resolve(self):
        url = reverse('product_detail')
        print(resolve(url))

