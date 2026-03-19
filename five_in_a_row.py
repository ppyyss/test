def print_board(board):
    for row in board:
        print(' '.join(row))

def check_win(board, row, col, player):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        # 正方向
        for i in range(1, 5):
            r, c = row + i * dr, col + i * dc
            if 0 <= r < 15 and 0 <= c < 15 and board[r][c] == player:
                count += 1
            else:
                break
        # 反方向
        for i in range(1, 5):
            r, c = row - i * dr, col - i * dc
            if 0 <= r < 15 and 0 <= c < 15 and board[r][c] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

def main():
    while True:
        board = [['.' for _ in range(15)] for _ in range(15)]
        current_player = 'X'

        while True:
            print_board(board)
            print(f"Player {current_player}'s turn. Enter row and column (1-15, e.g., '8 8'): ", end='')
            move = input().split()
            if len(move) != 2:
                print("Invalid input. Please enter two numbers.")
                continue
            try:
                row = int(move[0]) - 1
                col = int(move[1]) - 1
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue
            if row < 0 or row >= 15 or col < 0 or col >= 15:
                print("Coordinates out of bounds.")
                continue
            if board[row][col] != '.':
                print("That position is already occupied.")
                continue

            board[row][col] = current_player
            if check_win(board, row, col, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                while True:
                    choice = input("继续游戏？(y/n/u) - y 重新开始/u 选择先手/n 退出：").strip().lower()
                    if choice == 'y':
                        board = [['.' for _ in range(15)] for _ in range(15)]
                        current_player = 'X'
                        break
                    elif choice == 'n':
                        exit()
                    elif choice == 'u':
                        print("选择谁先手？(x/o)")
                        start_choice = input().strip().lower()
                        if start_choice == 'x':
                            current_player = 'X'
                        elif start_choice == 'o':
                            current_player = 'O'
                        else:
                            print("无效输入，默认 X 先手")
                            current_player = 'X'
                        board = [['.' for _ in range(15)] for _ in range(15)]
                        break
                    else:
                        print("无效输入，请输入 y、u 或 n。")
            else:
                current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()