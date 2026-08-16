# Fungsi untuk terima input panjang daripada user
def input_length():
    # Minta input dan tukar kepada float
    length_value = float(input("Enter length: "))
    return length_value


# Fungsi untuk terima input lebar daripada user
def input_width():
    # Minta input dan tukar kepada float
    width_value = float(input("Enter width: "))
    return width_value


# Class untuk represent rectangle
class Rectangle:

    # Constructor - jalankan apabila object dibuat
    def __init__(self, length, width):
        # Simpan length (nilai positif sahaja)
        self.length = abs(length)
        # Simpan width (nilai positif sahaja)
        self.width = abs(width)

    # Method untuk kira luas rectangle
    def area(self):
        # Luas = panjang × lebar
        result = self.length * self.width
        return result


# Jalankan program
# Terima input panjang
length_area = input_length()
# Terima input lebar
width_area = input_width()

# Buat object Rectangle
rect = Rectangle(length_area, width_area)
# Cetak hasil luas
print("Area:", rect.area())