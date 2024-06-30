# drawing.py

import pygame
import math
from constants import *
from utils import *

# Initialize pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SandTable Simulator")

# Function to draw the circle with CIRCLE_COLOR
def draw_circle():
    pygame.draw.circle(screen, CIRCLE_COLOR, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), SCREEN_WIDTH // 2)

# Function to calculate RGB values based on polar coordinates
def calculate_rgb(theta, rho):
    normalized_theta = (theta + math.pi) / (2 * math.pi)
    hue = normalized_theta % 1.0
    saturation = RGB_PATH_SATURATION
    value = RGB_PATH_VALUE

    c = value * saturation
    x = c * (1 - abs((hue * 6) % 2 - 1))
    m = value - c

    if 0 <= hue < 1/6:
        r, g, b = c, x, 0
    elif 1/6 <= hue < 2/6:
        r, g, b = x, c, 0
    elif 2/6 <= hue < 3/6:
        r, g, b = 0, c, x
    elif 3/6 <= hue < 4/6:
        r, g, b = 0, x, c
    elif 4/6 <= hue < 5/6:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return (int((r + m) * 255), int((g + m) * 255), int((b + m) * 255))

# Function to draw the path on screen
def draw_path(path):
    if USE_RGB_PATH:
        draw_path_rgb(path)
    else:
        draw_path_single_color(path, "#FFE0B5")

# Function to draw the path on screen with RGB color
def draw_path_rgb(path):
    for i in range(1, len(path)):
        theta1, rho1 = path[i - 1]
        theta2, rho2 = path[i]
        (x1, y1) = polar_to_cartesian(theta1, rho1)
        (x2, y2) = polar_to_cartesian(theta2, rho2)

        color = calculate_rgb(theta1, rho1)

        pygame.draw.line(screen, color,
                         (int(x1 * SCREEN_WIDTH/2 + SCREEN_WIDTH/2), int(y1 * SCREEN_HEIGHT/2 + SCREEN_HEIGHT/2)),
                         (int(x2 * SCREEN_WIDTH/2 + SCREEN_WIDTH/2), int(y2 * SCREEN_HEIGHT/2 + SCREEN_HEIGHT/2)),
                         PATH_THICKNESS)

# Function to draw the path on screen with a single color
def draw_path_single_color(path, color):
    for i in range(1, len(path)):
        theta1, rho1 = path[i - 1]
        theta2, rho2 = path[i]
        (x1, y1) = polar_to_cartesian(theta1, rho1)
        (x2, y2) = polar_to_cartesian(theta2, rho2)

        pygame.draw.line(screen, color,
                         (int(x1 * SCREEN_WIDTH/2 + SCREEN_WIDTH/2), int(y1 * SCREEN_HEIGHT/2 + SCREEN_HEIGHT/2)),
                         (int(x2 * SCREEN_WIDTH/2 + SCREEN_WIDTH/2), int(y2 * SCREEN_HEIGHT/2 + SCREEN_HEIGHT/2)),
                         PATH_THICKNESS)
