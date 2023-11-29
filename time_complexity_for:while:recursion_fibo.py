import time

def fibonacci_for_loop(n):
    one,two = 0,1
    for _ in range(n-1):
        temp = two
        two = one+two
        one = temp        
    return two    


def fibonacci_while_loop(n):
    one,two = 0,1
    while n-1:
        temp = two
        two = one+two
        one = temp
        n -= 1
    return two

def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_recursion(n-1) + fibonacci_recursion(n-2))


def fibonacci_dynamic_programming_tabulation(n):
    memo = [0] * (n+1)
    if n <= 2:
         return n
    memo[0] = 0
    memo[1] = 1
    for i in range(2,n+1):
           memo[i] = memo[i-1] + memo[i-2]   
    return memo[n]


def fibonacci_dynamic_programming_memoization(n):
    memo = [0,1]
    for _ in range(n-1):
        memo.append(memo[-1]+memo[-2])
    return memo[-1]


array_time_fibonacci_for_loop = []
array_time_fibonacci_while_loop = []
array_time_fibonacci_recursion = []
array_time_fibonacci_dynamic_programming_tabulation= []
array_time_fibonacci_dynamic_programming_memoization = []


for i in range(25):  
    start_fibonacci_for_loop = time.time_ns()
    fibonacci_for_loop(i)
    end_fibonacci_for_loop = time.time_ns()
    array_time_fibonacci_for_loop.append(end_fibonacci_for_loop - start_fibonacci_for_loop)

    start_fibonacci_while_loop = time.time_ns()
    fibonacci_while_loop(i)
    end_fibonacci_while_loop = time.time_ns()
    array_time_fibonacci_while_loop.append(end_fibonacci_while_loop - start_fibonacci_while_loop)

    start_fibonacci_recursion = time.time_ns()
    fibonacci_recursion(i)
    end_fibonacci_recursion = time.time_ns()
    array_time_fibonacci_recursion.append(end_fibonacci_recursion - start_fibonacci_recursion)

    start_fibonacci_dynamic_programming_tabulation = time.time_ns()
    fibonacci_dynamic_programming_tabulation(i)
    end_fibonacci_dynamic_programming_tabulation = time.time_ns()
    array_time_fibonacci_dynamic_programming_tabulation.append(end_fibonacci_dynamic_programming_tabulation - start_fibonacci_dynamic_programming_tabulation)

    start_fibonacci_dynamic_programming_memoization = time.time_ns()
    fibonacci_dynamic_programming_memoization(i)
    end_fibonacci_dynamic_programming_memoization = time.time_ns()
    array_time_fibonacci_dynamic_programming_memoization.append(end_fibonacci_dynamic_programming_memoization - start_fibonacci_dynamic_programming_memoization)