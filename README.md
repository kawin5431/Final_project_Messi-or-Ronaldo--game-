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

### UML Class Diagram
![UML Class Diagram](./UML_Class_Diagram_Rectangles.png)




