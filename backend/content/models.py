from django.db import models


class Author(models.Model):
    author_id = models.CharField(
        max_length=50,
        verbose_name='Author twitter ID'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Author twitter profile full name'
    )
    handle = models.CharField(
        max_length=50,
        verbose_name='Author twitter profile handle'
    )
    description = models.TextField(verbose_name='Author twitter profile description')
    created_at = models.DateTimeField(verbose_name='Author twitter profile creation datetime')
    profile_image = models.URLField(verbose_name='Author twitter profile image')

    def __str__(self):
        return self.handle

    @property
    def url(self):
        return f'https://twitter.com/{self.handle}'


class Tweet(models.Model):
    tweet_id = models.CharField(
        max_length=50,
        verbose_name='Tweet ID'
    )
    text = models.TextField(verbose_name='Tweet text')
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='tweets',
        verbose_name='Tweet author'
    )
    created_at = models.DateTimeField(verbose_name='Tweet creation datetime')

    def __str__(self):
        return self.text[:50]

    @property
    def url(self):
        return f'https://twitter.com/{self.author.handle}/status/{self.tweet_id}'
