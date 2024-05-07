class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def __add__(self, data):
        new_dict = Dictionary()
        new_dict.dictionary.update(self.dictionary)  
        new_dict.dictionary[data[0]] = data[1]  
        return new_dict  

    def __contains__(self, word):
        return word in self.dictionary

    def __sub__(self, word):
        if word in self.dictionary:
            new_dict = Dictionary() 
            new_dict.dictionary.update(self.dictionary) 
            del new_dict.dictionary[word] 
            return new_dict 

d = Dictionary()

while True:
    print("1) Add word 2) Search word 3) Delete word 4) Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        word = input("Enter the word: ")
        mean = input("Enter the meaning: ")
        d = d + (word, mean)
    elif ch == 2:
        word = input("Enter the word: ")
        if word in d:
            print(f"Word {word} found! Meaning: {d.dictionary[word]}")
        else:
            print("Word not found!")
    elif ch == 3:
        word = input("Enter the word: ")
        if word in d:
            d = d - word 
            print(f"{word} deleted from dictionary.")
        else:
            print("Word not found!")
    elif ch == 4:
        break
    else:
        print("Invalid choice!")
