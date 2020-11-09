from django.db.models import (
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
)
from datetime import date
# Create your models here.

class Category(Model):
    name = CharField(max_length=63)
    slug = SlugField(
        max_length=63,
        help_text="An identifier"
    )

    class Meta:
        ordering = ["name"]
        def __str__(self):
            return self.name


class Blog(Model):
    title = CharField(max_length=63)
    slug = SlugField(
        max_length=63,
        help_text="A label for SEO"
    )
    text = TextField()
    publish_date = DateField(
        "date published", default=date.today
    )
    categories = ManyToManyField(Category, related_name="blog_categories")

    class Meta:
        get_latest_by = "publish_date"
        ordering = ["-publish_date", "title"]
        verbose_name = "blog post"

        def __str__(self):
            return f" {self.title} : {self.publish_date}"


