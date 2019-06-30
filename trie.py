class Trie(object):

    def __init__(self,words):
        self._end = '*'
        self.trie = dict()
        self.max = 1
        self.word = ""
        self.maxlet = 1
        self.letter = ''
        self.chars = {}
        self.words = words
        for word in self.words.split():
            self.add_word(word)
        self.freq_word()
        
    def __repr__(self):
        return repr(self.trie)

    def make_trie(self, *words):
        trie = dict()
        for word in words:
            temp_dict = trie
            for letter in word:
                temp_dict = temp_dict.setdefault(letter, {})
            temp_dict[self._end] = self._end
        return trie

    def find_word(self, word):
        sub_trie = self.trie

        for letter in word:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]
            else:
                return False
        else:
            if self._end in sub_trie:
                sub_trie[self._end] += 1
                return True
            else:
                return False

    def freq_word(self):
        for word in self.words.split():
            sub_trie = self.trie
            for letter in word:
                if letter in sub_trie:
                    sub_trie = sub_trie[letter]       
            
            if self._end in sub_trie:
                if self.max < sub_trie[self._end]:
                        self.max = sub_trie[self._end]
                        self.word = word
            else:
                print("False")
        for key, value in self.chars.items():
            if value>self.maxlet:
                self.maxlet = value
                self.letter = key
    
    def add_word(self, word):
        if self.find_word(word):
            #print("Word Already Exists")
            return self.trie

        temp_trie = self.trie
        for letter in word:
            if letter in self.chars:
                self.chars[letter] += 1
            else:
                self.chars[letter] = 1
            if letter in temp_trie:
                temp_trie = temp_trie[letter]
            else:
                temp_trie = temp_trie.setdefault(letter, {})
        temp_trie[self._end] = 1
        return temp_trie



