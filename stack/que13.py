#greksforgreeks problem
# Stock Span Problem
# Last Updated : 25 Sep, 2025
# Given an array arr[] of daily stock prices, the stock span for the i-th day is the count of consecutive days up to and including day i, such that each of those days had a stock price less than or equal to the price on day i.
# Examples:
# Input: arr[] = [100, 80, 60, 120]
# Output: [1, 1, 1, 4]
# Explanation: For 100, there are no previous higher prices, so span = 1. For 80 and 60, each is smaller than the previous, so their spans remain 1. For 120, it is greater than all earlier prices (100, 80, 60), so the span extends back across all four days, giving span = 4.
# Input: arr[] = [10, 4, 5, 90, 120, 80]
# Output: [1, 1, 2, 4, 5, 1]
# Explanation: For 10 and 4, no earlier prices are smaller, so span = 1 each. For 5, it is greater than 4, so span = 2. For 90, it is greater than 10, 5, and 4, so span = 4. For 120, it is greater than all previous prices, giving span = 5. Finally, 80 is smaller than 120, so span = 1.


#this is MONOTONIC Decreasing STACK  problem(means stack's top < element)
def stockProblem(arr):
    stack = []
    span = [0] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            span[i] = i - stack[-1]
        else:
            span[i] = i + 1
        stack.append(i)
    return span

print(stockProblem([100, 80, 60, 120]))
print(stockProblem([10, 4, 5, 90, 120, 80]))

# 901. Online Stock Span
#leetcode version of this problem

# Medium
# Topics
# premium lock icon
# Companies
# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:

# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.
 

# Example 1:

# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]

# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6
 

# [10, 4, 5, 90, 120, 80]
# Day	Price	Span Reason
# 10	10	    no previous → 1
# 4	     4	     smaller than 10 → 1
# 5	     5	     beats 4 → 2
# 90	90	    beats 10,5,4 → 4
# 120	120   	beats all → 5
# 80	80	  smaller than 120 → 1

##For each day, count how many consecutive previous days (including today) had prices ≤ today’s price

#here next function include - One price per call  while in greeksforce question above - all array at once
class StockSpanner(object):

    def __init__(self):
        self.stack = []
        
    def next(self, price):
        span = 1
        # pop all smaller or equal prices
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        # push current price with its span
        self.stack.append((price, span))   #append() takes exactly one argument so in bracket ( (price,span) )
        
        return span