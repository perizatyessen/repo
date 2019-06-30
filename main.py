import trie

file=open("text.txt","r+")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
wordcount={}
substr={}
no_punct = ""

for line in file:
    for char in line:
        if char.upper() not in punctuations:
            no_punct = no_punct + char.upper()

#print(no_punct)

for word in no_punct.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    substr[k] = 1
    for k1,v1 in wordcount.items():
        if(k in k1):
            substr[k] += v1
#for key,val in substr.items():
    #print(key,val)
my_trie = trie.Trie(no_punct)
print("Most frequent word  is'",my_trie.word,"' and it's count is", my_trie.max)
print("Most frequent letter is'",my_trie.letter,"' and it's count is", my_trie.maxlet)


