
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Drone, Medication

# Create your tests here.


class DronTestCase(APITestCase):

    def test_create_drone_valid(self):
        #Test to create a drone with valid data.
        self.login_url = '/dron_register/'
        self.drone = Drone.objects.create(
            serial_number='f455t45ggvf5234',
            model='1'
        )
        response = self.client.post(
            self.login_url,
            {
                'serial_number':self.drone.serial_number,
                'model':self.drone.model
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_drone_invalid(self):
        #Test to create a drone with invalid data.
        self.login_url = '/dron_register/'
        self.drone = Drone.objects.create(
            serial_number='f455t45ggvf5234***',
            model='1'
        )
        response = self.client.post(
            self.login_url,
            {
                'serial_number':self.drone.serial_number,
                'model':self.drone.model
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_add_medications_drone_valid(self):
        #Test adding medications to a drone valid data.
        drone = Drone(
            serial_number='f455t45ggvf5234',
            model='1'
        )
        drone.save()

        medication = Medication(
            name='f455t45ggvf5234',
            weight=100,
            code='HGHJA_2423',
            image=''
        )
        medication.save()
        url = f'/add_medications_drone/{drone.id}'
        
        datas= {'medications': [f'{medication.id}']}
        
        response = self.client.patch(url, datas, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_add_medications_drone_invalid(self):
        #Test adding medications to a drone invalid data.
        drone = Drone(
            serial_number='f455t45ggvf5234',
            model='1'
        )
        drone.save()

        medication = Medication(
            name='f455t45ggvf5234',
            weight=200,
            code='HGHJA_2423',
            image=''
        )
        medication.save()
        url = f'/add_medications_drone/{drone.id}'
        
        datas= {'medications': [f'{medication.id}']}
        
        response = self.client.patch(url, datas, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_medications_valid(self):
       #Test to create a medication with valid data.
        url = '/create_medication/'
        self.medication = Medication.objects.create(
            name='f455t45ggvf5234',
            weight=100,
            code='HGHJA_2423',
            image=''
        )
        response = self.client.post(
            url,
            {
                'name':self.medication.name,
                'weight':self.medication.weight,
                'code':self.medication.code
                
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_medications_invalid(self):
       #Test to create a medications with invalid data.
        url = '/create_medication/'
        self.medication = Medication.objects.create(
            name='f455t45ggv_f5234',
            weight=100,
            code='HGHJA_2423*',
            image=''
        )
        response = self.client.post(
            url,
            {
                'name':self.medication.name,
                'weight':self.medication.weight,
                'code':self.medication.code
                
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_check_items_drone_valid(self):
        #TEST Checking of the elements in a drone satisfactory case.
        drone = Drone(
            serial_number='f455t45ggvf5234',
            model='1'
        )
        drone.save()

        medication = Medication(
            name='f455t45ggvf5234',
            weight=200,
            code='HGHJA_2423',
            image=''
        )
        medication.save()

        drone.medications.add(medication)
        drone.save()

        url = f'/check_items_drone/{drone.id}'
        
        datas= {'medications': [
                {
                    "name": medication.name,
                    "weight": medication.weight
                }
            ]}
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.data, {
                "id": drone.id,
                "serial_number": drone.serial_number,
                "medications": [{
                        "name": medication.name,
                        "weight": medication.weight
                    }]})

    def test_check_items_drone_invalid(self):
        #Test checking of the elements in a drone in a failed case.
        drone = Drone(
            serial_number='f455t45ggvf5234',
            model='1'
        )
        drone.save()

        medication = Medication(
            name='f455t45ggvf5234',
            weight=200,
            code='HGHJA_2423',
            image=''
        )
        medication.save()

        url = f'/check_items_drone/{drone.id}'
        
        datas= {'medications': [
                {
                    "name": medication.name,
                    "weight": medication.weight
                }
            ]}
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        self.assertNotEqual(response.data, {
                "id": drone.id,
                "serial_number": drone.serial_number,
                "medications": [{
                        "name": medication.name,
                        "weight": medication.weight
                    }]})