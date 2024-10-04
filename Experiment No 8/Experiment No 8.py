# To Program a Publication based Company Scenario on Inhertance
class Publications():
    def __init__(self):
        self.title = ""
        self.prize_of_publication = 0.0
        
    def get(self):
        self.title = input("Enter the Title Publications : ")
        self.prize_of_publication = float(input("Enter the Prize of Publication : "))
    def set(self):
        print(f"Title Publications : {self.title}")
        print(f"Prize of Publication : {self.prize_of_publication}")
class Book(Publications):
    def __init__(self):
        super().__init__()
        self.page_count = 0
    def get(self):
        super().get()
        self.page_count = int(input("Enter the Total Number Pages of the Book : "))
    def set(self):
            super().set()
            print(f"Total Number of Pgaes : {self.page_count}")
class Tape(Publications):
    def __init__(self):
        super().__init__()
        self.playing_time = 0
    def get(self):
        super().get()
        self.playing_time = int(input("Enter the Total Playting Time of the Tape : "))
    def set(self):
        super().set()
        print(f"Total Playing Time of Tape : {self.playing_time}")

def main():
    print("Enter details for the book:")
    book = Book()
    book.get()
    print("\nBook Details:")
    book.set()
    print("\n")

    print("Enter details for the tape:")
    tape = Tape()
    tape.get()
    print("\nTape Details:")
    tape.set()


if __name__ == "__main__":
    main()
