# RLE--algorithm
# IN: "WWWWWWWWWWWWWAAAAAAAAAAASSSSSSSSS"
# OUT: 13WA11S9

from utils import Utils


class RLE():
    
    def __init__(self, original_message: str) -> None:
        coded_message: str = ""
        decoded_message: str = ""
        
        self.original_message = original_message
        self.coded_message = coded_message
        self.decoded_message = decoded_message
        
    def encode(self) -> None:
        
        char: str = ""
        count: int = 0
        
        for i in range(len(self.original_message) - 1):
            if char == self.original_message[i]:
                pass
            else:
                char = self.original_message[i]
                count = 1
                for j in range(i, len(self.original_message) - 1):
                    if self.original_message[j] == self.original_message[j + 1]:
                        count += 1
                    else: 
                        break
                self.coded_message = self.coded_message + str(count) + char
    
    def decode(self) -> None:
        
        count_num: int = 0
        count_word: str = ""
        i: int = 0
        
        
        while i < len(self.coded_message) - 1:
            count_num = int(self.coded_message[i])
            count_word = self.coded_message[i + 1]
            
            for j in range(count_num):
                self.decoded_message = self.decoded_message + count_word
            i += 2
    
    def show(self) -> None:
        print(f" Original string: [{self.original_message}]\n",
              f"Encoded message: [{self.coded_message}]\n",
              f"Decoded message: [{self.decoded_message}]")
        
    
def main() -> int:
    
    message: str = ""
    
    while True:
        print(Utils.message(0))
        message = input(Utils.message(7))
        rle = RLE(message)
        rle.encode()
        rle.decode()
        rle.show()
        
        if Utils.terminate():
            break
        
    return 0
    
    
if __name__ == "__main__":
    main()        
