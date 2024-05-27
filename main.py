# A singleplayer pong game created by Satej Gandre
import machine
import ssd1306
import utime
import urandom

# Initialize I2C for the display
i2c = machine.I2C(0,scl = machine.Pin(17), sda = machine.Pin(16), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize buttons
button_a = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
button_b = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)

# Paddle and ball parameters
paddle_width = 20
paddle_height = 4
paddle_x = 86  # Start paddle in the middle
paddle_y = 60
ball_x = 64
ball_y = 32
ball_dx = 2
ball_dy = 2
score = 0
misses = 0
max_misses = 5

def aimbot():
    global paddle_x, ball_x
    if (not button_a.value()) and (not button_b.value()):
        if (paddle_x) < ball_x and (paddle_x+20) < ball_x and paddle_x < (128 - paddle_width):
            paddle_x += 4
        elif (paddle_x) > ball_x and (paddle_x+20) > ball_x and paddle_x > 0:
            paddle_x -= 4

def draw():
    oled.fill(0)
    oled.hline(0, 10, 128, 1)
    oled.fill_rect(paddle_x, paddle_y, paddle_width, paddle_height, 1)
    oled.fill_rect(int(ball_x), int(ball_y), 2, 2, 1)
    oled.rect(113, 0, 15, 7, 1)
    oled.fill_rect(113, 0, int(20*((max_misses-misses-1)/max_misses)), 7, 1)
    oled.text(f'Score: {score}', 0, 0)
    oled.show()

def update_paddle():
    global paddle_x
    if not button_a.value() and paddle_x > 0:
        paddle_x -= 4
    if not button_b.value() and paddle_x < (128 - paddle_width):
        paddle_x += 4

def update_ball():
    global ball_x, ball_y, ball_dx, ball_dy, score, misses
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= 126:
        ball_dx = -ball_dx
    if ball_y <= 11:
        ball_dy = -ball_dy
    # Ball collision with paddle
    if (paddle_y <= ball_y + 2 <= paddle_y + paddle_height and
        paddle_x <= ball_x <= paddle_x + paddle_width):
        ball_y = paddle_y - 2  # Ensure ball is positioned above the paddle
        ball_dy = -ball_dy
        # Add randomness to the ball's direction
        ball_dx += urandom.uniform(-1, 1)
        ball_dy += urandom.uniform(-1, 1)
        # Ensure the ball's speed is within reasonable bounds
        if ball_dx > 3:
            ball_dx = 3
        if ball_dx < -3:
            ball_dx = -3
        if ball_dy > 3:
            ball_dy = 3
        if ball_dy < -3:
            ball_dy = -3
        if (-0.6 < ball_dy) and (ball_dy < 0.6):
            ball_dy = [-0.6,0.6][urandom.randint(0,1)]
        if (-0.6 < ball_dx) and (ball_dx < 0.6):
            ball_dx = [-0.6,0.6][urandom.randint(0,1)]
        score += 1
        print(ball_dx)
        print(ball_dy)
    # Ball out of bounds
    if ball_y > 64:
        misses += 1
        reset_game()

def reset_game():
    global ball_x, ball_y, ball_dx, ball_dy, score, misses
    ball_x, ball_y = 64, 32
    ball_dx, ball_dy = 2, 2
    if misses >= max_misses:
        game_over_animation()
        # Reset variables
        misses = 0
        score = 0

def game_over_animation():
    for i in range(75):
        oled.fill(0)
        oled.text("Game Over", 25, i-10)
        oled.show()
        utime.sleep(0.05)
    for i in range(91):
        oled.fill(0)
        oled.text("Created by:", 25, i-26)
        oled.text("Satej Gandre", 18, i-10)
        oled.show()
        utime.sleep(0.05)
    for i in range(42):
        oled.fill(0)
        oled.text("Restart?", 32, i-10)
        oled.show()
        utime.sleep(0.05)
    while 1:
        if (not button_a.value()) or (not button_b.value()):
            break
    for i in range(33):
        oled.fill(0)
        oled.text("Restart?", 32, i+32)
        oled.show()
        utime.sleep(0.05)
    utime.sleep(1)

def mainloop():
    # Splashscreen
    for i in range(42):
        oled.fill(0)
        oled.text("PyAreSquare 2024",0,i-41)
        oled.text("Pong", 50, i-10)
        oled.show()
        utime.sleep(0.05)
    while 1:
        if (not button_a.value()) or (not button_b.value()):
            break
    for i in range(51):
        oled.fill(0)
        oled.text("PyAreSquare 2024",0,int(1.5*i))
        oled.text("Pong", 50, i+32)
        oled.show()
        utime.sleep(0.05)
    utime.sleep(1)
    while True: # Main gameloop
        aimbot()
        update_paddle()
        update_ball()
        draw()
        utime.sleep(0.01)
        
mainloop() # Start the game
