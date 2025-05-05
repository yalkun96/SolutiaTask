#Task 1
from statistics import mean

sentence = input("Enter a sentence: ")

def reverse_words(sentence):
    revesed_sentence = ' '.join(sentence.split()[::-1])
    return revesed_sentence



def reverse_and_swap_case(sentence):
    swapped = ''
    for letter in sentence:
        if letter.isupper():
            swapped += letter.lower()
        elif letter.islower():
            swapped += letter.upper()
        else:
            swapped += letter
    revesed_sentence = ' '.join(swapped.split()[::-1])
    return revesed_sentence

print(reverse_words('hello world'))
print(reverse_and_swap_case('Hello World!'))

#Task 2
books = [
    {'title': "The Hitchhiker's Guide to the Galaxy", 'price': 12.50},
    {'title': "Price and Prejudice", 'price': 9.99},
    {'title': "To Kill a Mockingbord", 'price': 15.00},
]

def calculate_average_price(dict):
    total = 0
    for book in books:
        total += book['price']
    return total / len(books)


print(calculate_average_price(books))





