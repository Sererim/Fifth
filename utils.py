from random import randint as random


class Utils:
    
    @staticmethod
    def message(num: int) -> str:
        
        words: list[str] =[
            "Program is running.\n",
            "Enter the size of a list.\n",
            "Enter numbers.\n",
            "Enter a number.\n",
            "Do you want to treminate the program Y/y ?.\n",
            "Error! Number must be positive!\n",
            "Error! k ∊ [1,6]\n",
            "Enter a string.\n"
        ]
        
        return words[num] 
    
    @staticmethod
    def terminate() -> bool:
        
        control: str = "NULL"
        while True:
            control = input(Utils.message(4))
            if control == "Y" or control == 'y':
                return True
            else:
                return False
    
    @staticmethod
    def ispositive(num: int) -> bool:
        if num > 0:
            return True
        else:
            return False
        
    @staticmethod
    def random_choice(x: int, y: int, z: int = 0) -> int:
        foo: int = 0
        
        if z == 0:
            foo = random(x, y)
    
        return foo
    
    def color(col: int):
        colors = ('\033[95m', #Header 0
                  '\033[94m', #Blue 1
                  '\033[96m', #Cyan 2
                  '\033[92m', #Green 3
                  '\033[93m', #Warning 4
                  '\033[91m', #Fail 5
                  '\033[0m', #ENDC 6
                  '\033[1m', #Bold 7
                  '\033[4m', #Underline 8
                  )
        return colors[col]

    def isallowed(num: int, left: int, right: int):
        
        if left <= num <= right:
            return True
        else:
            return False
