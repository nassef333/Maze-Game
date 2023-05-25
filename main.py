# Imports the main Pygame module, which provides functionalities for game development.
import pygame

# Imports the time module, which provides functions for working with time-related operations.
import time

# Imports the sys module, which provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import sys

# Imports the random module, which provides functions for generating random numbers and making random selections.
import random

# Imports all the constants and classes from the pygame.
# locals module, which includes definitions for Pygame-specific events, key constants, and other constants used in Pygame programming.
# This allows easy access to these constants without having to prefix them with the module name. For example, QUIT instead of pygame.locals.QUIT.
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
# Sets the width of the game screen to 640 pixels.
screen_width = 640
# Sets the height of the game screen to 480 pixels.
screen_height = 480
# Creates the game window with the specified width and height.
screen = pygame.display.set_mode((screen_width, screen_height))
# Sets the title of the game window to "Maze Game".
pygame.display.set_caption("Maze Game")

# Set the maze dimensions
# Sets the number of cells in the maze horizontally to 21.
maze_width = 29
# Sets the number of cells in the maze vertically to 25.
maze_height = 25

# Calculate the cell size based on the screen size and maze dimensions
# Calculates the width of each cell in the maze based on the screen width and maze width.
cell_width = screen_width // maze_width
# Calculates the height of each cell in the maze based on the screen height and maze height.
cell_height = screen_height // maze_height

# Load the images
# Scales the treasure image to match the size of a single cell in the maze.
player_image = pygame.image.load("player.png")
# Scales the treasure image to match the size of a single cell in the maze.
player_image = pygame.transform.scale(player_image, (cell_width, cell_height))
# Loads the image file "treasure.png" and converts it to the appropriate format for Pygame.
treasure_image = pygame.image.load("treasure.png")
# Scales the treasure image to match the size of a single cell in the maze.
treasure_image = pygame.transform.scale(treasure_image, (cell_width, cell_height))

# Set the player's starting position
# Sets the initial x-coordinate of the player's position in the maze.
player_x = 1
# Sets the initial y-coordinate of the player's position in the maze.
player_y = 1

# Set the end point position
# Sets the x-coordinate of the endpoint position in the maze, which is two cells less than the maze width.
end_x = maze_width - 2
# Sets the y-coordinate of the endpoint position in the maze, which is two cells less than the maze height.
end_y = maze_height - 2

# Set the reward (treasure) position
# Calculates the x-coordinate of the reward (treasure) position in pixels by multiplying the endpoint x-coordinate with the cell width.
reward_x = end_x * cell_width
# Calculates the y-coordinate of the reward (treasure) position in pixels by multiplying the endpoint y-coordinate with the cell height.
reward_y = end_y * cell_height

# Set the game timer
# Records the current time as the start time of the game.
start_time = time.time()

# Sets the time limit for the game to 60 seconds.
time_limit = 60  # in seconds

# Set up font
# Creates a Pygame font object with a size of 36 pixels.
font = pygame.font.Font("Pacifico-Regular.ttf", 36)

# Generate the maze using Recursive Backtracking algorithm
# Initializes the maze as a 2D list filled with "X" (representing walls) using a list comprehension.
maze = [["X" for _ in range(maze_width)] for _ in range(maze_height)]


def generate_maze(x, y):
    """
        Generates a randomized maze using Recursive Backtracking algorithm.
        The provided code snippet is a recursive function `generate_maze` that implements the Recursive Backtracking algorithm to generate a randomized maze. Here's how the function works:
    1. The function takes two parameters, `x` and `y`, which represent the coordinates of the current cell in the maze.

    2. The function marks the current cell as a path by setting `maze[y][x]` to `" "`. In this implementation, `"X"` represents a wall, and `" "` represents a path.

    3. The function creates a list of directions by adding four possible neighboring cells to the `directions` list: above `(x, y - 2)`, below `(x, y + 2)`, left `(x - 2, y)`, and right `(x + 2, y)`. The cells are separated by a distance of 2 to leave space for walls between them.

    4. The function shuffles the `directions` list randomly to determine the order in which the neighboring cells will be visited.

    5. The function iterates over the shuffled `directions` list and checks if each neighboring cell is within the boundaries of the maze (`0 <= new_x < maze_width` and `0 <= new_y < maze_height`) and if it is currently a wall (`maze[new_y][new_x] == "X"`).

    6. If the conditions in step 5 are satisfied for a neighboring cell, the function proceeds to create a path between the current cell and the neighboring cell.

    - If the neighboring cell is in the same column as the current cell (`new_x == x`), the function sets the cell between them as a path by setting `maze[max(y, new_y) - 1][x]` to `" "`. This creates a vertical path.

    - If the neighboring cell is in the same row as the current cell (`new_y == y`), the function sets the cell between them as a path by setting `maze[y][max(x, new_x) - 1]` to `" "`. This creates a horizontal path.

    7. After creating a path between the current cell and a neighboring cell, the function recursively calls itself with the coordinates of the neighboring cell (`generate_maze(new_x, new_y)`). This process continues until there are no more unvisited neighboring cells.

    The generate_maze(x, y) function stops recursion when there are no more valid paths to explore from the current cell (x, y). This occurs when all neighboring cells have already been visited or are outside the bounds of the maze.
    By using recursion and backtracking, the algorithm explores each cell in the maze and creates paths by removing walls between cells. The result is a randomized maze with a single path from the starting cell to the ending cell.
    By backtracking and returning from each recursive call, the function eventually completes its execution and returns to the initial call, effectively stopping the recursion. At this point, the entire maze has been generated with paths connecting the start and end points.

        Args:
            x (int): The x-coordinate of the current cell.
            y (int): The y-coordinate of the current cell.
    """
    maze[y][x] = " "

    directions = [(x, y - 2), (x, y + 2), (x - 2, y), (x + 2, y)]
    random.shuffle(directions)

    for new_x, new_y in directions:
        if (
            0 <= new_x < maze_width
            and 0 <= new_y < maze_height
            and maze[new_y][new_x] == "X"
        ):
            if new_x == x:
                maze[max(y, new_y) - 1][x] = " "
            else:
                maze[y][max(x, new_x) - 1] = " "

            generate_maze(new_x, new_y)


