import factory
from application.models import Application

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Application

    client_name = factory.Faker('name')
    client_email = factory.Faker('email')
    client_phone = factory.Faker('phone_number')

    project_title = factory.Faker('sentence', nb_words=4)
    project_type = factory.Iterator(['RESIDENTIAL', 'COMMERCIAL', 'INSTITUTIONAL', 'OTHER'])
    project_description = factory.Faker('paragraph', nb_sentences=5)

    viewed = factory.Faker('boolean', chance_of_getting_true=30)
    notes = factory.Faker('sentence', nb_words=10)
