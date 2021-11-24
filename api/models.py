from django.db import models

class items(models.Model):
    name = models.TextField()
    isbn = models.TextField()
    year = models.IntegerField()
    country = models.TextField()
    number_of_pages = models.IntegerField()
    publisher = models.TextField()
    release_date= models.TextField()
    class Meta:
        db_table = 'items'
    # authors = models.ManyToManyField(author)
    #  db.relationship('author',secondary=author_item_mapping,backref=db.backref('book_list',lazy=True,passive_deletes=True),lazy=True,passive_deletes=True)
    
    def __repr__(self):
        return f"item('{self.name}')"



class author(models.Model):
    name = models.TextField()
    books = models.ManyToManyField(items,related_name='authors') 
    class Meta:
        db_table = 'author'
    # db.reationship('items',secondary=author_item_mapping,backref=db.backref('author_list',lazy=True,passive_deletes=True),lazy=True,passive_deletes=True)
    
    def __repr__(self):
        return f"writer'{self.name}')"




