# Question 1
class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

author1 = Author('J.K Rowling')
author2 = Author('author2')
book1 = Book('Harry Potter', author1)
book2 = Book('book2', author1)
book3 = Book('book3', author2)

books = [book1, book2, book3]

for book in books:
    print(f'{book.title} is written by {book.author.name}')

# Question 2
class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return

class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(dog.name + " checked in")
        return

    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(dog.name + " checked out")
        return

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)

dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")

hotel = Hotel()

hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.greet_dogs()

hotel.dog_checkout(dog1)
hotel.greet_dogs()

# Question 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return

    def remove_book(self, book):
        self.books.remove(book)
        return

    def get_books(self):
        return [book.title for book in self.books]


book1 = Book('title1', 'author1')
book2 = Book('title2', 'author2')

library = Library()

library.add_book(book1)
library.add_book(book2)

books = library.get_books()
print(books)
