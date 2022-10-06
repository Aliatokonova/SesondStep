from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        return f'{self.name} --> {self.parent}' if self.parent else f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    preview = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} - {self.title}'

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

class PostImages(models.Model):
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to ='image/')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='images')


    @staticmethod
    def generate_name():
        from random import randint
        return 'image' +str(randint(100000000, 10000000))

    def save(self):
        self.title = self.generate_name(*args, **kwargs)
        return super(PostImages, self).save(PostImages, self).save(*args, **kwargs)

class Comment(models.Model):
    owner = models.ForeignKey('auth.User', related_name='comment', on_delete=models.CASCADE)


    post = models.ForeignKey(Post, related_name ='coment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} -> {self.post} -> {self.created_at}'

class Meta:
    verbose_name = 'Coments'
    verbose_name_plural = 'Comments'