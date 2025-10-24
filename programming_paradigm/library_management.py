class Book:
    def __init__(self, title, author):
        self.title  = title
        self.author = author
        self.__is_checked_out = False
    
    def check_out(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False

    def is_available(self):
        return not self.__is_checked_out
    
class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book : Book):
        self._books.append(book)
        print(f"Available books after setup:")
        self.list_available_books()
    
    def check_out_book(self, title):       
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                print(f"Available books after checking out '{title}':")
                self.list_available_books()
                return
        print(f"Book: {title} not found.")
    
    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                print(f"Available books after returning '{title}':")
                self.list_available_books()
                return
        print(f"Book: {title} not found")
    
    def list_available_books(self):
       if len(self._books) == 0:
           print("No books available at the moment.")
           return
       for book in self._books:
           if book.is_available():
               print(f"{book.title} by {book.author}")
           