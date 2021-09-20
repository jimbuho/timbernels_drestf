from django.test import TestCase

from rest_framework.test import APITestCase, APIRequestFactory

from . import views

import json

class CreateTestCase(APITestCase):
    
    def test_create(self):
        """
        Test creation of new links, unique title validation and
        valid title text format
        """
        data = {
            'title':'spartans'
        }
        
        response = self.client.post('/api/v1/links/create/', 
                                    data=json.dumps(data),
                                    content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['title'], data['title'])
        
        response = self.client.post('/api/v1/links/create/', 
                                    data=json.dumps(data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 400)
        
        
        data = {
            'title':'Los González'
        }
        
        response = self.client.post('/api/v1/links/create/', 
                                    data=json.dumps(data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['title'][0]), 
                         'Invalid format title, do not use invalid characters')
        
    def test_update(self):
        """
        Test update of title
        """
        data = {
            'title':'goblings'
        }
        
        response = self.client.post('/api/v1/links/create/', 
                                    data=json.dumps(data),
                                    content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        
        data['title'] = 'goonies'
        
        response = self.client.put('/api/v1/links/update/1/', 
                                    data=json.dumps(data),
                                    content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], data['title'])
        
    def test_list(self):
        """
        Test list request
        """
        MAX_LINKS = 10
        
        for i in range(1,MAX_LINKS):
            data = {
                'title':'Team{}'.format(i)
            }
            
            response = self.client.post('/api/v1/links/create/', 
                                        data=json.dumps(data),
                                        content_type='application/json')
                
            self.assertEqual(response.status_code, 201)
        
        
        response = self.client.get('/api/v1/links/list/', 
                                    format='json')
        
        self.assertEqual(response.status_code, 200)
        items = [dict(r) for r in response.data]
        self.assertEqual(len(items), MAX_LINKS-1)
        self.assertEqual(items[-1]['title'],'Team{}'.format(MAX_LINKS-1))
    
    def test_delete(self):
        """
        Test delete an item
        """
        MAX_LINKS = 5
        
        for i in range(1,MAX_LINKS):
            data = {
                'title':'Team{}'.format(i)
            }
            
            response = self.client.post('/api/v1/links/create/', 
                                        data=json.dumps(data),
                                        content_type='application/json')
                
            self.assertEqual(response.status_code, 201)
        
        
        response = self.client.get('/api/v1/links/list/', 
                                    format='json')
        
        self.assertEqual(response.status_code, 200)
        items = [dict(r) for r in response.data]
        self.assertEqual(len(items), MAX_LINKS-1)
        
        response = self.client.delete('/api/v1/links/delete/1/',
                                    format='json')
        
        self.assertEqual(response.status_code, 204)
        
        
        response = self.client.get('/api/v1/links/list/', 
                                    format='json')
        
        self.assertEqual(response.status_code, 200)
        items = [dict(r) for r in response.data]
        self.assertEqual(len(items), MAX_LINKS-2)
        
    def test_visit(self):
        """
        Test a visit at link
        """
        data = {
            'title':'goonies'
        }
        
        response = self.client.post('/api/v1/links/create/', 
                                    data=json.dumps(data),
                                    content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['visits'], 0)
        
        response = self.client.put('/api/v1/links/visit/goonies/', 
                                    data=json.dumps(data),
                                    content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['visits'], 1)

