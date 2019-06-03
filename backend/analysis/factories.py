import datetime

import factory
import faker

from .enums import IBM_WATSON, AWS_COMPREHEND
from .models import AnalysisResponse


# Instance of Faker for lazy use.
fake = faker.Faker()


class IBMResponseFactory(factory.DjangoModelFactory):
    class Meta:
        model = AnalysisResponse
    
    service = IBM_WATSON
    tweet = factory.SubFactory('content.models.Tweet')
    data = {'sentiment': 0.8}
    created_at = factory.LazyFunction(datetime.datetime.now)


class AWSResponseFactory(factory.DjangoModelFactory):
    class Meta:
        model = AnalysisResponse
    
    service = AWS_COMPREHEND
    tweet = factory.SubFactory('content.models.Tweet')
    data = {'sentiment': 0.5}
    created_at = factory.LazyFunction(datetime.datetime.now)
