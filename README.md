# Tic-Tac-Toe Game (Connect 4)

This project implements a simple Tic-Tac-Toe game (Connect 4 variant) using Python. The game logic is encapsulated in the `connect4.py` script, which provides functions to create and manage the game board, verify moves, update the board state, and check for winning conditions.

## Features

- **Game Board Management**:
  - Initialize an empty game board with specified dimensions (rows and columns).
  - Print the current game board to the console with player tokens ('X' and 'O').

- **Move Validation**:
  - Verify the validity of a player's move based on the selected column.
  - Ensure that a move is within the bounds of the game board and that the selected column is not full.

- **Board Update**:
  - Update the game board with a player's move, placing their token ('X' or 'O') in the specified column.

- **Winning Condition**:
  - Check the game board to determine if a player has won the game by connecting four tokens either horizontally, vertically, or diagonally.

## Functions

### `make_empty_board(nrows, ncols)`

Creates and returns an empty game board represented as a list of strings.

### `print_board(l)`

Prints the current game board to the console.

### `verify_board(l)`

Verifies the validity and integrity of the game board state.

### `verify_move(l, id)`

Verifies if a move (placement in a specific column) is valid and allowed.

### `update_board(l, id, d)`

Updates the game board with a player's move (token placement) in the specified column.

### `has_won(l, id)`

Checks if a player has won the game by connecting four tokens in a row (horizontally, vertically, or diagonally).

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/namdavid2904/Tic-Tac-Toe.git
   ```

2. **Navigate to Project Directory**:
   ```bash
   cd Tic-Tac-Toe
   ```

3. **Run the Game**:
   ```bash
   python connect4.py
   ```

4. **Follow the Game Instructions**:
   - The game will prompt players to make moves by entering column numbers (0-indexed).
   - The game board will be updated after each valid move, and winning conditions will be checked.

## Example

```python
# Initialize a 6x7 game board
board = make_empty_board(6, 7)

# Display the empty board
print_board(board)

# Example game loop (pseudo-code)
current_player = 'X'
while True:
    column = int(input(f"Player {current_player}, enter column (0-6): "))
    if verify_move(board, column):
        update_board(board, column, current_player)
        print_board(board)
        if has_won(board, column):
            print(f"Player {current_player} wins!")
            break
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Invalid move. Please try again.")

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
