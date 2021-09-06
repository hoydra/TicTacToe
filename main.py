import random


class TicTacToe:

    def __init__(self):




        self.board = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
                      ]

        self.position = {
            "A":{1:self.board[0][0], 2:self.board[0][1], 3:self.board[0][2]},
            "B":{1:self.board[1][0], 2:self.board[1][1], 3:self.board[1][2]},
            "C":{1:self.board[2][0], 2:self.board[2][1], 3:self.board[2][2]}
            }
        # maybe change these to class variables

    def player(self):

        try:

            place = input("Where: ").upper()
            place = list(place)
            row = place[0]
            column = int(place[1])

            if self.position[row][column] == "-":
                self.position[row][column] = "X"
            else:
                raise Exception

        except Exception:

            print("Your turn was not registered")

    def board_ui(self):
        letters = list(self.position.keys())
        for num,i in enumerate(self.position.values(), start=0):
            print(letters[num], list(i.values()))

        print("   " + "1" + "    " + "2" + "     " + "3")

    def tie(self):
        self.test = []
        for i in self.position.values():

            self.test.append(list(i.values()).count("-"))
            if self.test.count(0) == 3:
                return True


    def patterns(self):



        for i in list(self.position.values()):  # Horizontal X
            if list(i.values()).count("X") == 3:
                return True
                                                # Horizontal 0
            if list(i.values()).count("0") == 3:
                return False

                                                                                                             #  Vertical X
        if self.position["A"][1] == "X" and self.position["B"][1] == "X" and self.position["C"][1] == "X":
            return True

        if self.position["A"][2] == "X" and self.position["B"][2] == "X" and self.position["C"][2] == "X":
            return True

        if self.position["A"][3] == "X" and self.position["B"][3] == "X" and self.position["C"][3] == "X":
            return True

                                                                                                            # Diagonal X
        if self.position["A"][1] == "X" and self.position["B"][2] == "X" and self.position["C"][3] == "X":
            return True

        if self.position["A"][3] == "X" and self.position["B"][2] == "X" and self.position["C"][1] == "X":
            return True



                                                                                                            #Vertical 0
        if self.position["A"][1] == "0" and self.position["B"][1] == "0" and self.position["C"][1] == "0":
            return False

        if self.position["A"][2] == "0" and self.position["B"][2] == "0" and self.position["C"][2] == "0":
            return False

        if self.position["A"][3] == "0" and self.position["B"][3] == "0" and self.position["C"][3] == "0":
            return False

                                                                                                            # Diagonal 0
        if self.position["A"][1] == "0" and self.position["B"][2] == "0" and self.position["C"][3] == "0":
            return False
        if self.position["A"][3] == "0" and self.position["B"][2] == "0" and self.position["C"][1] == "0":
            return False

       # the patterns method needs some cleaning up with for loops
    def bot(self):

        rand_num = random.randint(1,3)

        for letter in self.position.keys():
            if self.position[letter][rand_num] == "-":
                self.position[letter][rand_num] = "0"
                break

    def game(self):  # Main function where all functions run
        won = False

        while won == False:

            self.board_ui()

            self.player()

            self.bot()

            if self.tie():
                self.board_ui()
                print("The game is a tie")
                won = True

            if self.patterns() == False:
                self.board_ui()
                print("You lost!")
                won = True

            if self.patterns():
                self.board_ui()
                print("You won!")
                won = True







if __name__ == '__main__':

    game = TicTacToe()
    game.game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
