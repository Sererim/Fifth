# 2021 candies
# two players
# each can take up to 28 candies from the stack
# make a bot 
# make a cleaver bot
# randomly decide who will be the first to pick candies
# last one to pick candies wins 
from utils import Utils
from operator import xor
class CandyGame():
    
    _possible_moves: list[int] = [i for i in range(0,29)]
    
    def __init__(self) -> None:
        
        candies: int = 151
        first_player: int = 0
        second_player: int = 0
        who_goes_first: int = 0
        who_goes_first = 0
        who_won = 0
        heapes: list[int] = [50, 50, 50]
        
        self.who_goes_first = who_goes_first
        self.who_won = who_won
        self.candies = candies
        self.first_player = first_player
        self.second_player = second_player
        self.heapes = heapes
    
    
    def draw(self) -> None:
        print(5 * " " + f"{Utils.color(0)}" + f"{self.candies}" + f"{Utils.color(6)}",
              f"\n{Utils.color(1)}" + f"{self.first_player}" + f"{Utils.color(6)}" ,
              11 * " " + f"{Utils.color(3)}" + f"{self.second_player}" + f"{Utils.color(6)}")
        
    def play(self, ai: int = 0) -> None:
        
        self.who_goes_first = Utils.random_choice(0, 1)
        
        while True:
            CandyGame.draw(self)
            
            if self.who_won == 1 or self.who_won == 2:
                CandyGame.victory(self)
                break     
            
            if self.who_goes_first == 0:
                CandyGame.player(self)
                self.who_goes_first = 1
            elif self.who_goes_first == 1:
                if ai == 1:
                    CandyGame.stupid_bot(self)
                else:
                    CandyGame.cleaver_bot(self)
                self.who_goes_first = 0
            
    def stupid_bot(self) -> None:
        num: int = 0
        while True:
            num = Utils.random_choice(1, 28)
            self.second_player += num
            self.candies -= num
            if self.candies - num <= 0:
                self.who_won = 2
                break
            break
    
    def cleaver_bot(self) -> None:
        num: int = 0
        x: int = 0
        foo: int = 0
        while True:
            if self.candies > 300:
                num = 28
                self.candies -= num
                self.second_player += num
                break
            elif self.candies > 150:
                num = Utils.random_choice(1,28)
                self.candies -= num
                self.second_player += num
                break
            elif self.candies > 0:
                x = xor(xor(self.heapes[0], self.heapes[1]), self.heapes[2])
                if x not in self._possible_moves:
                    num = Utils.random_choice(1, 28)
                    self.candies -= num
                    self.second_player += num
                    for x in range(0, num):
                        if self.heapes[foo] - (num + x) >= 0:
                            self.heapes[foo] -= (num + x)
                            foo = Utils.random_choice(0, 2)
                            self.heapes[foo] -= x
                    break
                elif x in self._possible_moves:
                    num = x
                    self.candies -= num
                    self.second_player += num
                    for x in range(0, num):
                        if self.heapes[foo] - (num + x) >= 0:
                            self.heapes[foo] -= (num + x)
                            foo = Utils.random_choice(0, 2)
                            self.heapes[foo] -= x
                    break
            else:
                self.who_won = 2
                break

    def player(self) -> None:
        num: int = 0
        while True:
            num = int(input(f"{Utils.message(3)}"))
            if Utils.isallowed(num, 0, 28):
                if self.candies - num <= 0:
                    self.who_won = 1
                    break
                self.candies -= num
                self.first_player += num
                break
            else:
                print("Error! Number must be between 1 and 28!")
    
    def victory(self) -> bool:
        if self.who_won == 1:
            print("Player won!")
            return True
        elif self.who_won == 2:
            print("Bot won!")
            return True
        return False
    
                  
def main() -> int:
    
    ai: int = 0
    
    game = CandyGame()
    
    ai = int(input("Enter 1 to play with a simple bot.\nEnter 2 to play with a hard bot.\n"))
    if not Utils.isallowed(ai, 1, 2):
        main()
    
    while True:
        game.play(ai)
        if Utils.terminate():
            break
   
    return 0


if __name__ == "__main__":
    main()