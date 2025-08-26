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

def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int):
    success_count = 0
    
    for _ in range(num_experiments):
        hat_cp = copy.deepcopy(hat)
        draw = hat_cp.draw(num_balls_drawn)

        success_count += check_contains(draw, expected_balls)

    return success_count/num_experiments
            
def check_contains(draw: list[str], expected_balls: dict[str:int]) -> int:
    for key, value in expected_balls.items():
        for _ in range(value):
            if key not in draw:
                return 0
            draw.remove(key)
        
    return 1


if __name__ == '__main__':
    hat = Hat(red=4, green=2, blue=2, cyan=2, magenta=3, black=8, white=6, gray=4, purple=3, golden=3, silver=4, platinum=1, crystal=2)
    print(hat.draw(7))
    print(experiment(hat=hat,
                expected_balls={'platinum':1,'cyan':1},
                num_balls_drawn=5,
                num_experiments=20000))