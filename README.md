### Micropython Pong

#### Overview:
PyAreSquare Pong is a single-player pong game designed for the Raspberry Pi Pico with an SSD1306 OLED display. The game combines classic pong mechanics with modern features such as an aimbot option, a dynamic score display, and engaging animations. Created by Satej Gandre, the game offers a mix of challenge and entertainment.

#### Features:
1. **Simple Controls**: 
    - The game uses two buttons connected to GPIO 0 and GPIO 1 for paddle movement. Button A (GPIO 0) moves the paddle left, and Button B (GPIO 1) moves it right.
    
2. **Dynamic Paddle Movement**: 
    - The paddle is 20 pixels wide and 4 pixels high. It starts at the middle of the screen and can move left or right based on button inputs.
    - The paddle's position is updated smoothly with a step of 4 pixels per input, ensuring responsive control.

3. **Ball Physics**:
    - The ball starts from the center of the screen with a random direction and speed.
    - It bounces off the walls and the paddle. The ball's speed and direction change slightly on each paddle hit to add randomness to its movement.
    - If the ball goes out of bounds (passes the paddle), the player loses a life.

4. **Score and Lives Display**:
    - The current score is displayed at the top left of the screen.
    - A horizontal line is drawn at \( y = 10 \) to separate the score area from the game area.
    - A lives bar is displayed at the top right, showing the remaining lives visually.
    
5. **Splash Screen**:
    - The game starts with a splash screen displaying "PyAreSquare 2024" and "Pong" with smooth downward scrolling text. The game starts when any button is pressed.

6. **Restart Option**:
    - After the game over sequence, the player is prompted to restart the game. Pressing any button will reset the game and allow for a new playthrough.

#### Easter Eggs:
1. **Creator Credits**:
    - In the game over sequence, the credits show "Created by: Satej Gandre" with a smooth scrolling effect, adding a personal touch from the developer.
    
2. **Hidden Aimbot Activation**:
    - The aimbot feature is subtly hinted at by the "aimbot" function name. It activates only when both buttons are pressed simultaneously, giving players a hint of an easier mode if they explore the controls.

### Detailed Code Description:

#### Initialization:
- The game initializes the I2C communication for the SSD1306 display and configures the buttons for input.
- The paddle and ball parameters are set, including positions and velocities.

#### Functions:
- **aimbot()**: Moves the paddle towards the ball if both buttons are pressed.
- **draw()**: Clears the screen and redraws the paddle, ball, horizontal line, score, and lives bar.
- **update_paddle()**: Updates the paddle position based on button inputs.
- **update_ball()**: Updates the ball's position and checks for collisions with walls, paddle, and out-of-bounds conditions.
- **reset_game()**: Resets the ball and paddle positions and checks for game over conditions.
- **game_over_animation()**: Displays the game over sequence with scrolling text.
- **mainloop()**: The main game loop that includes the splash screen, game logic, and aimbot functionality.

#### Main Game Loop:
- **Splash Screen**: Displays the initial splash screen with "PyAreSquare 2024" and "Pong" text. The game starts when a button is pressed.
- **Game Loop**: Continuously updates paddle and ball positions, redraws the screen, and checks for game over conditions.
