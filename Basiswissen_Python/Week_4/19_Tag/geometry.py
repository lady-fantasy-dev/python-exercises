class Room:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        
    def show_info(self):
        print(f"The room is {self.length} cm long, {self.width} cm wide, and {self.height} cm high.")
        
    def area(self):
        print("The room has an area of", self.length * self.width, "cm²")
    
    def volume(self):
        print("The room has a volume of", self.length * self.width * self.height, "cm³")