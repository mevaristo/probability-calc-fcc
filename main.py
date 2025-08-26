import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [item for sublist in ([key for _ in range(value)] for key, value in kwargs.items()) for item in sublist]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

if __name__ == '__main__':
    hat = Hat(red=4, green=2, blue=0)