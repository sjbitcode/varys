from django.core.management.base import BaseCommand, CommandError

from content.factories import TweetFactory
from content.models import Tweet, Author


class Command(BaseCommand):
    help = 'Creates random tweets from amount provided'

    def add_arguments(self, parser):
        parser.add_argument('tweet_amt', nargs='?', type=int)
    
    def handle(self, *args, **options):
        try:
            tweet_amt = options['tweet_amt']
        except KeyError:
            raise CommandError('Something wrong with number of tweets you provided')

        TweetFactory.create_batch(tweet_amt)
