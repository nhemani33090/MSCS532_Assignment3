
# Quicksort and Hash Table with Chaining

## Description
This project implements and analyzes two key algorithms:

1. **Quicksort Analysis**: Includes implementations of both deterministic and randomized Quicksort, with performance comparisons on various input types.
2. **Hash Table with Chaining**: A hash table that resolves collisions using chaining, supporting efficient insert, search, and delete operations.

---

## File Structure
- **`quicksort_analysis.py`**: Implements deterministic and randomized Quicksort algorithms and compares their performance.
- **`hash_table_chaining.py`**: Implements a hash table with chaining for collision resolution.

---

## How to Run the Code

### Prerequisites
- Python 3.x installed on your system.

### Steps to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/nhemani33090/MSCS532_Assignment3.git
   cd MSCS532_Assignment3
   ```
2. Run the **Quicksort Analysis**:
   ```bash
   python3 quicksort_analysis.py
   ```
   - This script will compare the performance of deterministic and randomized Quicksort on different input types, such as random, sorted, reversed, and repeated arrays.

3. Test the **Hash Table with Chaining**:
   ```bash
   python3 hash_table_chaining.py
   ```
   - This script demonstrates operations like inserting, searching, and deleting key-value pairs in the hash table.

---

## Summary of Findings

### **Quicksort Analysis**
- **Randomized Quicksort**:
  - Uses a randomly chosen pivot, which reduces the likelihood of poor splits and achieves better performance on average.
  - **Time Complexity**:
    - Best Case: \(O(n \log n)\)
    - Average Case: \(O(n \log n)\)
    - Worst Case: \(O(n^2)\), though this is rare due to the randomness in pivot selection.

- **Deterministic Quicksort**:
  - Uses a fixed pivot (e.g., the first or last element), which makes it more prone to poor splits when the input is sorted or nearly sorted.
  - **Time Complexity**:
    - Best Case: \(O(n \log n)\)
    - Average Case: \(O(n \log n)\)
    - Worst Case: \(O(n^2)\), when the pivot consistently results in unbalanced partitions.

### **Hash Table with Chaining**
- Handles collisions by maintaining chains (linked lists) for each bucket.
- **Time Complexity** (on average):
  - Search: \(O(1)\)
  - Insert: \(O(1)\)
  - Delete: \(O(1)\)
- The hash table dynamically resizes when the load factor exceeds 0.75, ensuring high efficiency even as it grows.

---