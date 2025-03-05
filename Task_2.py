#AbdelRahman Ahmed Mohammed Yassin   5

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are greater than key (higher grade, lower rank)
        while j >= 0 and key[1] > arr[j][1]:  # Sort by grades in descending order
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# A utility function to print names with grades
def printArray(arr):
    for name, grade in arr:
        print(f"{name}: {grade}")

# Driver method
if __name__ == "__main__":
    students = [
        ("Hazem", 85),
        ("Hossam", 92),
        ("Nakrish", 78),
        ("Dawwood", 88),
        ("lolo", 90)
    ]
    
    print("Before sort the names : ")
    printArray(students)
    insertionSort(students)
    print("After sorting : ")
    printArray(students)
