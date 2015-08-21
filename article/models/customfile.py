__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from django.db import models

from article.models import Publication


class CustomFile(models.Model):
    class Meta:
        app_label = 'article'

    publication = models.ForeignKey(Publication)
    description = models.CharField(max_length=256)
    file = models.FileField(upload_to='article/')

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description
