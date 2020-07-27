#                        Sorting With Fun
# ----------------------------------------------------------------------

import pygame
import random


pygame.mixer.init()
pygame.mixer.music.load('sound2.mp3')
button_press = pygame.mixer.Sound('sound1.wav')

pygame.mixer.music.play(-1)

pygame.init()

screen_width = 1200
screen_height = 600

# Other Variables
z = 0
flag = 0
flag_1 = 0
count_1 = 0
number_of_array = 10
user_choice = 600
types_of_sort = 1
sorting = 'BUBBLE'

# Color Generate
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
yellow_red_1 = (255, 255, 0)
yellow_red_2 = (255, 242, 0)
yellow_red_3 = (255, 229, 0)
yellow_red_4 = (255, 216, 0)
yellow_red_5 = (255, 203, 0)
yellow_red_6 = (255, 190, 0)
yellow_red_7 = (255, 177, 0)
yellow_red_8 = (255, 164, 0)
yellow_red_9 = (255, 151, 0)
yellow_red_10 = (255, 138, 0)
yellow_red_11 = (255, 125, 0)
yellow_red_12 = (255, 112, 0)
yellow_red_13 = (255, 99, 0)
yellow_red_14 = (255, 86, 0)
yellow_red_15 = (255, 73, 0)
yellow_red_16 = (255, 60, 0)
yellow_red_17 = (255, 47, 0)
yellow_red_18 = (255, 34, 0)
yellow_red_19 = (255, 15, 0)
yellow_red_20 = (255, 0, 0)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

# Font Generate
font_40 = pygame.font.SysFont(None, 40)
font_100 = pygame.font.SysFont(None, 100)
font_30 = pygame.font.SysFont(None, 30)

exit_game = False

# Creating Game Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sorting With Fun")
pygame.display.update()

def loading():
    text_screen('**********      Sort With Fun      **********', green, 0, 100, 1)
    pygame.display.update()
    for p in range(12):
        terminate_in_middle()
        pygame.draw.line(gameWindow, white, (100 * p, 450), (100 * p + 100, 450), 20)

        pygame.time.wait(1000)
        pygame.display.update()

def welcome_screen():
    gameWindow.fill(black)
    pygame.draw.line(gameWindow, white, (0, 30), (screen_width, 30), 5)
    pygame.draw.line(gameWindow, white, (0, 40), (screen_width, 40), 5)

    text_screen('**********      Sort With Fun      **********', green, 0, 60, 1)
    pygame.draw.line(gameWindow, white, (0, 150), (screen_width, 150), 5)
    pygame.draw.line(gameWindow, white, (0, 160), (screen_width, 160), 5)

    text_screen('   ALL TYPES OF VISUAL SORTING', yellow, 10, 210, 1)

    pygame.draw.rect(gameWindow, green, [525, 350, 200, 100])
    text_screen('Enter', white, 590, 390, 2)

    pygame.draw.line(gameWindow, white, (0, 500), (screen_width, 500), 5)
    pygame.draw.line(gameWindow, white, (0, 510), (screen_width, 510), 5)


