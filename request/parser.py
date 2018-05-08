import json


class Author:
    def __init__(self, author):
        self.author = author

    def dict(self):
        return {'author':self.author}


class Categorie:
    def __init__(self, categorie):
        self.categorie = categorie

    def dict(self):
        return {'categorie':self.categorie}


class Book:
    def __init__(self, google_id, self_link, title, publisher, published_date, description, isbn_13, isbn_10, small_thumbnail):
        self.google_id = google_id
        self.self_link = self_link
        self.title = title
        self.publisher = publisher
        self.published_date = published_date
        self.description = description
        self.isbn_13 = isbn_13
        self.isbn_10 = isbn_10
        self.small_thumbnail = small_thumbnail

    def dict(self):
        return {'google_id':self.google_id,'self_link':self.self_link,'title':self.title,'publisher':self.publisher,'published_date':self.published_date,'description':self.description,'isbn_13':self.isbn_13,'isbn_10':self.isbn_10,'small_thumbnail':self.small_thumbnail}


def extract(raw):

    total = raw['totalItems']
    items = raw['items']
    items_data = {}

    for index in range(0, len(items)):

        path = raw['items'][index]['volumeInfo']

        google_id = raw['items'][index]['id']
        self_link = raw['items'][index]['selfLink']
        title = path['title']
        authors = path['authors']
        publisher = path['publisher']
        published_date = path['publishedDate']
        description = path['description']
        isbn = path['industryIdentifiers'][0:2]
        for i in isbn:
            n = i['type']
            if n == "ISBN_13":
                isbn_13 = i['identifier']
            elif n == "ISBN_10":
                isbn_10 = i['identifier']
        categories = path['categories']
        small_thumbnail = path['imageLinks']['smallThumbnail']

        author = Author(authors)
        categorie = Categorie(categories)
        book = Book(google_id, self_link, title, publisher, published_date, description, isbn_13, isbn_10, small_thumbnail)

        item_data = {("item_"+str(index)): {**author.dict(), **categorie.dict(), **book.dict()}}
        items_data.update(item_data)


    return items_data
