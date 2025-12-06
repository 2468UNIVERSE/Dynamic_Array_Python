# MyList – Custom Dynamic Array in Python.
A complete custom implementation of Python’s list using ctypes and dynamic array resizing, built from scratch for learning low-level data structure internals.

## Features:
1- Dynamic resizing (like Python list / ArrayList)
2- Append, Insert, Remove
3- Pop, Clear
4- Find element
5- Extend with another list
6- Sort (ascending & descending)
7- Max & Min
8- Deletion by index
9- Custom __getitem__, __str__, __len__
10- Backed by C-style array using ctypes

## How It Works? 
### This project manually implements:
1- A resizable array
2- C-type storage (ctypes.py_object)
3- Manual resizing when list grows
4- Element shifting for insertion and deletion
5- Bubble-sort logic
6- Magic methods for indexing and printing
7- This helps understand how Python lists work internally.

## Methods Implemented:
| Method                | Description              |
| --------------------- | ------------------------ |
| `append(item)`        | Add element at end       |
| `insert(index, item)` | Insert at specific index |
| `remove(item)`        | Remove first occurrence  |
| `pop()`               | Remove last item         |
| `extend(list)`        | Add multiple items       |
| `sort(bool=True)`     | Asc/Desc sorting         |
| `max()`               | Return largest element   |
| `min()`               | Return smallest element  |
| `sum()`               | Sum of elements          |
| `clear()`             | Clear the list           |
| `find(item)`          | Get index of an element  |
| `__len__()`           | Return number of items   |
| `__str__()`           | String representation    |
| `__getitem__(index)`  | Indexing support         |
| `__delitem__(index)`  | Delete by index          |

## Goal of This Project
### This project is built for learning how Python’s list works internally by manually implementing:
1- memory allocation
2- resizing
3- C-style arrays
4- element shifting
5- sorting
