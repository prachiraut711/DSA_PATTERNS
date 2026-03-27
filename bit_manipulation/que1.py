# Check if a Number is Even or Odd

# Key Idea (Bit Manipulation)

# 👉 Look at the last bit (LSB):

# Even number → last bit = 0
# Odd number → last bit = 1

# So we use:
# n & 1

def even_or_odd(n):
    if n & 1 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(10))
print(even_or_odd(5))


#alternative norml ethod
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")