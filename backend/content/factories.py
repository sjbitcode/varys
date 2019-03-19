import datetime
import random

import factory
import faker

from .models import Tweet, Author


# Instance of Faker for lazy use.
fake = faker.Faker()

author_ids = Author.objects.values_list('id', flat=True)

class TweetFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tweet
    
    tweet_id = factory.Faker('credit_card_number')
    text = factory.LazyFunction(lambda: ' '.join(fake.paragraphs())[:280])
    author_id = factory.LazyFunction(lambda: random.choice(author_ids))
    created_at = factory.LazyFunction(lambda: fake.date_time_between(start_date='-1y', end_date='now', tzinfo=datetime.timezone.utc))
