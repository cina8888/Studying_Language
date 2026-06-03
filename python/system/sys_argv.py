import sys

class systemcall:
    def __init__(self, x):
        self.x = x
    
    def view(self):
        return [i for i in self.x]

try:
    x = sys.argv[1:]
    syscall = systemcall(x)
    print(syscall.view())

except ValueError:
    print("Please input integer number")
