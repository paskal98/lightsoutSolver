import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer

from main.algorithmus.bfs import BreathFirstSearch
from main.algorithmus.dfs import DeepFirstSearch
from main.utils.toggle import LightToggler


class MainWindow(QMainWindow):
    def __init__(self, toggle_combination, size_row, size_column, initial_field):
        super().__init__()
        self.toggle_combination = toggle_combination
        self.size_row = size_row
        self.size_column = size_column
        self.initial_field = initial_field.copy()
        self.field = initial_field.copy()
        self.toggler = LightToggler(size_row, size_column)
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.gridLayout = QGridLayout(self.centralWidget)

        self.labels = []
        for i in range(self.size_row * self.size_column):
            label = QLabel(self.centralWidget)
            color = "yellow" if self.initial_field[i] == 1 else "black"
            label.setStyleSheet(f"background-color: {color}; border: 1px solid black;")
            self.gridLayout.addWidget(label, i // self.size_column, i % self.size_column)
            self.labels.append(label)

        self.startButton = QPushButton('Start Visualization', self.centralWidget)
        self.startButton.clicked.connect(self.startVisualization)
        self.gridLayout.addWidget(self.startButton, self.size_row, 0, 1, self.size_column)

        self.setWindowTitle('Light Toggle Visualization')
        self.show()

    def startVisualization(self):
        self.field = self.initial_field.copy()  # Reset to initial field
        self.updateLabels()  # Update labels to reflect the reset field
        self.animateToggles()  # Start the animation

    def updateLabels(self):
        for i, label in enumerate(self.labels):
            color = "yellow" if self.field[i] == 1 else "black"
            label.setStyleSheet(f"background-color: {color}; border: 1px solid black;")

    def animateToggles(self):
        delay = 0
        for combination in self.toggle_combination:
            for cell_index in range(len(combination)):
                if combination[cell_index] == 1:
                    QTimer.singleShot(delay, lambda cell_index=cell_index: self.applyToggle(cell_index))
                    delay += 500

    def applyToggle(self, cell_index):
        self.field = self.toggler.on_toggle(cell_index, self.field)
        for i in range(len(self.field)):
            color = "yellow" if self.field[i] == 1 else "black"
            self.labels[i].setStyleSheet(f"background-color: {color}; border: 1px solid black;")

def runBFS(size_row, size_column ,field):
    try:
        bfs = BreathFirstSearch(size_row, size_column, field)
        _, toggle_combination, queue_solution = bfs.solve()
        return toggle_combination, queue_solution
    except Exception as e:
        print(f"An error occurred while running BFS: {e}")
        return []

def runDFS(size_row, size_column ,field):
    try:
        dfs = DeepFirstSearch(size_row, size_column, field)
        _, toggle_combination, queue_solution = dfs.solve()
        return toggle_combination, queue_solution
    except Exception as e:
        print(f"An error occurred while running DFS: {e}")
        return []


def main():
    size_row = 5
    size_column = 5

    # 11 000 000 combination dfs
    # 7 000 000 combination bfs
    # field = [
    #     1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 0,
    #     1, 0, 1, 0, 0,
    #     0, 1, 1, 0, 1,
    #     0, 0, 0, 0, 1
    # ]

    field = [
        1, 1, 0, 1, 1,
        1, 0, 1, 0, 1,
        0, 1, 1, 1, 0,
        1, 0, 1, 0, 1,
        1, 1, 0, 1, 1
    ]



    # field = [
    #     0, 1, 1,
    #     1, 0, 1,
    #     1, 1, 0
    # ]

    # print("BFS")
    # toggle_combination, queue_solution = runBFS(size_row, size_column, field)
    # print(toggle_combination)
    # print("\n==============\n")

    print("DFS")
    toggle_combination2, queue_solution2 = runDFS(size_row, size_column, field)
    print(toggle_combination2)

    app = QApplication(sys.argv)
    mainWindow = MainWindow(toggle_combination2, size_row, size_column, field)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
