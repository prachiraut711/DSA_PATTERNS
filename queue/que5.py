#implementation of circular queue  (“Circular queue uses modulo arithmetic to reuse empty spaces and avoid memory wastage.)
# 622. Design Circular Queue

# 🔄 Circular Queue (Array Implementation)
# Why Circular Queue?

# Normal queue wastes space after dequeues.
# Circular queue reuses space by wrapping around using modulo %.

# ✅ Key Concepts

# front → index of first element

# rear → index of last element

# Queue is full when
# (rear + 1) % size == front

# Queue is empty when
# front == -1