def draw_maze():
    """Draws the maze on the screen using rectangles."""
    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x] == "X":
                pygame.draw.rect(
                    screen,
                    (198, 173, 148),
                    (x * cell_width, y * cell_height, cell_width, cell_height),
                )
            elif maze[y][x] == " ":
                pygame.draw.rect(
                    screen,
                    (234, 240, 206),
                    (x * cell_width, y * cell_height, cell_width, cell_height),
                )


def draw_player():
    """Draws the player on the screen using a 2D player icon image."""
    player_rect = player_image.get_rect()
    player_rect.topleft = (player_x * cell_width, player_y * cell_height)
    screen.blit(player_image, player_rect)


def draw_treasure():
    """Draws the treasure on the screen using a 2D treasure icon image."""
    treasure_rect = treasure_image.get_rect()
    treasure_rect.topleft = (reward_x, reward_y)
    screen.blit(treasure_image, treasure_rect)


def check_win():
    """Checks if the player has reached the end point."""
    return player_x == end_x and player_y == end_y


def check_lose():
    """Checks if the game time has exceeded the time limit."""
    elapsed_time = time.time() - start_time
    return elapsed_time > time_limit


def display_message(caption, message):
    """
    Displays a pop-up message on the screen using the provided caption and message.

    Args:
        caption (str): The caption of the window.
        message (str): The message to be displayed.
    """
    pygame.display.set_caption(caption)
    message_surface = font.render(message, True, (68, 56, 80))
    message_rect = message_surface.get_rect(
        center=(screen_width // 2, screen_height // 2)
    )
    screen.blit(message_surface, message_rect)
    pygame.display.update()
    pygame.time.wait(2000)  # Pause for 2 seconds to show the message


# Generate the maze using Recursive Backtracking algorithm
generate_maze(player_x, player_y)

# Game loop
running = True
clock = pygame.time.Clock()
animation_speed = 10

while running:
    # Handle events
    # This part handles the events, such as quitting the game when the window is closed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player movement
    # This part handles the player movement based on the arrow keys pressed.
    # It checks if the movement is valid by verifying that the cell in the desired direction is empty.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if maze[player_y - 1][player_x] == " ":
            player_y -= 1
    elif keys[pygame.K_DOWN]:
        if maze[player_y + 1][player_x] == " ":
            player_y += 1
    elif keys[pygame.K_LEFT]:
        if maze[player_y][player_x - 1] == " ":
            player_x -= 1
    elif keys[pygame.K_RIGHT]:
        if maze[player_y][player_x + 1] == " ":
            player_x += 1

    # This part clears the screen and then draws the maze, player, and treasure on the screen.
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the maze
    draw_maze()

    # Draw the player
    draw_player()

    # Draw the treasure
    draw_treasure()

    # Check for win condition
    # This part checks if the player has reached the treasure (win condition).
    # If the win condition is met, it stops the game loop, waits for a second to display the final position, and then shows a pop-up message for winning.
    if check_win():
        running = False
        pygame.time.wait(1000)  # Pause for a second to see the final position
        pygame.mixer.music.load("win_music.mp3")
        pygame.mixer.music.play()
        # Display pop-up message for winning
        display_message(
            "Maze Game - You Win!", "Congratulations! You found the treasure!"
        )

    # Check for lose condition
    # This part checks if the time limit has been exceeded (lose condition).
    # If the lose condition is met, it stops the game loop and displays a pop-up message for losing.
    if check_lose():
        running = False
        # Display pop-up message for losing
        pygame.mixer.music.load("lose_music.mp3")
        pygame.mixer.music.play()
        display_message(
            "Maze Game - You Lose!", "Time's up! You didn't find the treasure."
        )

    # Update the screen
    # This part updates the screen to show the changes made, and it limits the frames per second to control the animation speed.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(animation_speed)

# Quit the game
pygame.quit()
