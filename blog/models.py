from django.db import models


# Create your models here.
class Blog(models.Model):
    """
    Allows user to add a blog post
    """
    title = models.CharField(
        max_length=200,
        blank=False)
    pub_date = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    description = models.TextField(
        max_length=2000,
        blank=False)

    def pub_date_beautify(self):
        """
        Beautifies the pub_date and makes it a more
        presentable format using strftime
        """
        return self.pub_date.strftime('%e %b %Y')

    def __str__(self):
        return self.title
