from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QWidget, QPushButton, QLabel, QMessageBox, QSpinBox, QHBoxLayout
from PySide2.QtCore import QSize
import sys
import doctest

class TicTacToe(QWidget):
    def __init__(self, num_cols, num_rows):
        """Initializes Game Window
        >>> obj = TicTacToe(3, 3)
        >>> obj = TicTacToe(9, 9)
        >>> obj = TicTacToe(4, 4)
        >>> obj.display_scores()
        >>> obj.game_won()
        False
        >>> obj.win_by_row(2)
        False
        >>> obj.win_by_col(2)
        False
        >>> obj.win_by_diag_right()
        False
        >>> obj.win_by_diag_left()
        False
        >>> obj.no_more_slots()
        False
        """
        super().__init__()
        
        self.setWindowTitle("Tic-Tac-Toe Game")

        self.curr_player = 'x'
        self.curr_player_label = QLabel(f'Current Player\'s Turn: x')
        self.button_list = []
        self.winner = ''
        self.winner_buttons = []
        self.NUM_ROWS = int(num_rows)
        self.NUM_COLS = int(num_cols)
        self.player_scores = [0, 0, 0]
        self.game_over = False

        start_game_label = QLabel("Welcome to Tic-Tac-Toe!!\nInstructions: Press any button with a \'-\' symbol to claim space.")

        retry_button = QPushButton("New Game")
        retry_button.clicked.connect(self.new_game_button_clicked)

        player_scores_button = QPushButton("Player Scores")
        player_scores_button.clicked.connect(self.display_scores)
        
        general_layout = QGridLayout()

        game_subheading_layout = QVBoxLayout()
        self.render_subtitles(game_subheading_layout, start_game_label, self.curr_player_label)

        game_board_layout = QGridLayout()
        self.render_game_board(game_board_layout)
        game_board_layout.setHorizontalSpacing(0)

        bottom_button_layout = QHBoxLayout()
        self.render_bottom_buttons(bottom_button_layout, retry_button, player_scores_button)
        
        general_layout.addLayout(game_subheading_layout, 0, 0, 1, self.NUM_COLS)
        middle = self.NUM_COLS // 2 if self.NUM_COLS % 2 != 0 else (self.NUM_COLS // 2) - 1
        general_layout.addLayout(game_board_layout, 1, middle)
        general_layout.addLayout(bottom_button_layout, 2, 0, 1, self.NUM_COLS)

        self.setLayout(general_layout)
    
    def render_subtitles(self, layout, instructions_label, player_label):
        """Creates subheading layout.
        """
        layout.addWidget(instructions_label)
        layout.addWidget(player_label)

    def render_game_board(self, layout):
        """Creates game board layout.
        >>> obj = TicTacToe(3, 3)
        >>> len(obj.button_list) == 3
        True
        >>> obj = TicTacToe(5, 5)
        >>> len(obj.button_list) == 5
        True
        >>> list = obj.button_list
        >>> list[0][0].text() == '-'
        True
        """
        for row in range(self.NUM_ROWS):
            buttons_in_row = []
            for col in range(self.NUM_COLS):
                button = QPushButton('-')
                button.setFixedSize(QSize(40, 40))
                button.clicked.connect(self.game_board_button_clicked)
                layout.addWidget(button, row, col)
                buttons_in_row.append(button)
            self.button_list.append(buttons_in_row)
    
    def render_bottom_buttons(self, layout, retry_button, score_button):
        """Creates layout for new game button and player score button.
        """
        layout.addWidget(retry_button)
        layout.addWidget(score_button)
    
    def game_board_button_clicked(self):
        """Checks whether the game is not over, if it is, it does not respond to the click of a board button after the player has won.
        This method also highlights the winning buttons.
        If the game is not over, it will change the symbol of the button according to the current player\'s turn.
        """
        if self.game_over == False:
            if self.sender().text() == '-':
                self.sender().setText(self.curr_player)
                self.curr_player = 'o' if self.curr_player == 'x' else 'x'
                self.curr_player_label.setText(f'Current Player\'s Turn: {self.curr_player}')
            else:
                warning_message = QMessageBox()
                warning_message.setIcon(QMessageBox.Warning)
                warning_message.setWindowTitle("Slot Already Taken!")
                warning_message.setText(f"This slot has already being selected by player \'{self.sender().text()}\'.\nPlease select another slot.")
                warning_message.exec_()
            
            if self.game_won():
                for button in self.winner_buttons:
                    button.setStyleSheet("background-color : yellow")
                win_message = QMessageBox()
                win_message.setWindowTitle("Game Ended")
                win_message.setIcon(QMessageBox.Information)
                win_message.setStandardButtons(QMessageBox.Ok)
                win_message.setText("Game completed, winner is " + self.winner)
                win_message.exec_()
                if self.winner == 'x':
                    self.player_scores[0] += 1
                else:
                    self.player_scores[1] += 1
                self.game_over = True
            elif self.no_more_slots():
                win_message = QMessageBox()
                win_message.setWindowTitle("Game Ended")
                win_message.setIcon(QMessageBox.Information)
                win_message.setStandardButtons(QMessageBox.Ok)
                win_message.setText("Game completed, no winners")
                win_message.exec_()
                self.game_over = True
                self.player_scores[2] += 1
    
    def new_game_button_clicked(self):
        """Pops up a confirmation dialog to check if the players want to play again.
        If they confirm, the symbols and color of the buttons will reset and a new game will start.
        This method does not erase players\' scores.
        """
        confirm_window = QMessageBox()
        confirm_window.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        confirm_window.setIcon(QMessageBox.Warning)
        confirm_window.setWindowTitle("Warning")
        confirm_window.setText("Do you want to start a new game?")
        button = confirm_window.exec_()
        if button == QMessageBox.Ok:
            self.curr_player = 'x'
            self.curr_player_label.setText(f"Current Player\'s Turn: {self.curr_player}")
            for row_buttons in self.button_list:
                for button in row_buttons:
                    button.setStyleSheet("background-color : ")
                    button.setText('-')
            self.game_over = False
            self.winner = ''
    
    def display_scores(self):
        """Displays a dialog of the score of each player.
        """
        player_score_window = QMessageBox()
        player_score_window.setWindowTitle("Current Scores")
        player_score_window.setText("Player x Score: " + str(self.player_scores[0]) + "\nPlayer o Score: " + str(self.player_scores[1]) + "\nNumber of Draws: " + str(self.player_scores[2]))
        player_score_window.setStandardButtons(player_score_window.Ok)
        player_score_window.setIcon(player_score_window.Information)
        player_score_window.exec_()

    def game_won(self):
        """Checks if a player has won.
        >>> obj = TicTacToe(3, 3)
        >>> obj.game_won()
        False
        >>> obj.button_list = [[QPushButton('x'), QPushButton('x')], [QPushButton('o'), QPushButton('-')]]
        >>> obj.game_won()
        True
        """
        for num in range(len(self.button_list)):
            if self.win_by_row(num):
                return True
            elif self.win_by_col(num):
                return True
        else:
            if self.win_by_diag_right() or self.win_by_diag_left():
                return True
            else:
                return False
    
    def win_by_row(self, curr_row):
        """Checks each column of a row to see if a player won.
        >>> obj = TicTacToe(3, 3)
        >>> obj.button_list = [[QPushButton('x'), QPushButton('x')], [QPushButton('o'), QPushButton('-')]]
        >>> obj.win_by_row(0)
        True
        >>> obj.win_by_row(1)
        False
        """
        first_mark = self.button_list[curr_row][0].text()
        if first_mark == '-':
            return False
        for col in range(len(self.button_list)):
            self.winner_buttons.append(self.button_list[curr_row][col])
            if self.button_list[curr_row][col].text() != first_mark:
                self.winner_buttons = []
                return False
        self.winner = first_mark
        return True

    def win_by_col(self, curr_col):
        """Checks each row of a column to see if a player won.
        >>> obj = TicTacToe(3, 3)
        >>> obj.button_list = [[QPushButton('x'), QPushButton('-')], [QPushButton('x'), QPushButton('-')]]
        >>> obj.win_by_col(0)
        True
        >>> obj.win_by_col(1)
        False
        """
        first_mark = self.button_list[0][curr_col].text()
        if first_mark == '-':
            return False
        for row in range(len(self.button_list)):
            self.winner_buttons.append(self.button_list[row][curr_col])
            if self.button_list[row][curr_col].text() != first_mark:
                self.winner_buttons = []
                return False
        self.winner = first_mark
        return True

    def win_by_diag_right(self):
        """Checks the right diagonal of the game board to see if a player won.
        >>> obj = TicTacToe(3, 3)
        >>> obj.button_list = [[QPushButton('x'), QPushButton('-')], [QPushButton('-'), QPushButton('x')]]
        >>> obj.win_by_diag_right()
        True
        >>> obj.button_list = [[QPushButton('-'), QPushButton('-')], [QPushButton('-'), QPushButton('-')]]
        >>> obj.win_by_diag_right()
        False
        """
        first_mark = self.button_list[0][0].text()
        if first_mark != '-':
            for num in range(len(self.button_list)):
                self.winner_buttons.append(self.button_list[num][num])
                if self.button_list[num][num].text() != first_mark:
                    self.winner_buttons = []
                    return False
            else:
                self.winner = first_mark
                return True
        else:
            return False
    
    def win_by_diag_left(self):
        """Checks if the left diagonal of the game board to see if a player won.
        >>> obj = TicTacToe(3, 3)
        >>> obj.button_list = [[QPushButton('-'), QPushButton('x')], [QPushButton('x'), QPushButton('-')]]
        >>> obj.win_by_diag_left()
        True
        >>> obj.button_list = [[QPushButton('-'), QPushButton('-')], [QPushButton('-'), QPushButton('-')]]
        >>> obj.win_by_diag_left()
        False
        """
        first_mark = self.button_list[0][len(self.button_list) - 1].text()
        if first_mark != '-':
            col = len(self.button_list) - 1
            for row in range(len(self.button_list)):
                self.winner_buttons.append(self.button_list[row][col])
                if self.button_list[row][col].text() != first_mark:
                    self.winner_buttons = []
                    return False
                col -= 1
            else:
                self.winner = first_mark
                return True
        else:
            return False
    
    def no_more_slots(self):
        """Checks if there are any spaces available.
        >>> obj = TicTacToe(3, 3)
        >>> obj.button_list = [[QPushButton('-'), QPushButton('-')], [QPushButton('-'), QPushButton('-')]]
        >>> obj.no_more_slots()
        False
        >>> obj.button_list = [[QPushButton('x'), QPushButton('x')], [QPushButton('x'), QPushButton('x')]]
        >>> obj.no_more_slots()
        True
        """
        for row in range(len(self.button_list)):
            for col in range(len(self.button_list)):
                if self.button_list[row][col].text() == '-':
                    return False
        return True

