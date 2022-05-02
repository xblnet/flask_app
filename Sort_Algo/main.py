import math
import pygame
import random
pygame.init()

class Drawwindow():
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    BACKGROUND_COLOR = WHITE
    GRADIANTS = [
        (128,128,128),
        (160,160,160),
        (192,192,192),
    ]

    FONT = pygame.font.SysFont('comicsans',20)
    LARGE_FONT = pygame.font.SysFont('comicsans',30)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, list):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithm Display")
        self.set_list(list)

    def set_list(self, list):
        self.list = list
        self.min_val = min(list)
        self.max_val = max(list)
        self.block_width = round(self.width - self.SIDE_PAD) / len(list)
        self.block_height = math.floor(self.height - self.TOP_PAD) / (self.max_val - self.min_val)
        self.start_x = self.SIDE_PAD // 2
def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Decending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 45))

    sorting = draw_info.FONT.render("I - Insertion Sort | B Bubble Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 75))


    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions = {}, clear_bg = False):
    list = draw_info.list

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD //2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, draw_info.height -draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)
    
    for i, val in enumerate(list):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIANTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

        if clear_bg:
            pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    list = []
    for _ in range(n):
        val = random.randint(min_val , max_val)
        list.append(val)

    return list

def bubble_sort(draw_info, ascending = True):
    list = draw_info.list

    for i in range(len(list) -1):
        for j in range(len(list) - 1 - i):
            num1 = list[j]
            num2 = list[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                list[j], list[j + 1] = list [j + 1], list[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True

def insertion_sort(draw_info, ascending = True):
    list = draw_info.list

    for i in range(1,  len(list)):
        current = list[i]

        while True:
            ascending_sort = i > 0 and list[i - 1] > current and ascending
            decending_sort = i > 0 and list[i - 1] > current and not ascending

            if not ascending_sort and not decending_sort:
                break
            list[i] = list[i - 1]
            i = i - 1
            list[i] = current
            draw_list(draw_info,{i: draw_info.GREEN, i -1: draw_info.RED}, True)
            yield True


def main():
    run = True
    clock = pygame.time.Clock()
    n = 50
    min_val = 0
    max_val= 100

    list = generate_starting_list(n, min_val, max_val)
    draw_info = Drawwindow(800,600,list)
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)
        
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False

        else:           
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                list = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(list)
                sorting = False

            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"

    pygame.quit()

if __name__ == "__main__":
    main()
