from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    pub_date = models.DateField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = (
            '-pub_date',
            'title',
        )

    def get_absolute_url(self):
        return reverse('post', args=(self.id,))

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    content = models.TextField()
    rating = models.IntegerField()

    def __unicode__(self):
        return self.content