class MenuWindow(QMainWindow):
    def __init__(self):
        """Initializes the launcher for the tic-tac-toe game.
        >>> obj = MenuWindow()
        >>> obj.render_game()
        >>> spinbox = obj.row_col_spin
        """
        super().__init__()
        self.setFixedSize(275, 150)
        self.setWindowTitle("Launcher")

        welcome_label = QLabel('Welcome to Tic-Tac-Toe\nSelect Number of Rows and Columns')

        start_game_button = QPushButton('Start Game!!')
        start_game_button.clicked.connect(self.render_game)

        self.row_col_spin = QSpinBox()
        self.row_col_spin.setMinimum(3)
        self.row_col_spin.setMaximum(10)
        
        layout = QVBoxLayout()

        layout.addWidget(welcome_label)
        layout.addWidget(self.row_col_spin)
        layout.addWidget(start_game_button)

        container = QWidget()

        container.setLayout(layout)

        self.setCentralWidget(container)
    
    def render_game(self):
        """Pops up a new window for a new tic-tac-toe game.
        """
        self.game_window = TicTacToe(self.row_col_spin.text(), self.row_col_spin.text())
        self.game_window.show()

app = QApplication(sys.argv)
menu_window = MenuWindow()

menu_window.show()
app.exec_()
"""
if __name__ == '__main__':
    doctest.testmod()
"""
