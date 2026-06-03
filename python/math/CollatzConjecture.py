class CollatzConjecture:
    def __init__(self, x):
        self.number = x
    
    def count(self):
        if not isinstance(self.number, int) or self.number < 0:
            print("Please type interger number (>0)")
            return
        
        step = 0
        sequence = []
        cur = self.number

        while cur != 1:
            if cur%2 == 0:
                cur = cur//2
            else:
                cur = (cur*3) + 1
            sequence.append(cur)
            step += 1
        print(", ".join(map(str,sequence)))
        print(step)

try:
    x = int(input("Please enter number: "))
    step = CollatzConjecture(x)
    step.count()
except ValueError:
    print("Please input a valid integer!")