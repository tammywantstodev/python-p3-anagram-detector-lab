# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word=word

    def match(self, anagrams):
        matches=[]
        for anagram in anagrams:
           if sorted(anagram) == sorted(self.word):
               matches.append(anagram)
        return matches 

    

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])
# => ['inlets']