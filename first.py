# Find and delete all words that have 'абв'
from utils import Utils


class FindAndDelete():
    
    _undesiered: str = 'абв'
    
    def __init__(self) -> None:
        og_message: str = ""
        cleaned_message: str = ""
        
        self.og_message = og_message
        self.cleaned_message = cleaned_message
        
    def get_message(self, get: str) -> None:
        self.og_message = get
    
    def Find(self, word) -> bool:
        for i in range(len(word) - 2):
            if word[i] == self._undesiered[0]:
                if word[i + 1] == self._undesiered[1]:
                    if word[i + 2] == self._undesiered[2]:
                        return True
            elif len(word) < 3:
                return False
            else:
                return False
                 
    
    def clean(self) -> None:
        self.cleaned_message = filter(FindAndDelete.Find, self.og_message)
        
    def show(self) -> None:
        return self.cleaned_message
    
    
def main() -> int:
    
    message: str = ""
    fad = FindAndDelete()
    while True:
        message = input(Utils.message(7))
        fad.get_message(message)
        fad.clean()
        print(f" Original message: {fad.og_message}\n",
              f"Cleaned message: {fad.show}")
        
        if Utils.terminate:
            break
        
    return 0


if __name__ == "__main__":
    main()
