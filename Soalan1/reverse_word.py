# Import module untuk guna fungsi word_list()
import module_reverse_word

# Class untuk reverse string word by word
class StringReverser:
    
    # Constructor - jalankan apabila object dibuat
    def __init__(self, input_string):
        # Simpan string dalam variable instance
        self.input_string = input_string

    # Method untuk reverse string
    def reverse(self):
        # Panggil fungsi word_list() dari module_reverse_word
        return module_reverse_word.word_list(self.input_string)


# Buat string test
text_string = "hello .py"
# Buat object StringReverser
reverser = StringReverser(text_string)
# Cetak input dan output
print("Input :", text_string)
print("Output:", reverser.reverse())