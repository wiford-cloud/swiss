from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class home_slide(models.Model):

    s_title = models.CharField(max_length=100)
    s_description = models.TextField(max_length=150)
    s_button = models.CharField(max_length=20)
    s_image = ImageField(upload_to='media')

    class Meta():
        ordering = ("s_button", "s_title", "s_description")

    def __str__(self):
        return f"{self.s_title},{self.s_description},{self.s_button}"

# latest news 

class latest_news(models.Model):
    ln_title = models.CharField(max_length=50)
    ln_description = models.TextField(max_length=300)
    ln_image = models.ImageField(upload_to='media')
    

    def __str__(self):
        return f"{self.ln_title}, {self.ln_description},{self.ln_image}"


# gallery

class gallery(models.Model):
    g_image = models.ImageField(upload_to='media/Gallery')

    def __str__(self):
        return f"{self.g_image}"

#guild leadership

class Executive(models.Model):

    Names = models.CharField(max_length=100)
    E_Position = models.TextField(max_length=100)
    E_picture = ImageField(upload_to='media')

    class Meta():
        ordering = ("Names", "E_Position","E_picture")

    def __str__(self):
        return f"{self.Names},{self.E_Position},{self.E_picture}"


#Executives
class cabinet(models.Model):

    Name = models.CharField(max_length=100)
    position = models.TextField(max_length=100)
    picture = ImageField(upload_to='media')

    class Meta():
        ordering = ("Name", "position","picture")

    def __str__(self):
        return f"{self.Name},{self.position},{self.picture}"

# parliament 

class speakership(models.Model):

    Name = models.CharField(max_length=50)
    Position = models.TextField(max_length=50)
    m_picture = ImageField(upload_to='media')

    class Meta():
        ordering = ("Name","Position", "m_picture")

    def __str__(self):
        return f"{self.Name},{self.Position},{self.m_picture}"


class parliament(models.Model):

    name = models.CharField(max_length=100)
    departement = models.TextField(max_length=100)
    m_picture = ImageField(upload_to='media')

    class Meta():
        ordering = ("name","departement", "m_picture")

    def __str__(self):
        return f"{self.name},{self.departement},{self.m_picture}"
