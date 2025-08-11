class Anagram:
    def __init__(self,text):
        self.text = text

    def is_anagram(self):
        list1 = list(self.text)
        length = len(self.text)
        for i in range(length-1):
            for j in range(length -i - 1):
                if list1[j] > list1[j+1]:
                    list1[j],list1[j+1] = list1[j+1],list1[j]
        return list1

word1 = Anagram("madam")
word2 = Anagram("mmaad")


if word1.is_anagram() == word2.is_anagram():
    print(True)

else:
    print(False)    






        