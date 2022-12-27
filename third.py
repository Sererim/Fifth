# tic tac toe 
# made in console

from utils import Utils


class Game():
    
    _all_possible_winning_possitions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    def __init__(self) -> None:
        
        grid: list[str] = [' ' for x in range(9)]
        players:dict = {'X': [], 'O':[]}
        who_is: int = 0
        sign: list[str] = ['X', 'O']
        p_sign: str = " "
        b_sign: str = " "
        now: str = " "
        
        self.now = now
        self.b_sign = b_sign
        self.p_sing  = p_sign
        self.sign = sign
        self.grid = grid
        self.players = players
        self.who_is = who_is
        
    def draw(self) -> None:
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.grid[0], self.grid[1], self.grid[2]))
        print('\t_____|_____|_____')
 
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.grid[3], self.grid[4], self.grid[5]))
        print('\t_____|_____|_____')
 
        print("\t     |     |")
 
        print("\t  {}  |  {}  |  {}".format(self.grid[6], self.grid[7], self.grid[8]))
        print("\t     |     |")
        print("\n")

    def mainloop(self, ai: int = 0) -> None:
        self.who_is = Utils.random_choice(0, 1) # 0 human player, 1 - bot
        self.p_sing = self.sign.pop(Utils.random_choice(0,1))
        self.b_sign = self.sign[0]
        print("Start the game.")
        while True:
            match Game.victory(self):
                case 0:
                    if self.now == 'X':
                        print("Player won!")
                    else:
                        print("Computer won!")
                    break
                case 1:
                    print("It's a draw!")
                    break
                case 2:
                    pass
            Game.draw(self)
            if self.who_is == 0:
                Game.player(self)
                self.who_is = 1
            elif self.who_is == 1:
                Game.bot(self, ai)
                self.who_is = 0
    
    def player(self) -> None:
        foo: int = 0
        
        while True:
            try:
                foo = int(input("Player enter number from 1 to 9: "))
            except ValueError:
                print("Wrong input. Input must be a number!")
                continue
            if foo < 1 or foo > 9:
                print("Wrong input. Number must be in [1,9]")
                continue
            if self.grid[foo - 1] != ' ':
                print("Space is occupied.")
                continue
            else:
                self.grid[foo - 1] = self.p_sing
                self.players[self.p_sing].append(foo)
                self.now = self.p_sing
                break
    
    def bot(self, ai: int = 0):
        foo: int = 0
        
        if ai == 0:
            while True:
                foo = Utils.random_choice(0, 8)
                if self.grid[foo] == ' ':
                    self.grid[foo] = self.sign[0]
                    self.players[self.sign[0]].append(foo)
                    now = self.b_sign
                    break
        else:
            pass
            
    def victory(self) -> int:
        if self.now == ' ':
            return 2
        for x in self._all_possible_winning_possitions:
            if all(y in self.players[self.now] for y in x):
                return 0
        if len(self.players[self.p_sing]) + len(self.players[self.b_sign]) == 9:
            return 1
        else:
            return 2
        
            
def main() -> None:
    
    game = Game()
    game.mainloop()
    return 0


if __name__ == "__main__":
    main()
