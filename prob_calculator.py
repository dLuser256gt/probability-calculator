import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(0, value):
        self.contents.append(key)

  def draw(self, num_balls_draw):
    if num_balls_draw < len(self.contents):
      balls = []
      for i in range(0, num_balls_draw):
        random_ball = random.randint(0, len(self.contents) - 1)
        balls.append(self.contents.pop(random_ball))

      return balls
    else:
      return self.contents

  def __str__(self):
    return 'Hat contents: ' + ', '.join(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  succes = 0  #Number of succesful experiments
  probability = 0

  # Create a list of expexcted_balls
  list_expected = []
  for key, value in expected_balls.items():
    for i in range(0, value):
      list_expected.append(key)

  # Here we do experiments
  for i in range(0, num_experiments):
    copy_hat = copy.deepcopy(hat)
    copy_expected = copy.copy(list_expected)
    drawn_balls = copy_hat.draw(num_balls_drawn)  # drawn the balls
    for ball in drawn_balls:
        for j in range(0,len(copy_expected)):
            if ball == copy_expected[j]:
                copy_expected.pop(j)
                break
    if copy_expected == []:
        succes += 1
    

  probability = succes / num_experiments
  return probability