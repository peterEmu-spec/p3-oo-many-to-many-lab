class Author:
    def __init__(self,name):
        self.name=name
        self._contracts=[]
        self._books=[]
    def contracts(self):
        return self._contracts
    def books(self):
        return self._books
    def sign_contract(self,book,date,royalties):
        if not isinstance(book, Book):
            raise TypeError("book must be a Book instance")
        contract=Contract(author=self,book=book,date=date,royalties=royalties)
        return contract
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


        pass
    pass


class Book:
    def __init__(self,title):
        self.title=title
        self._contracts=[]
        self._authors=[]
    def contracts(self):
        return self._contracts
    def authors(self):
        return self._authors
        pass
    pass

class Contract:
    all = []  # Use the name the test expects

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        if not isinstance(book, Book):
            raise TypeError("book must be a Book instance")
        if not isinstance(date, str):
            raise TypeError("date must be of type string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be of type integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Establish relationships
        author._books.append(book)
        author._contracts.append(self)
        book._contracts.append(self)
        book._authors.append(author)
        Contract.all.append(self)  # Add to class-level list

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts for the given date, sorted by date"""
        return sorted([c for c in cls.all if c.date == date], key=lambda c: c.date)
