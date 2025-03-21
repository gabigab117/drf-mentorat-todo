from django.db import models


class SingletonModel(models.Model):

    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        pass
    
    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    max_todo_items = models.PositiveIntegerField()

    def __str__(self):
        return "Paramètre du site"

    class Meta:
        verbose_name = "Paramètre du site"
        verbose_name_plural = "Paramètre du site"
        