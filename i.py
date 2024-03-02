class LibraryLite:
    def search(books, title):
        for book in books:
            if (title==book):
                print(book)
    def returns(book):
        print(f"{book} has been returned.") #This is definitly my new favorite way of doing print statements.

class LibraryFull:
    def search(books, title):
        for book in books:
            if (title==book):
                print(book)
    def returns(book):
        print(f"{book} has been returned.")
    def catalog(book, add):
        if (add==True):
            print("add book")
        else:
            print("remove book")
    def report(data):
        print("Data but in a useful way.")
