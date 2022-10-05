import json
import ftfy # Fixes the text from quotes.json
import os
import random


class Quotes:

    def __init__(self):
        self.data = json.load(open('quotes.json', 'r', encoding='utf-8'))
        self.i = random.randrange(0, len(self.data))
        self.quote = ftfy.fix_text(self.data[self.i]['text'])

    def get_quote(self):
        """
        Returns a random quote
        """
        return self.quote



# Main 
if __name__ == '__main__':
    q = Quotes()
    print(q.get_quote())



