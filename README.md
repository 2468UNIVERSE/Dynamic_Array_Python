📘 MyList – Custom Dynamic Array in Python

A complete custom implementation of Python’s list using ctypes and dynamic array resizing, built from scratch for learning low-level data structure internals.

🔥 Features

Dynamic resizing (like Python list / ArrayList)

Append, Insert, Remove

Pop, Clear

Find element

Extend with another list

Sort (ascending & descending)

Max & Min

Deletion by index

Custom __getitem__, __str__, __len__

Backed by C-style array using ctypes

🚀 How It Works

This project manually implements:

A resizable array

C-type storage (ctypes.py_object)

Manual resizing when list grows

Element shifting for insertion and deletion

Bubble-sort logic

Magic methods for indexing and printing

This helps understand how Python lists work internally.

🧠 Methods Implemented
Method	Description
append(item)	Add element at end
insert(index, item)	Insert at specific index
remove(item)	Remove first occurrence
pop()	Remove last item
extend(list)	Add multiple items
sort(bool=True)	Asc/Desc sorting
max()	Return largest element
min()	Return smallest element
sum()	Sum of elements
clear()	Clear the list
find(item)	Get index of an element
__len__()	Return number of items
__str__()	String representation
__getitem__(index)	Indexing support
__delitem__(index)	Delete by index

🎯 Goal of This Project

This project is built for learning how Python’s list works internally by manually implementing:

memory allocation

resizing

C-style arrays

element shifting

sorting
