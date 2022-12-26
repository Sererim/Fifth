# 2021 candies
# two players
# each can take up to 28 candies from the stack
# make a bot 
# make a cleaver bot
# randomly decide who will be the first to pick candies
# last one to pick candies wins 
from utils import Utils

class CandyGame():
    
    def __init__(self) -> None:
        
        candies: int = 2021
        first_player: int = 0
        second_player: int = 0
        who_goes_first: int = 0
        who_goes_first = Utils.random_choice(1,2)
        who_won = 0
        
        self.who_goes_first = who_goes_first
        self.who_won = who_won
        self.candies = candies
        self.first_player = first_player
        self.second_player = second_player
        
    def draw(self) -> None:
        print(5 * " " + f"{Utils.color(0)}" + f"{self.candies}" + f"{Utils.color(6)}",
              f"\n{Utils.color(1)}" + f"{self.first_player}" + f"{Utils.color(6)}" ,
              11 * " " + f"{Utils.color(3)}" + f"{self.second_player}" + f"{Utils.color(6)}")
        
    def play(self) -> None:
        
        
        if self.who_goes_first == 1:
            CandyGame.player(self)
       # elif self.who_goes_first == 2:
            # CandyGame.stupid_bot()
        
    # def stupid_bot(self) -> None:
    #    pass
    
    def cleaver_bot(self) -> None:
        pass
    
    def player(self) -> None:
        num: int = 0
        while True:
            num = int(input(f"{Utils.message(3)}"))
            if Utils.isallowed(num, 0, 28):
                if self.candies - num <= 0:
                    self.who_won = 1
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
    
    game = CandyGame()
    while True:
        game.draw()
        game.play()
        if game.victory():
            print("GOOD")
            break
    return 0


if __name__ == "__main__":
    main()