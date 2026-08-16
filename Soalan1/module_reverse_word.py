# Fungsi untuk reverse urutan words dalam satu string
def word_list(input_string):
    # Pisahkan string kepada list of words
    words = input_string.split()
    # Balik urutan words dan gabung balik dengan space
    reverse_word = " ".join(reversed(words))
    # Return hasil yang sudah dibalik
    return reverse_word


# Fungsi untuk cetak hasil
def display():
    # Panggil word_list() dan cetak hasilnya
    print(word_list("hello .py"))


# Jalankan fungsi display()
display()