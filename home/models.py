from django.db import models


class Home(models.Model):
    filename = models.CharField(max_length=255)
    videofile= models.FileField(upload_to='video/home', null=True, verbose_name="")

    def __str__(self):
        return self.filename + ": " + str(self.videofile)

    def snippet(self):
        return self.filename
