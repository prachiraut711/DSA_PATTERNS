# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
# Input: s = "Mr Ding"
# Output: "rM gniD"


#approch 1 (without built in method)

def reverseWords(s):
    result = ""
    word = ""

    for ch in s:
        if ch != " ":
            word += ch
        else:
            # Reverse the word manually and add it to result
            i = len(word) - 1
            while i >= 0:
                result += word[i]
                i -= 1
            
            result += " "  # Add the space

            word = ""       # Reset word for next on
    
    # Reverse the last word after loop
    i = len(word) - 1
    while i >= 0:
        result += word[i]
        i -= 1

    return result

print(reverseWords("Mr Ding"))


#approch 2 (USING STACK)
def reverseWords(s):
    stack = []
    result = ""

    for ch in s:
        if ch != " ":
            stack.append(ch)
        else:
            while stack:
                result += stack.pop()
            
            result += " "
    
    while stack:
        result += stack.pop()

    return result

print(reverseWords("Hello World"))