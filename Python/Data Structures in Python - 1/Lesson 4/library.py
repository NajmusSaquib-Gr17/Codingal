class Library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendBook = {}

    def displayBooks(self):
        print('We have following books: ')
        for book in self.booklist:
            print(book)

    def lendBooks(self, user, book):
        if book not in self.lendBook.keys():
            self.lendBook.update({book:user})
            print('Update in the database, you can take the book')
        else:
            print('You have already borrowed it')

    def addBooks(self, book):
        self.booklist.append(book)
        print('Book added')
    
    def returnBook(self, book):
        self.lendBook.pop(book)

if __name__ == '__main__':
    books = Library(['Python', 'Javascript', 'Harry Potter', 'Machine Learning', 'DeepLearning', 'AI'], 'user')

    while(True):
        print('Welcome')
        print('1. Display Books')
        print('2. Lend a Book')
        print('3. Add a Book')
        print('4. Return Book')

        user_input = int(input())

        if user_input not in [1, 2, 3, 4]:
            print('Please Enter a Valid Input')
            continue
            
        
        if user_input == 1:
            books.displayBooks()
        elif user_input == 2:
            book = input('Enter the book name: ')
            user = input('Enter your name: ')
            books.lendBooks(user, book) # it should be lendBooks insted of lendBook

        elif user_input == 3:
            book = input('Enter the book name you want to add')# promt error it should be Enter the book name you want to add
            books.addBooks(book)# Wrong Method returnBook(books) it should be addBooks(book)
        else:
            book = input('Enter the book name you want to return: ')
            books.returnBook(book)
        

        
        print('Enter q to quit and c to continue')
        user_input2 = ''
        while(user_input2 != 'c' and user_input2 != 'q'):
            user_input2 = input()
            if user_input2 == 'q':
                exit()
            else: 
                continue