def game_navigation():
    gameWindow.fill(black)
    text_screen('**************      Sort With Fun      **************', green, 300, 10, 2)
    pygame.draw.line(gameWindow, white, (0, 50), (screen_width, 50), 5)

    pygame.draw.rect(gameWindow, yellow, [100, 55, 200, 50])
    text_screen('Generate', blue, 155, 60, 3)
    text_screen('New Array', black, 135, 80, 2)

    text_screen('Concentration =  ', blue, 355, 65, 2)

    pygame.draw.line(gameWindow, yellow_red_1, (600, 80), (613, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_2, (613, 80), (625, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_3, (625, 80), (638, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_4, (638, 80), (650, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_5, (650, 80), (663, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_6, (663, 80), (675, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_7, (675, 80), (668, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_8, (668, 80), (700, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_9, (700, 80), (713, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_10, (713, 80), (725, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_11, (725, 80), (738, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_12, (738, 80), (750, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_13, (750, 80), (763, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_14, (763, 80), (775, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_15, (775, 80), (788, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_16, (788, 80), (800, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_17, (800, 80), (813, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_18, (813, 80), (825, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_19, (825, 80), (838, 80), 10)
    pygame.draw.line(gameWindow, yellow_red_20, (838, 80), (850, 80), 10)

    pygame.draw.circle(gameWindow, red, (user_choice, 80), 15, 10)

    pygame.draw.rect(gameWindow, red, [1000, 55, 150, 50])
    text_screen('EXIT', black, 1045, 70, 2)

    pygame.draw.line(gameWindow, white, (0, 110), (screen_width, 110), 5)

    pygame.draw.rect(gameWindow, green, [25, 115, 150, 50])
    text_screen('Bubble', black, 50, 115, 2)
    text_screen('Sort', blue, 75, 145, 3)

    pygame.draw.rect(gameWindow, green, [225, 115, 150, 50])
    text_screen('Insertion', black, 240, 115, 2)
    text_screen('Sort', blue, 280, 145, 3)

    pygame.draw.rect(gameWindow, green, [425, 115, 150, 50])
    text_screen('Selection', black, 435, 115, 2)
    text_screen('Sort', blue, 475, 145, 3)

    pygame.draw.rect(gameWindow, green, [625, 115, 150, 50])
    text_screen('Quick', black, 660, 115, 2)
    text_screen('Sort', blue, 680, 145, 3)

    pygame.draw.rect(gameWindow, green, [825, 115, 150, 50])
    text_screen('Merge', black, 855, 115, 2)
    text_screen('Sort', blue, 875, 145, 3)

    pygame.draw.rect(gameWindow, green, [1025, 115, 150, 50])
    text_screen('Heap', black, 1060, 115, 2)
    text_screen('Sort', blue, 1080, 145, 3)

    pygame.draw.line(gameWindow, white, (0, 170), (screen_width, 170), 5)
    pygame.draw.line(gameWindow, white, (0, 180), (screen_width, 180), 5)


    pygame.draw.rect(gameWindow, yellow, [50, 200, 300, 250])
    text_screen(f'NUMBER OF ARRAY', black, 60, 225, 2)
    text_screen(f'= {number_of_array}', blue, 160, 260, 2)

    pygame.draw.line(gameWindow, black, (50, 300), (350, 300), 10)

    if types_of_sort == 1:
        sorting = 'BUBBLE'
    elif types_of_sort == 2:
        sorting = 'INSERTION'
    elif types_of_sort == 3:
        sorting = 'SELECTION'
    elif types_of_sort == 4:
        sorting = 'QUICK'
    elif types_of_sort == 5:
        sorting = 'MERGE'
    elif types_of_sort == 6:
        sorting = 'HEAP'

    text_screen('TYPE OF SORT', black, 90, 325, 2)
    pygame.draw.line(gameWindow, green, (60, 355), (340, 355), 5)

    text_screen(f'{sorting}', blue, 125, 365, 2)
    text_screen('SORT', red, 140, 410, 2)

    pygame.draw.rect(gameWindow, red, [100, 470, 200, 100])
    text_screen('SORT', black, 160, 505, 2)

    pygame.draw.rect(gameWindow, blue, [370, 200, 800, 380])

    pygame.draw.line(gameWindow, white, (0, 590), (screen_width, 590), 20)
    pygame.draw.line(gameWindow, white, (10, 0), (10, screen_height), 20)
    pygame.draw.line(gameWindow, white, (1190, 0), (1190, screen_height), 20)


def array_generation(array, position, count_1):
    breath = 800//len(array)
    count = 0
    for i in array:
        if count_1 == 0:
            pygame.draw.line(gameWindow, green, ((370+(breath-1)//2) + count * breath, i), ((370+(breath-1)//2) + count * breath, 550), breath-1 )
        elif count_1 == 1:
            if count in position:
                pygame.draw.line(gameWindow, yellow, ((370+(breath-1)//2) + count * breath, i), ((370+(breath-1)//2) + count * breath, 550), breath-1 )
            else:
                pygame.draw.line(gameWindow, red, ((370+(breath-1)//2) + count * breath, i), ((370+(breath-1)//2) + count * breath, 550), breath-1)

        count += 1


def terminate_in_middle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if flag == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and event.pos[0] > 1000 and event.pos[0] < 1150 and event.pos[1] > 55 and event.pos[1] < 105:
                quit()

def bubble_sort(arr, count_1):
    count_1 = 1
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            terminate_in_middle()

            game_navigation()
            array_generation(arr, [], count_1)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                array_generation(arr, [j, j+1], count_1)
            pygame.display.update()
            pygame.time.wait(100)

    count_1 = 0


def insertion_sort(arr, count_1):
    count_1 = 1
    for i in range(1, len(arr)):
        game_navigation()
        array_generation(arr, [], count_1)
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            terminate_in_middle()
            array_generation(arr, [j, j + 1], count_1)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        pygame.display.update()
        pygame.time.wait(100)
    count_1 = 0


def selection_sort(array, count_1):
    count_1 = 1

    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):

            terminate_in_middle()

            game_navigation()
            array_generation(arr, [], count_1)
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
        array_generation(arr, [i, min_idx], count_1)

        pygame.display.update()
        pygame.time.wait(100)

    count_1 = 0


def quick_sort(arr, low, high):
    count_1 = 1
    if low < high:
        i = (low - 1)
        pivot = arr[high]
        for j in range(low, high):
            terminate_in_middle()
            game_navigation()
            array_generation(arr, [], count_1)
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                array_generation(arr, [i, j], count_1)
            pygame.display.update()
            pygame.time.wait(100)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = (i + 1)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    count_1 = 0


def merge_sort(arr, l, r):
    count_1 = 1
    if l < r:
        m = (l + (r - 1)) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        n1 = m - l + 1
        n2 = r - m
        L = [0] * (n1)
        R = [0] * (n2)
        for i in range(0, n1):
            terminate_in_middle()
            L[i] = arr[l + i]
        for j in range(0, n2):
            terminate_in_middle()
            R[j] = arr[m + 1 + j]
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            terminate_in_middle()
            game_navigation()
            array_generation(arr, [], count_1)
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
                array_generation(arr, [k], count_1)
            else:
                arr[k] = R[j]
                j += 1
                array_generation(arr, [k], count_1)
            k += 1
            pygame.display.update()
            pygame.time.wait(100)
        while i < n1:
            terminate_in_middle()
            game_navigation()
            array_generation(arr, [], count_1)
            arr[k] = L[i]
            i += 1
            k += 1
            # array_generation(arr, [k], count_1)
            pygame.display.update()
            pygame.time.wait(100)
        while j < n2:
            terminate_in_middle()
            game_navigation()
            array_generation(arr, [], count_1)
            arr[k] = R[j]
            j += 1
            k += 1
            array_generation(arr, [], count_1)
            pygame.display.update()
            pygame.time.wait(100)

    count_1 = 0


def heapify(arr, n, i):
    count_1 = 1
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    array_generation(arr, [i], count_1)
    if l < n and arr[i] < arr[l]:
        largest = l
        array_generation(arr, [i, l], count_1)

    if r < n and arr[largest] < arr[r]:
        largest = r
        array_generation(arr, [i, r], count_1)
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        array_generation(arr, [i, largest], count_1)
        heapify(arr, n, largest)
    pygame.display.update()
    # pygame.time.wait(100)


def heap_sort(arr):

    count_1 = 1

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        count_1 = 1
        terminate_in_middle()
        game_navigation()
        array_generation(arr, [i], count_1)
        heapify(arr, n, i)
        pygame.display.update()
        pygame.time.wait(100)

    for i in range(n - 1, 0, -1):
        count_1 = 1
        terminate_in_middle()
        game_navigation()
        array_generation(arr, [i], count_1)
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        pygame.display.update()
        pygame.time.wait(100)

    count_1 = 0


def press_sort(arr, count_1):
    terminate_in_middle()
    if types_of_sort == 1:
        bubble_sort(arr, count_1)
    elif types_of_sort == 2:
        insertion_sort(arr, count_1)
    elif types_of_sort == 3:
        selection_sort(arr, count_1)
    elif types_of_sort == 4:
        quick_sort(arr, 0, len(arr)-1)
    elif types_of_sort == 5:
        merge_sort(arr, 0, len(arr)-1)
    elif types_of_sort == 6:
        heap_sort(arr)


def text_screen(text, color, x, y, size):
    screen_text = font_40.render(text, True, color)
    if size == 1:
        screen_text = font_100.render(text, True, color)
    elif size == 3:
        screen_text = font_30.render(text, True, color)

    gameWindow.blit(screen_text, (x, y))

# Main loop


while not exit_game:

    if flag == 0 and z == 0:
        loading()
        z = 1

    if flag == 0:
        welcome_screen()

    if flag == 1:
        game_navigation()

    for event in pygame.event.get():
        button_press.play()
        if event.type == pygame.QUIT:
            exit_game = True

        # Enter Key
        if event.type == pygame.MOUSEBUTTONDOWN and flag == 0:
            if event.button == 1 and event.pos[0] > 525 and event.pos[0] < 725 and event.pos[1] > 350 and event.pos[1] < 450:
                # pygame.mixer.music.play()
                flag = 1

        # Generate New Array
        if flag == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and event.pos[0] > 100 and event.pos[0] < 300 and event.pos[1] > 55 and event.pos[1] < 105:
                # pygame.mixer.music.play()
                flag_1 = 1
                arr = []
                for i in range(number_of_array):
                    a = random.randint(200, 500)
                    arr.append(a)

        # Exit game
        if flag == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and event.pos[0] > 1000 and event.pos[0] < 1150 and event.pos[1] > 55 and event.pos[1] < 105:
                exit_game = True

        # Position of Circle
        if flag == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and event.pos[0] >= 600 and event.pos[0] <= 850 and event.pos[1] >= 70 and event.pos[1] <= 90:
                # pygame.mixer.music.play()
                user_choice = event.pos[0]
                if user_choice >= 600 and user_choice < 613:
                    number_of_array = 10
                elif user_choice >= 613 and user_choice < 625:
                    number_of_array = 20
                elif user_choice >= 625 and user_choice < 638:
                    number_of_array = 30
                elif user_choice >= 638 and user_choice < 650:
                    number_of_array = 40
                elif user_choice >= 650 and user_choice < 663:
                    number_of_array = 50
                elif user_choice >= 663 and user_choice < 675:
                    number_of_array = 60
                elif user_choice >= 675 and user_choice < 688:
                    number_of_array = 70
                elif user_choice >= 688 and user_choice < 700:
                    number_of_array = 80
                elif user_choice >= 700 and user_choice < 713:
                    number_of_array = 90
                elif user_choice >= 713 and user_choice < 725:
                    number_of_array = 100
                elif user_choice >= 725 and user_choice < 738:
                    number_of_array = 110
                elif user_choice >= 738 and user_choice < 750:
                    number_of_array = 120
                elif user_choice >= 750 and user_choice < 763:
                    number_of_array = 130
                elif user_choice >= 763 and user_choice < 775:
                    number_of_array = 140
                elif user_choice >= 775 and user_choice < 788:
                    number_of_array = 150
                elif user_choice >= 788 and user_choice < 800:
                    number_of_array = 160
                elif user_choice >= 800 and user_choice < 813:
                    number_of_array = 170
                elif user_choice >= 813 and user_choice < 825:
                    number_of_array = 180
                elif user_choice >= 825 and user_choice < 838:
                    number_of_array = 190
                elif user_choice >= 838 and user_choice < 850:
                    number_of_array = 200


        # Type of Sorting
        if flag == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            # pygame.mixer.music.play()
            if event.button == 1 and event.pos[0] >= 25 and event.pos[0] <= 175 and event.pos[1] >= 115 and event.pos[1] <= 165:
                types_of_sort = 1

            if event.button == 1 and event.pos[0] >= 225 and event.pos[0] <= 375 and event.pos[1] >= 115 and event.pos[1] <= 165:
                types_of_sort = 2

            if event.button == 1 and event.pos[0] >= 425 and event.pos[0] <= 575 and event.pos[1] >= 115 and event.pos[1] <= 165:
                types_of_sort = 3

            if event.button == 1 and event.pos[0] >= 625 and event.pos[0] <= 775 and event.pos[1] >= 115 and event.pos[1] <= 165:
                types_of_sort = 4

            if event.button == 1 and event.pos[0] >= 825 and event.pos[0] <= 975 and event.pos[1] >= 115 and event.pos[1] <= 165:
                types_of_sort = 5

            if event.button == 1 and event.pos[0] >= 1025 and event.pos[0] <= 1175 and event.pos[1] >= 115 and event.pos[1] <= 165:
                types_of_sort = 6

        if flag == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and event.pos[0] >= 100 and event.pos[0] <= 300 and event.pos[1] >= 470 and event.pos[1] <= 570 and flag_1 == 1:
                press_sort(arr, count_1)



    if flag_1 == 1:
        array_generation(arr, [], count_1)


    pygame.display.update()

