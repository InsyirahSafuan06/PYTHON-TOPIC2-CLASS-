# Fungsi untuk terima input radius daripada user
def value_circle():
    # Minta input dan tukar kepada float
    radius_value = float(input("Enter radius: "))
    return radius_value


# Class untuk represent circle
class Circle:

    # Constructor - jalankan apabila object dibuat
    def __init__(self, radius):
        # Simpan radius dalam variable instance
        self.radius = radius

    # Method untuk kira luas bulatan
    def area(self):
        # Luas = π × radius² (gunakan 3.14159 untuk π)
        return round(3.14159 * self.radius ** 2, 2)

    # Method untuk kira lilitan bulatan
    def perimeter(self):
        # Lilitan = 2 × π × radius (gunakan 3.14159 untuk π)
        return round(2 * 3.14159 * self.radius, 2)


# Jalankan program
# Terima input radius daripada user
radius = value_circle()

# Buat object Circle
circle = Circle(radius)

# Cetak hasil luas dan lilitan
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())