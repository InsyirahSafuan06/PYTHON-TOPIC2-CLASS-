class StringReverser:
    def __init__(self, input_string):
        self.words = input_string  # simpan string asal

    def reverse(self):
        words = self.words.split()  # pisahkan string kepada list of words
        return " ".join(reversed(words))  # balik urutan words, gabung balik


#declare variable text_string dengan nilai "hello .py"
text_string = "hello .py"
#object bernama word_value dari class StringReverser, panggil __init__ dengan text_string
word_value = StringReverser(text_string) 
result = word_value.reverse()  # panggil method reverse()

print("Input string  :", text_string)
print("Expected Output:", result)