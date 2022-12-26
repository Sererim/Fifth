# Find and delete all words that have 'абв'
from utils import Utils


class FindAndDelete():
    
    _undesiered: list[str] = ['абв']
    
    def __init__(self) -> None:
        og_message: list[str] = []
        message: list[str] = []
        cleaned_message: str = ""
        
        self.og_message = og_message
        self.message = message
        self.cleaned_message = cleaned_message
        
    def get_message(self, get: str) -> None:
        foo: str = ""
        
        if len(get) < 3:
            get += " абв "
        
        for i in range(len(get)):
            if get[i] == ' ':
                pass
            elif i % 2 == 0:
                try:
                    foo += get[i] + get[i + 1] + get[i + 2]
                    self.og_message.append(foo)
                    foo = ""
                except IndexError:
                    pass
            else:
                pass
    
    def clean(self) -> None:
        self.message = list(filter(lambda x: x not in self._undesiered, self.og_message))    
        
    def show(self) -> str:
        for i in range(len(self.message)):
            self.cleaned_message += str(self.message[i])
        return self.cleaned_message
    
    
def main() -> int:
    
    message: str = ""
    fad = FindAndDelete()
    while True:
        message = input(Utils.message(7))
        fad.get_message(message)
        fad.clean()
        print(f" Original message: {fad.og_message}\n",
              f"Cleaned message: {fad.show()}")
        
        if Utils.terminate:
            break
        
    return 0


if __name__ == "__main__":
    main()
