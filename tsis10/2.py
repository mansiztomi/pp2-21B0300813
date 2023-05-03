import turtle
import time
import random
import sqlite3

# Connect to the database
conn = sqlite3.connect('snake_game.db')
c = conn.cursor()

# Create the user table
c.execute('''CREATE TABLE IF NOT EXISTS user
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL UNIQUE)''')

# Create the user_score table
c.execute('''CREATE TABLE IF NOT EXISTS user_score
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER NOT NULL,
              level INTEGER NOT NULL,
              score INTEGER NOT NULL,
              FOREIGN KEY (user_id) REFERENCES user(id))''')

delay = 0.1
score = 0
high_score = 0
current_level = 1
levels = {
    1: {'walls': [(0, -280), (0, 280), (-280, 0), (280, 0)], 'speed': 10},
    2: {'walls': [(0, -280), (0, 280), (-280, 0), (280, 0), (-200, -200), (200, -200), (-200, 200), (200, 200)], 'speed': 15},
    3: {'walls': [(0, -280), (0, 280), (-280, 0), (280, 0), (-200, -200), (200, -200), (-200, 200), (200, 200)],
        'speed': 20, 'food_color': 'yellow', 'wall_color': 'red'},
}
paused = False

# Functions
def save_score():
    global score
    c.execute("SELECT id FROM user WHERE username=?", (username,))
    user_id = c.fetchone()[0]
    c.execute("INSERT INTO user_score (user_id, level, score) VALUES (?, ?, ?)", (user_id, current_level, score))
    conn.commit()
    print("Score saved.")

def show_level():
    global current_level
    if current_level not in levels:
        print("Invalid level.")
        return
    print(f"Current level: {current_level}")
    print(f"Walls: {levels[current_level]['walls']}")
    print(f"Speed: {levels[current_level]['speed']}")
    if 'food_color' in levels[current_level]:
        print(f"Food color: {levels[current_level]['food_color']}")
    if 'wall_color' in levels[current_level]:
        print(f"Wall color: {levels[current_level]['wall_color']}")

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def toggle_pause():
    global paused
    if paused:
        print("Game resumed.")
        paused = False
    else:
        print("Game paused. Press 'p' to resume or 's' to save and quit.")
        paused = True

def move():
    if paused:
        return

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head