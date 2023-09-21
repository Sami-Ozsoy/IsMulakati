from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    suite = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=50)
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=20)
    companyName = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    body = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Albums(models.Model):

    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Photo(models.Model):

    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    thumbnailUrl = models.CharField(max_length=50)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Todo(models.Model):

    title = models.CharField(max_length=50)
    completed = models.BooleanField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
