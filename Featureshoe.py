from ClassShoe import Shoe

class FeatureShoe(Shoe):
    def __init__(self, size, material, price, model, color):
        super().__init__(size, material, price, model)
        self.color = color

# Create an instance of the FeatureShoe class
Shoe1 = FeatureShoe("M", "Leather", 56, "MDKL", "Black")

# Access and print attributes of Shoe1
print("Size:", Shoe1.size)
print("Material:", Shoe1.material)
print("Price:", Shoe1.price)
print("Model:", Shoe1.model)
print("Color:", Shoe1.color)

