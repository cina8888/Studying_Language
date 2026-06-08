class Reverse:
    def __init__(self, arr):
        self.arr = arr
    
    def reverse(self, arr):
        n = len(self.arr)
        temp = []
        for i in range(n):
            temp.append(self.arr[n-i-1])
            
        for i in range(n):
            self.arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 32, 24, 56, 78, 45]
    rv = Reverse(arr)
    rv.reverse(arr)
    for i in arr:
        print(i, end = " ")
    print("")
