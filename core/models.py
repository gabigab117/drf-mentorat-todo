from django.db import models


class SingltonModel(models.Model):
    
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


class SiteSettings(SingltonModel):
    max_todo_items = models.PositiveIntegerField(verbose_name="nombre maximum de todo items")
    
    def __str__(self):
        return "Paramètres du site"
    
    class Meta:
        verbose_name = "Paramètres du site"
        verbose_name_plural = "Paramètres du site"
        