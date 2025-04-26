# AI Project 0

## 📁 src 0

## 📚 Course
- [YouTube Course](https://www.youtube.com/watch?v=WbzNRTTrX0g&t=2549s)

## 📄 Documentation
- [Project Description](https://cs50.harvard.edu/ai/2024/projects/0/)
- [Quiz](https://cs50.harvard.edu/ai/2024/quizzes/0/)
- [Lecture Notes](https://cs50.harvard.edu/ai/2024/notes/0/)

## 📝 My Notes

### Search Algorithms

- **Stack**: LIFO structure.
- **Queue**: FIFO structure.

#### Uninformed Search vs Informed Search
- **Uninformed Search**: No additional information about states beyond that provided in the problem definition.
- **Informed Search**: Uses problem-specific knowledge.

#### Greedy Best-First Search
- Uses a **heuristic** to estimate how close we are to the goal.
- **Heuristic function h(n)**:
  - Returns estimated cost from node `n` to goal.
  - Example: **Manhattan Distance** — the sum of the absolute differences in the horizontal and vertical coordinates (ignores walls).

#### A* Search
- Expands the node with the lowest value of `g(n) + h(n)`.
  - `g(n)`: Cost to reach node `n`.
  - `h(n)`: Estimated cost to reach the goal.
- **Optimality conditions**:
  - `h(n)` must be **admissible**: Never overestimates the true cost.
  - `h(n)` must be **consistent**: For every node `n` and successor `n'` with step cost `c`,  
    `h(n) ≤ h(n') + c`.

---

### Adversarial Search

- **Adversarial search problem**: One agent tries to succeed while another tries to prevent it.

#### Minimax Algorithm
- **Max** player aims to maximize score.
- **Min** player aims to minimize score.
- Builds a **logic tree** alternating between Max and Min nodes.

##### Functions:
- `max-value(state)`
- `min-value(state)`

#### Optimizations
- **Alpha-Beta Pruning**:
  - Prune branches that won't affect the final decision, reducing time and space complexity.
  
- **Depth-Limited Minimax**:
  - Limit the depth of the search tree to save resources.

#### Evaluation Function
- Estimates the expected utility of the game from a given state.
- Answers: *How good is the current game state?*

---

## ⏭️ Next Topic
- Knowledge representation: How AI knows, reasons, and draws conclusions.
