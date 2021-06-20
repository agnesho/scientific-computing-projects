import copy
import random

class Hat:
  
  def __init__(self, **kwargs):
    contents = list()
    for k, v in kwargs.items():
      for i in range(v):
        contents.append(k)
    self.contents = contents
  
  def draw(self, number=1):
    removed = list()
    # Number of balls to draw does not exceed available quantity
    if number >= len(self.contents):
      removed = self.contents
    else:
      for i in range(number):
        choice = random.choice(self.contents)
        removed.append(choice)
        self.contents.pop(self.contents.index(choice))
    return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  
  # Draw balls N (num_experiments) times
  for i in range(num_experiments):
    result = True
    hat_obj = copy.deepcopy(hat)
    drawn = hat_obj.draw(num_balls_drawn)
    drawn_dict = {ball: drawn.count(ball) for ball in set(drawn)}

    for k, v in expected_balls.items():
      if k not in drawn_dict or drawn_dict[k] < v:
        result = False
        break

    if result == True:
      M += 1

  return M/num_experiments