<h1>Snake Game</h1>

  <p>This is a classic Snake Game implemented in Python using the Pygame library. The objective of the game is to control
    the snake, guiding it to eat food and grow longer without hitting the walls or colliding with itself.</p>

  <h2>Files Overview</h2>

  <ul>
    <li><code>main.py</code>: This file contains the main game logic, including initializing the game, handling user
      input, updating the game state, and rendering the game on the screen.</li>
    <li><code>snake.py</code>: The <code>snake.py</code> file defines the Snake class, which represents the snake object
      in the game. It includes methods for moving the snake, growing its length, checking collisions, and updating its
      position.</li>
    <li><code>food.py</code>: In the <code>food.py</code> file, you'll find the Food class responsible for generating
      food items (represented as green squares) for the snake to eat. It handles the random spawning of food on the game
      screen.</li>
    <li><code>scoreboard.py</code>: The <code>scoreboard.py</code> file contains the Scoreboard class, which manages the
      player's score and displays it on the screen during gameplay. It tracks the score based on the number of food items
      eaten by the snake.</li>
    <li><code>speed.py</code>: This file defines constants or variables related to the game's speed or framerate. It may
      include settings for the snake's movement speed or the game's refresh rate.</li>
  </ul>

  <h2>Installation</h2>

  <ol>
    <li>Ensure you have Python installed on your system. You can download Python from the official website: <a
        href="https://www.python.org/downloads/">python.org</a>.</li>
    <li>Install the Pygame library using pip:
      <pre><code>pip install pygame</code></pre>
    </li>
  </ol>

  <h2>How to Play</h2>

  <ol>
    <li>Run the game by executing the <code>main.py</code> file.</li>
    <li>Use the arrow keys (Up, Down, Left, Right) to control the movement of the snake.</li>
    <li>Guide the snake to eat the food (displayed as green squares) to grow longer.</li>
    <li>Avoid hitting the walls or colliding with the snake's own body.</li>
    <li>The game ends if the snake collides with a wall or itself.</li>
    <li>Try to achieve the highest score by eating as much food as possible without crashing.</li>
  </ol>

  <h2>Controls</h2>

  <ul>
    <li><strong>Up Arrow:</strong> Move the snake upwards.</li>
    <li><strong>Down Arrow:</strong> Move the snake downwards.</li>
    <li><strong>Left Arrow:</strong> Move the snake to the left.</li>
    <li><strong>Right Arrow:</strong> Move the snake to the right.</li>
  </ul>

  <h2>Features</h2>

  <ul>
    <li>Responsive snake movement controlled by arrow keys.</li>
    <li>Random spawning of food for the snake to eat.</li>
    <li>Score tracking to monitor player progress.</li>
    <li>Game over screen displaying the final score.</li>
  </ul>

  <h2>Dependencies</h2>

  <ul>
    <li>Python 3.x</li>
    <li>Pygame</li>
  </ul>

  <h2>Contributing</h2>

  <p>Contributions are welcome! If you have any suggestions, bug fixes, or improvements for the game, feel free to submit
    a pull request or open an issue on GitHub.</p>

  <h2>License</h2>

  <p>This Snake Game is released under the <a href="LICENSE">MIT License</a>.</p>
