def reverse_string(str):
    stack = []
    reversed = []
    split = list(str)   # convert string to a list

    # add characters into the stack
    for ch in split:
        stack.append(ch)

    # retrieve items from stack
    while len(stack) > 0:  # do items exist in the stack?
        item = stack.pop()   # retrieve the item at the top of the stack
        reversed.append(item)

    return ("".join(reversed))


print(reverse_string("remove"))
