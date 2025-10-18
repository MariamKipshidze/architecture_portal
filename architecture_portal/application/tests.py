from django.test import TestCase
from application.factories import ApplicationFactory

class ApplicationTests(TestCase):
    def test_application_creation(self):
        # Create instance using factory
        application = ApplicationFactory()

        # Assert that it was saved (has a primary key)
        self.assertTrue(application.pk)

        # Assert required fields are filled
        self.assertTrue(application.client_name)
        self.assertTrue(application.client_email)
        self.assertTrue(application.project_title)

        # Assert description meets validator requirement
        self.assertGreaterEqual(len(application.project_description), 20)

        # Assert project_type is valid
        valid_types = ['RESIDENTIAL', 'COMMERCIAL', 'INSTITUTIONAL', 'OTHER']
        self.assertIn(application.project_type, valid_types)

        # Optional: check boolean field and date
        self.assertIsInstance(application.viewed, bool)
        self.assertIsNotNone(application.submission_date)
