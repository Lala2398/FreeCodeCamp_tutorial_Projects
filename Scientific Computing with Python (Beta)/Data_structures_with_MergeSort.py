def merge_sort(array):
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))



'''
Merge Sort is a divide and conquer algorithm used for sorting an array or list. 
It works by recursively dividing the array into two halves, sorting them individually, and then merging the two sorted halves into a single sorted array. 
It is highly efficient for large datasets.
-Steps:
        Divide the array into two halves.
        Recursively sort each half.
        Merge the sorted halves together.
-Time Complexity: O(n log n)
-Space Complexity: O(n)


Data Structures are ways of organizing and storing data to perform operations efficiently. 
They are fundamental for solving computational problems and are used in algorithms and programming.
Efficient data structures improve performance in searching, sorting, and managing data
Common Types of Data Structures:
        -Arrays: Fixed-size collection of elements.
        -Linked Lists: Elements linked via pointers.
        -Stacks and Queues: Linear structures with specific rules (LIFO/FIFO).
        -Trees: Hierarchical data structures like binary trees.
        -Graphs: Nodes (vertices) connected by edges.
        -Hash Tables: Key-value pairs for fast lookups.'''
