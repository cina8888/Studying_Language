def getSecondLargest(arr):
    largest = Slargest = float("-inf")
    for x in arr:
        if x > largest:
            Slargest = largest
            largest = x
        elif x < largest and x > Slargest:
            Slargest = x
    return Slargest if Slargest != float("-inf") else -1

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))