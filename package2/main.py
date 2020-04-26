
from urllib.request import urlopen
import random

myVar = False

def fetch_word():
    try: 
        story = urlopen("http://sixty-north.com/c/t.txt")
        stor_words = []
        for line in story:
            line_words = line.decode('utf8').split()
            for word in line_words:
                stor_words.append(word)
                # print(stor_words)
        story.close()

        for stor_word in stor_words:
            print(stor_word) 
    except (TypeError, KeyError) as e:
        print(e)
        pass
    except ValueError:
        print('value error')

if __name__ == '__main__':
    fetch_word()


def print_item():
    word_array = [ 1,2,3,4,5]
    for word in word_array:
        pass

def ask_name():
    name = input('so, what is your name:')
    print('Hi'+ " " + name)

ask_name()

def print_random_value():
    for i in range(3):
        print(random.randint(10, 20))

print_random_value()


class Mammal:
    
    def walk(self):
        print('walk')


class Dog(Mammal):        #Inheritance
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')
    
    def draw(self):
        print('draw')


point1 = Dog(1,2)
point1.draw()
point1.walk()