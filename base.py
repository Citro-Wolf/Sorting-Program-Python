import time 
startTime = time.time()
# Welcome to hell!
file = open("numbers.txt","r")
data = []
for line in file:
    data.append(int(line))
file.close()
def bubbleSort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if (swapped == False):
            break

    print("Sorted array:")
    for i in range(len(data)):
        print("%d" % data[i], end=" ")
bubbleSort(data)
endTime = time.time() - startTime
print(f"Your searching algorithm took {endTime} seconds.")