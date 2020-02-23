from django.db import models


# Create your models here.
class Project(models.Model):
    """
    Stores information about user's projects/jobs
    that they worked on
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    # Images will be uploaded to media/portfolio/images
    image = models.ImageField(upload_to='portfolio/images/')
    # blank=True makes this field optional
    url = models.URLField(blank=True)

    def __str__(self):
        return "#{0} - {1}".format(self.id, self.title)
