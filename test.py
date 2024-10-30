import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Square")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player variables
player_size = 50
player_x = WIDTH // 2 - player_size // 2  # Center horizontally
player_y = HEIGHT - player_size  # Start on the ground
player_velocity_y = 0  # Vertical velocity (will change when jumping)
gravity = 1  # Constant gravity pulling the player down
jump_strength = -30  # Strength of the jump (negative because up is negative in Pygame)
is_jumping = False  # Whether the player is currently jumping

FPS = 60  # Frames per second
clock = pygame.time.Clock()


# Function to handle player input and movement
def handle_player_input(keys_pressed, player_y, player_velocity_y, is_jumping):
    # Jump if spacebar is pressed and player is not already in the air
    if keys_pressed[pygame.K_SPACE] and not is_jumping:
        player_velocity_y = jump_strength  # Apply upward velocity
        is_jumping = True  # Set jumping flag to True

    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y

    # If the player hits the ground, reset the jump
    if player_y >= HEIGHT - player_size:
        player_y = HEIGHT - player_size  # Keep player on the ground
        player_velocity_y = 0  # Reset vertical velocity
        is_jumping = False  # Allow the player to jump again

    return player_y, player_velocity_y, is_jumping


# Function to draw the window and the player
def draw_window(player_x, player_y):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, (player_x, player_y, player_size, player_size))  # Draw the player square
    pygame.display.update()


# Main game loop
def main():
    global player_y, player_velocity_y, is_jumping
    run = True
    while run:
        clock.tick(FPS)  # Control frame rate

        # Event loop to handle quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Check which keys are pressed
        keys_pressed = pygame.key.get_pressed()

        # Handle player input and movement (function-based)
        player_y, player_velocity_y, is_jumping = handle_player_input(keys_pressed, player_y, player_velocity_y, is_jumping)

        # Draw everything
        draw_window(player_x, player_y)

    pygame.quit()


if __name__ == "__main__":
    main()
