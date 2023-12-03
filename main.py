import sys

import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer

from main.algorithmus.A_start.a_star import AStar
from main.algorithmus.bfs.bfs import BreathFirstSearch
from main.algorithmus.dfs.dfs import DeepFirstSearch
from main.algorithmus.greedy.greedy import GreedySearch
from main.algorithmus.heuristic.gaus import get_heuristic_solution
from main.utils.toggle.toggle import LightToggler


class MainWindow(QMainWindow):
    def __init__(self, toggle_combination, size_row, size_column, initial_field, name="Light Toggle Visualization"):
        super().__init__()
        self.toggle_combination = toggle_combination
        self.size_row = size_row
        self.size_column = size_column
        self.initial_field = initial_field.copy()
        self.field = initial_field.copy()
        self.toggler = LightToggler(size_row, size_column)
        self.name=name
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

        self.setWindowTitle(self.name)
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
                    delay += 300

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

def runAStart(size_row, size_column, field):
    try:
        astar_search = AStar(size_row, size_column, field)
        execution_time, toggle_combination, _ = astar_search.solve()
        return toggle_combination, execution_time
    except Exception as e:
        print(f"An error occurred while running Greedy Search: {e}")
        return [], 0

def runGreedy(size_row, size_column, field):
    try:
        greedy_search = GreedySearch(size_row, size_column, field)
        execution_time, toggle_combination, _ = greedy_search.solve()
        return toggle_combination, execution_time
    except Exception as e:
        print(f"An error occurred while running Greedy Search: {e}")
        return [], 0


def main():
    size_row = 5
    size_column = 5

    # 11 000 000 combination dfs
    # 7 000 000 combination bfs
    # init_field = [
    #     1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 0,
    #     1, 0, 1, 0, 0,
    #     0, 1, 1, 0, 1,
    #     0, 0, 0, 0, 1
    # ]
    # size_row = 5
    # size_column = 5


    # init_field= [
    #     1, 1, 0, 1, 1,
    #     1, 0, 1, 0, 1,
    #     0, 1, 1, 1, 0,
    #     1, 0, 1, 0, 1,
    #     1, 1, 0, 1, 1
    # ]
    # size_row = 5
    # size_column = 5

    init_field = [
        0, 1, 0,
        1, 1, 0,
        1, 0, 0
    ]
    size_row = 3
    size_column = 3

    # init_field= [
    #     1, 1, 0, 1, 1, 0, 0,
    #     1, 0, 1, 0, 1, 0, 0,
    #     0, 1, 1, 1, 0, 0, 0,
    #     1, 0, 1, 0, 1, 0, 0,
    #     1, 1, 0, 1, 1, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0
    # ]
    # size_row = 7
    # size_column = 7

    # init_field = [
    #     1, 1, 0, 1, 1, 0, 0, 0,
    #     1, 0, 1, 0, 1, 0, 0, 0,
    #     0, 1, 1, 1, 0, 0, 0, 0,
    #     1, 0, 1, 0, 1, 0, 0, 0,
    #     1, 1, 0, 1, 1, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0
    #
    # ]
    # size_row = 8
    # size_column = 8

    # init_field = [
    #     1, 0, 1,
    #     1, 0, 1
    # ]
    # size_row = 2
    # size_column = 3

    # init_field = [
    #     0, 0, 0,
    #     0, 1, 0,
    #     0, 0, 0
    # ]
    # size_row = 3
    # size_column = 3

    # init_field = [
    #     0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0,
    #     0, 0, 1, 0, 0,
    #     0, 0, 0, 1, 1,
    #     0, 0, 0, 1, 1
    # ]
    # size_row = 5
    # size_column = 5

    init_field = [
        1, 0, 1, 0, 1,
        0, 1, 0, 0, 0,
        0, 1, 1, 0, 1,
        0, 1, 1, 0, 1,
        0, 0, 0, 1, 1
    ]
    size_row = 5
    size_column = 5

    # init_field = [
    #     1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    #     1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    #
    # ]
    # size_row = 10
    # size_column = 10



    # print("BFS")
    # toggle_combination, queue_solution = runBFS(size_row, size_column, init_field)
    # print(toggle_combination)
    # print("---------------------------------------------------------------\n")
    #
    # print("DFS")
    # toggle_combination2, queue_solution2 = runDFS(size_row, size_column, init_field)
    # print(toggle_combination2)
    # print("---------------------------------------------------------------\n")

    print("Greedy")
    toggle_combination4, queue_solution4 = runGreedy(size_row, size_column, init_field)
    print(toggle_combination4)
    print("---------------------------------------------------------------\n")

    print("A*")
    toggle_combination3, queue_solution3 = runAStart(size_row, size_column, init_field)
    print(toggle_combination3)
    print("---------------------------------------------------------------\n")


    solution_combination = get_heuristic_solution(init_field, size_row, size_column)
    print(solution_combination)

    are_same_1_2 = np.array_equal(np.array(toggle_combination4), solution_combination)
    print(f"Array1 is the same as Array2: {are_same_1_2} ")







    # toggler = LightToggler(size_row, size_column)
    #
    # field = init_field.copy()
    #
    # toggle_combination3 = []
    # for i in range(len(solution_combination)):
    #     if solution_combination[i] == 1:
    #         field = toggler.on_toggle(i, field.copy())
    #         toggle_combination3.append(field.copy())
    #
    # print(toggle_combination3)


    # app = QApplication(sys.argv)
    # mainWindow = MainWindow([solution_combination], size_row, size_column, init_field,"GAUSS")
    #
    #
    # app2 = QApplication(sys.argv)
    # mainWindow2 = MainWindow(np.array(toggle_combination), size_row, size_column, init_field,"BFS")
    #
    #
    # app3 = QApplication(sys.argv)
    # mainWindow3 = MainWindow(np.array(toggle_combination2), size_row, size_column, init_field,"DFS")
    #
    #
    # app4 = QApplication(sys.argv)
    # mainWindow4 = MainWindow([np.array(toggle_combination3)], size_row, size_column, init_field,"A*")


    app5 = QApplication(sys.argv)
    mainWindow5 = MainWindow([np.array(toggle_combination4)], size_row, size_column, init_field, "Greedy")

    sys.exit(app5.exec_())


if __name__ == '__main__':
    main()


