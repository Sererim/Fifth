
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
    