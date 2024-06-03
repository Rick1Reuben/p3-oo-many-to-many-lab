class Author:
    all = []
    def __init__(self, name):
        self._name = ""
        self.name = name 
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]
       

    def books(self): 
        return [contract.book for contract in Contract.all if contract.author is self] # was 
       
    def sign_contract(self, book, date, royalties): 
        return Contract(self, book, date, royalties)

    def total_royalties(self): 
      
        return sum([contract.royalties for contract in Contract.all if contract.author is self]) 

class Book: 
    all = []
    def __init__(self, title):
        self._title = title 
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    def contracts(self): # think of as get_contracts
        return [contract for contract in Contract.all if contract.book is self] 

    def authors(self): # think of as get_authors
        return [contract.author for contract in Contract.all if contract.book is self]
       
class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
  
    @classmethod
    def contracts_by_date(cls, date): 
        return [contract for contract in Contract.all if contract.date is date]
       
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of the Author class")
        self._author = value 

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of the Book class")
        self._book = value

    @property
    def date(self):
        return self._date

    @ date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Royalties must be a number")
        self._royalties = value