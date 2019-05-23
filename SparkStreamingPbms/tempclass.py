class color:
    def __init__(self, color):
        self.color = color

    def print_color(self):
        print (self.color)

mycolor = color("red")

print (mycolor.print_color())