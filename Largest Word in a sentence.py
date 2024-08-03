#Find Largest word in a sentence
def LargestWord(sentence):
    words=sentence.split(' ')
    maxlen=0
    for word in words:
    if len(word)>maxlen:
        maxlen=len(word)
        longword=word
    print(word)
sentence=input()
LargestWord(sentence)