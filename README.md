# **Pong Game: Messi or Ronaldo Edition**

## **Description**
This is a Python-based Pong-style game built using the **Turtle Graphics Library**. It features enhanced gameplay mechanics with special cones, real-time scoring, and dynamic animations. Players compete to score the highest points before the timer runs out.

## **Features**
- **Classic Pong Gameplay**: Two-player paddle game with smooth and responsive controls.
- **Cone Challenge**: Randomly spawning cones add an exciting scoring opportunity for bonus points.
- **Dynamic Scoring System**: Real-time score updates displayed on the screen.
- **Interactive Timer**: Countdown timer challenges players to maximize their score within a limited time.
- **Graphical Enhancements**: Animated paddles, boundary effects, and engaging visual elements.
- **Victory Announcement**: The winner is displayed with a celebratory message at the end of the game.

## **Technologies Used**
- **Python**: Core logic and game mechanics.
- **Turtle Graphics**: Rendering of visual elements.
- **Random Module**: Randomized velocities and cone spawning.
- **Time Module**: Game timing and animations.

## **How to Install**
1. Ensure you have Python installed with the `turtle` module.
2. Clone or download the repository.
   ```bash
   https://github.com/kawin5431/Final_project_Messi-or-Ronaldo--game-.git
   ```
3. Set environment:
   
      Set Interpreter and environment before run file.    
   
3. Run the game:

      Run file game.py

## Usage

### Objective of the Game
Players control paddles to hit and interact with the ball, aiming to score points by hitting targets (Cones) and obstacles. The goal is to achieve the highest score before time runs out or complete all the levels.

## 🎯 Objective
- Players must use their paddles to hit the main ball and collect yellow balls to score points.
- The score is tracked for both the left player (Player 1) and the right player (Player 2).
- The game ends after 63 seconds.

---

## 🕹️ Controls
1. **Move Paddles:**
   - **Player 1 (Left):**
     - Press **W** to move the paddle up.
     - Press **S** to move the paddle down.
   - **Player 2 (Right):**
     - Press **Up Arrow (↑)** to move the paddle up.
     - Press **Down Arrow (↓)** to move the paddle down.

2. **Scoring:**
   - Yellow balls spawn randomly on the field.
   - Players must hit the main ball to make it collide with a yellow ball to score.
   - Points are awarded to the last player to hit the main ball before it collides with the yellow ball.

3. **Ball Speed:**
   - Ball speed increases temporarily after collecting a yellow ball.

4. **Game Timer:**
   - The game runs for **63 seconds**.
   - When the timer ends, the game concludes, and the winner is announced.

---

## 🏆 Winning
- The player with the higher score at the end of the game wins:
  - **"Crying Penaldo!"** if Player 1 wins.
  - **"Messi Robber Ronaldo Better!"** if Player 2 wins.
  - **"Two Goat!"** if it’s a tie.

---

## ⚙️ Game Field and Mechanics
- The field size is **800x600 pixels**.
- Paddles can only move vertically within bounds to hit the ball.
- The main ball bounces off the edges and paddles, changing direction dynamically.

---

# Class Descriptions for "Messi or Ronaldo?" Game

This document describes the classes used in the **"Messi or Ronaldo?"** game and their roles within the system.

---

## 📚 Classes Overview

### `Game`
- **Purpose:** Main class responsible for running the game and coordinating all other components.
- **Attributes:**
  - `screen`: Turtle screen for rendering the game.
  - `boundary_width` and `boundary_height`: Dimensions of the game field.
  - `timer`: Instance of `Timer` for tracking game duration.
  - `score_left` and `score_right`: Instances of `Score` to manage player scores.
  - `bat_left` and `bat_right`: Instances of `Bat` for the player paddles.
  - `ball`: Instance of `Ball` representing the main ball.
  - `yellow_balls`: List of `YellowBall` instances for bonus points.
- **Methods:**
  - `play()`: Starts the game loop.
  - `spawn_yellow_ball()`: Spawns a yellow ball at a random position.
  - `check_yellow_ball_collision(yellow_ball)`: Checks if the main ball collides with a yellow ball.
  - `increase_ball_speed()`: Temporarily increases the ball's speed.
  - `show_winner()`: Displays the winning message at the end of the game.

---

### `Ball`
- **Purpose:** Represents the main ball in the game.
- **Attributes:**
  - `radius`, `color`: Visual properties of the ball.
  - `x`, `y`, `vx`, `vy`: Position and velocity attributes.
  - `boundary_width`, `boundary_height`: Boundaries of the game field.
- **Methods:**
  - `move()`: Updates the ball's position based on its velocity.
  - `bounce_vertical()` and `bounce_horizontal()`: Reverses velocity on collision with paddles or walls.
  - `curve(direction)`: Adjusts velocity for curving the ball's trajectory.

---

### `YellowBall`
- **Purpose:** A special ball that provides bonus points when collected.
- **Inheritance:** Inherits from `Ball`.
- **Attributes:**
  - `spawn_area`: Tuple defining the area where the ball can spawn.
- **Methods:**
  - `spawn()`: Spawns the ball at a random position within the spawn area.
  - `hide()`: Hides the ball when collected.

---

### `Bat`
- **Purpose:** Represents a player's paddle for hitting the ball.
- **Attributes:**
  - `width`, `height`: Dimensions of the paddle.
  - `position`: Current position of the paddle.
  - `boundary_width`, `boundary_height`: Boundaries within which the paddle can move.
- **Methods:**
  - `move(x, y)`: Moves the paddle up or down.
  - `check_collision(ball)`: Checks if the paddle collides with the ball and adjusts the ball's velocity.
  - `tilt(direction)`: Changes the paddle's angle for visual effect.

---

### `Timer`
- **Purpose:** Tracks and displays the remaining game time.
- **Attributes:**
  - `duration`: Total game duration in seconds.
  - `time_left`: Remaining time in seconds.
- **Methods:**
  - `update()`: Updates the timer display and decreases time left.

---

### `Score`
- **Purpose:** Tracks and displays the player's score.
- **Attributes:**
  - `score`: Current score of the player.
  - `position`: Screen position for displaying the score.
- **Methods:**
  - `update(score)`: Updates the score and refreshes the display.

---

### `Outter`
- **Purpose:** Draws the boundary of the game field.
- **Attributes:**
  - `width`, `height`: Dimensions of the game boundary.
- **Methods:**
  - *(None specific, boundary is visual only.)*

---

## 🛠️ Class Diagram

Refer to the UML class diagram for a visual representation of the classes and their relationships.

![UML_Class_Diagram_Complete](https://github.com/user-attachments/assets/98ce8993-7646-4042-87be-e539d54467bd)

---

This structure allows easy maintenance, scalability, and understanding of the game's core logic.

### Present Video
Provide a link to a present video of the project: [[Present Video](https://youtu.be/6tJNVEoawHY?si=OIT6cV9dm0BFIZei)](#)








