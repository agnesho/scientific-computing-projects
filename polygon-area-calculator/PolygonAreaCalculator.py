class Rectangle:
  
  def __init__(self, a, b):
    self.width = a
    self.height = b
    
  # instance of Rectangle represented as a string
  def __str__(self):
    return ("Rectangle(width={}, height={})".format(self.width, self.height))

  def set_width(self, x):
    self.width = x
  
  def set_height(self, y):
    self.height = y

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    # Limit width and height
    if self.width <= 50 and self.height <=  50:
      columns = self.width * "*" + '\n'
      output = columns * self.height
      return output
    else:
      return "Too big for picture."

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()
    

# Square is a subclass of Rectangle
class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side
  
  def set_height(self, side):
    self.width = side
    self.height = side

  # instance of Square represented as a string
  def __str__(self):
    return ("Square(side={})".format(self.width))