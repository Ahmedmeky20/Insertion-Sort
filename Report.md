# Insertion Sort

## 1. Objective

The objective of this project is to implement the Insertion Sort algorithm and analyze its performance experimentally.

The algorithm is tested using three types of input data: sorted, reverse-sorted, and random arrays. The running time is measured for different input sizes, ranging from 100 to 5000 elements.

The experimental results are then compared with the theoretical time complexity of the algorithm.

## 2. Methodology

The Insertion Sort algorithm was implemented using Python.

During the implementation, two operations were counted:

* **Comparisons:** The number of times an element is compared with the key.
* **Shifts:** The number of times an element is moved to the right to make space for the key.

To evaluate the algorithm's performance, three types of input data were tested:

1. **Sorted Input:** An array arranged in ascending order.
2. **Reverse-Sorted Input:** An array arranged in descending order.
3. **Random Input:** An array containing randomly generated integers.

The experiments were performed using input sizes ranging from 100 to 5000 elements, increasing by 100 elements each time.

Python's `time` module was used to measure the running time of each experiment, and Matplotlib was used to plot the results.



## 3. Results and Discussion

The experimental results showed different performance levels depending on the input arrangement.

* **Sorted Input:** Insertion Sort achieved the best performance because the elements were already arranged in ascending order. It required very few shifts, and its running time increased approximately linearly with the input size.

* **Reverse-Sorted Input:** This case showed the worst performance because each new element had to be moved through the previously processed elements. The running time increased significantly as the input size grew, following a quadratic growth pattern.

* **Random Input:** The running time was between the sorted and reverse-sorted cases. As the input size increased, the running time generally followed a quadratic growth pattern.

The results are consistent with the theoretical time complexity of Insertion Sort:

* Best Case: O(n)
* Average Case: O(n²)
* Worst Case: O(n²)

Small variations in the measured running times are expected because of computer performance and background processes.



## 4. Comparison with Merge Sort

Insertion Sort and Merge Sort are both sorting algorithms, but they have different performance characteristics.

| Feature                     | Insertion Sort | Merge Sort             |
| --------------------------- | -------------- | ---------------------- |
| Best Case                   | O(n)           | O(n log n)             |
| Average Case                | O(n²)          | O(n log n)             |
| Worst Case                  | O(n²)          | O(n log n)             |
| Extra Space                 | O(1)           | O(n)                   |
| Performance on Small Arrays | Efficient      | Usually less efficient |

Merge Sort is generally more efficient for large datasets because its time complexity is O(n log n), while Insertion Sort has O(n²) average and worst-case complexity.

However, Insertion Sort is simple to implement and requires less extra memory.

## 5. Conclusion

This project demonstrated the practical performance of the Insertion Sort algorithm under different input conditions.

The experiments confirmed that the input arrangement has a significant effect on running time. Insertion Sort performs very well with sorted data but becomes slower with reverse-sorted and random data as the input size increases.

In conclusion, Insertion Sort is suitable for small or nearly sorted datasets, while Merge Sort is generally a better choice for large datasets.
