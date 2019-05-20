from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
import json
#from rest_framework.test import APITestCase

class OrdersTest(TestCase):
    def test_sendOrder(self):
        """
        debe enviar un 201 cuando llega información a la url y se envía a kafka
        """
        url = reverse('ListOrders')
        data = {"Domain": "Fulfillment",
                "OrderId": "929211474791-01",
                "State": "waiting-ffmt-authorization",
                "LastChange": "2019-05-02T17:24:45.4558497Z"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_getOrders(self):
        """
        debe enviar un 200 y en el body data no avaliable        """    
        url = reverse('ListOrders')
        jsonRes={"data": "no avaliable"}
           
        response = self.client.get(url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(jsonRes, response_data)