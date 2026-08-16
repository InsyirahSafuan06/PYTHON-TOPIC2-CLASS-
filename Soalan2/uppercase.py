# Class untuk handle operasi string
class StringHandler:

    # Constructor - jalankan apabila object dibuat
    def __init__(self):
        # Initialize variable untuk simpan string
        self.string_word = ""

    # Method untuk terima input string daripada user
    def input_String(self):
        # Minta user input dan simpan
        self.string_word = input("Enter a string: ")

    # Method untuk cetak string dalam huruf besar
    def print_String(self):
        # Tukar kepada uppercase dan cetak
        print(self.string_word.upper())


# Buat object dari class
Word = StringHandler()
# Terima input dari user
Word.input_String()
# Cetak dalam huruf besar
Word.print_String()