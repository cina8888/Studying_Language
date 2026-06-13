class Convert:
    def convert(self, a_string):
        total = 0
        temp = []
        for i in a_string:
            if (i.isupper()):
                temp.append(i.lower())
            elif (i.isdigit()):
                total += int(i)
                temp.append(i)
            else:
                temp.append(i.upper())
        return temp, total
a = "Hello123 45abc"
cv = Convert()
result, total = cv.convert(a)
print("".join(map(str, result)))
print(total)
