# main.py

import pygame
import os
from constants import *
from utils import *
from drawing import *

# Main function
def main():
    clock = pygame.time.Clock()

    # Get list of input files
    input_files = get_input_files(INPUT_FOLDER)

    if not input_files:
        print(f"No '.thr' files found in '{INPUT_FOLDER}' folder.")
        return

    # Main loop
    running = True
    file_index = 0  # Index to track current file
    index = 0  # Index to track current position in path
    frame_count = 0  # Counter to track frames
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Read coordinates from current file
        path = read_coordinates(input_files[file_index])

        # Draw the path up to the current index
        draw_path(path[:index])

        # Calculate current and next positions
        if index < len(path) - 1:
            theta_current, rho_current = path[index]
            theta_next, rho_next = path[index + 1]
        else:
            # Wrap around if reached the end of path
            theta_current, rho_current = path[-1]
            theta_next, rho_next = path[0]

        # Interpolate between current and next positions based on frame_count
        fraction = frame_count / BALL_SPEED
        theta = theta_current + fraction * (theta_next - theta_current)
        rho = rho_current + fraction * (rho_next - rho_current)

        # Draw the current position as a ball
        (x, y) = polar_to_cartesian(theta, rho)
        pygame.draw.circle(screen, BALL_COLOR,
                           (int(x * SCREEN_WIDTH/2 + SCREEN_WIDTH/2), int(y * SCREEN_HEIGHT/2 + SCREEN_HEIGHT/2)),
                           BALL_RADIUS)

        pygame.display.flip()
        clock.tick(60)  # Cap the frame rate at 60 FPS

        # Increment frame_count
        frame_count += 1

        # If frame_count exceeds ball_speed, move to the next index in path
        if frame_count >= BALL_SPEED:
            index += 1
            frame_count = 0

        # Wrap around if reached the end of path
        if index >= len(path):
            index = 0

            # Move to the next file
            file_index = (file_index + 1) % len(input_files)

    pygame.quit()

if __name__ == "__main__":
    main()
