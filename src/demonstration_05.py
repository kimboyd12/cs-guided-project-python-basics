"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""

# want to get the length of each list item and then sort
# sort func will take a key and a param for what you are looking for so this one is key = len since we are looking for the length

# could also use a lambda func

def sort_by_length(lst):
    # Your code here
    lst.sort(key = len)
    print(lst)
    
sort_by_length(["apple", "pie", "shortcake"])
sort_by_length(["may", "april", "september", "august"])