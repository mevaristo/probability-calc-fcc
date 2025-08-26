import copy
import random

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = [item for sublist in \
            ([key for _ in range(value)] for key, value in kwargs.items()) \
                for item in sublist]
    
    def draw(self, amount: int) -> list[str]:
        draw_list = []
        for _ in range(amount):
            if not self.contents:
                return draw_list
            draw_list.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
            
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

if __name__ == '__main__':
    hat = Hat(red=4, green=2, blue=2, cyan=2, magenta=3, black=8, white=6, gray=4, purple=3, golden=3, silver=4, platinum=1, crystal=2)
    print(hat.draw(0))