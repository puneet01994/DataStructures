# https://www.geeksforgeeks.org/the-stock-span-problem/


def stock_span(arr):
    result = [0 for i in range(len(arr))]
    result[0] = 1
    stack = []
    stack.append(0)

    for i in range(1, len(arr)):

        while len(stack) > 0 and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if len(stack) <= 0:
            result[i] = i+1

        else:
            result[i] = i-stack[-1]

        stack.append(i)

    return result


ar = [100, 80, 60, 70, 60, 75, 85]
data = stock_span(ar)
print(data)
