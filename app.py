# Linear search function
def linear_search(arr, target):
    # Traverse through all elements in the list
    for i in range(len(arr)):
        # If the current element matches the target, return its index
        if arr[i] == target:
            return i
    # If target is not found, return -1
    return -1

# Main code to take user input
if __name__ == "__main__":
    try:
        # Taking input array from user
        arr = list(map(int, input("Enter the elements of the array (separated by space): ").split()))

        # Taking target value from user
        target = int(input("Enter the target element: "))

        # Call the linear search function
        result = linear_search(arr, target)

        # Display the result
        if result != -1:
            print(f"Element found at index: {result}")
        else:
            print("Element not found")
    except ValueError:
        print("Please enter valid integers for the array and target.")
