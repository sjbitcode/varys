import datetime
import random

import factory
import faker

from .models import Tweet, Author
from analysis.factories import IBMResponseFactory, AWSResponseFactory


# Instance of Faker for lazy use.
fake = faker.Faker()


class TweetFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tweet
    
    tweet_id = factory.Faker('credit_card_number')
    text = factory.LazyFunction(lambda: ' '.join(fake.paragraphs())[:280])
    author = factory.Iterator(Author.objects.all())
    created_at = factory.LazyFunction(lambda: fake.date_time_between(start_date='-1y', end_date='now', tzinfo=datetime.timezone.utc))

    ibm_response = factory.RelatedFactory(IBMResponseFactory, 'tweet')
    aws_response = factory.RelatedFactory(AWSResponseFactory, 'tweet')
