from django.db import models


class Bb(models.Model):
    
    # class Kinds(models.TextChoices):
    #     BUY = 'b', 'Куплю'
    #     SELL = 's', 'Продам'
    #     EXCHANGE = 'c', 'Обменяю'
    #     RENT = 'r'
    #     __empty__ = 'Выберите тип публикуемого объявления'
        
        
    class Kinds(models.IntegerChoices):
        BUY = 1, 'Куплю'
        SELL = 2, 'Продам'
        EXCHANGE = 3, 'Обменяю'
        RENT = 4
        __empty__ = 'Выберите тип публикуемого объявления'
    
    
    TYPES_PRODUCTS = (
        ('', 'Выберите тип продукта'),
        ('new', 'Новый'),
        ('old', 'Б/У'),
    )
    
    # KINDS = (
    #     ('Купля-Продажа', (
    #         ('b', 'Куплю'),
    #         ('s', 'Продам'),
    #     )),
    #     ('Обмен', (
    #         ('c', 'Обменяю'),
    #     ))
    # )
    
    
    title = models.CharField(max_length=50,
                            verbose_name='Товар')
    content = models.TextField(null=True, 
                               blank=True, 
                               verbose_name='Описание')
    price = models.FloatField(null=True, 
                              blank=True, 
                              verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, 
                                     db_index=True, 
                                     verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', 
                               null=True, 
                               on_delete=models.PROTECT, 
                               verbose_name='Рубрика')
    types_of_product = models.CharField(max_length=3,
                                        choices=TYPES_PRODUCTS,
                                        blank=True, # необязательно к заполнению
                                        verbose_name='Состояние продукта')
    kind = models.CharField(max_length=1,
                            choices=Kinds.choices,
                            default=Kinds.SELL,
                            verbose_name='Тип объявления')
    
    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
        
        
class Measure(models.Model):
    class Measurements(float, models.Choices):
        METERS = 1.0, 'Метры'
        FEET = 0.3048, 'Футы'
        YARDS = 0.9144, 'Ярды'
        
    measurements = models.FloatField(choices=Measurements.choices)


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
