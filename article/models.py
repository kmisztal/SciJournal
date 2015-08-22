from django.db import models

#TODO
# classes:
# article versions (date, files, comment)
# review (reviewer, coment)
# held in Publication as many to many
# add states (Assan)
# add to admin page

class Publication(models.Model):
    """
    Model representing a publication.
    """

    class Meta:
        app_label = 'article'
        ordering = ['-year', '-month', '-id']
        verbose_name_plural = 'Articles'

    # names shown in admin area
    MONTH_CHOICES = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    )

    title = models.CharField(max_length=512)
    #TODO many to many with user
    authors = models.CharField(max_length=2048,
                               help_text='List of authors separated by commas or <i>and</i>.')
    year = models.PositiveIntegerField()
    month = models.IntegerField(choices=MONTH_CHOICES, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True, verbose_name='Issue number')
    pages = PagesField(max_length=32, blank=True)
    note = models.CharField(max_length=256, blank=True)
    keywords = models.CharField(max_length=256, blank=True,
                                help_text='List of keywords separated by commas.')
    url = models.URLField(blank=True, verbose_name='URL',
                          help_text='Link to PDF or journal page.')
    #pdf = models.FileField(upload_to='publications/', verbose_name='PDF', blank=True, null=True)
    doi = models.CharField(max_length=128, verbose_name='DOI', blank=True)
                                   help_text='If publication was written in another lab, mark as external.')
    abstract = models.TextField(blank=True)