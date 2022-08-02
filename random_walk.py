
from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a random walk"""

        self.num_points = num_points

        # All walks start at (0,0). Both co-ordinates are lists which will be filled as the choice() function runs against the data

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        #Keep taking steps until walk reaches the desired length

        while len(self.x_values)< self.num_points:

            #Decide which direction to go and how far you go in that direction

            
            x_step = self.get_step()
          
            y_step = self.get_step()

            # Reject moves that go nowhere

            if x_step == 0 and y_step == 0:
                continue

            x= self.x_values[-1] + x_step
            y= self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):

        direction = choice([1,-1])
        distance = choice([0,1,2,3,4,5,6,7,8])
        step = direction * distance

        return step

