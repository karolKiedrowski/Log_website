from django.db import models

# Create your models here.
class Topic(models.Model):
    """Topic learned by a user."""
    text = models.CharField(max_length=200)
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns model as a string."""
        return self.text
    
class Entry(models.Model):
    """Specific infromation about learning progress."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return model as a string."""
        if len(self.text) > 50:
            return f"{self.text[:50].rstrip()}..."
        else:
            return self.text