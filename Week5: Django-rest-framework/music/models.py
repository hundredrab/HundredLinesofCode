from django.db import models


class Artist(models.Model):
    """Model definition for Artist."""

    name = models.CharField(max_length=50)
    real_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        """Meta definition for Artist."""

        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        """Unicode representation of Artist."""
        return self.name


class Track(models.Model):
    """Model definition for Track."""

    name = models.CharField(max_length=50)
    artist = models.ManyToManyField(Artist, related_name='track')
    release_year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        """Meta definition for Track"""

        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'

    def __str__(self):
        """Unicode representation of Track"""
        return self.name
