# Dancing-Numbers-using-Python

Summary:
The 'generate_dancing_numbers' function generates dancing numbers up to a given limit. Dancing numbers are numbers in which the absolute difference between adjacent digits is always 1.

Example Usage:
dancing_numbers = generate_dancing_numbers(20)
for number in dancing_numbers:
    print(number)

Code Analysis:
  Inputs:
    'dancing_limit' (integer): The upper limit for generating dancing numbers.

Flow:
1. Iterate over the range from 0 to dancing_limit.
2. If the current number is less than 10, yield the number and continue to the next iteration.
3. Set check to 1 to indicate that the number is a dancing number.
4. Set temp to the current number.
5. Get the last digit of temp and assign it to digit.
6. Divide temp by 10 and assign the result back to temp.
7. While temp is greater than 0, do the following:
    Check if the absolute difference between digit and the last digit of temp is not equal to 1.
    If the condition is not met, set check to 0 to indicate that the number is not a dancing number and break the loop.
    Assign the last digit of temp to digit.
    Divide temp by 10 and assign the result back to temp.
8. If check is still 1, yield the current number as a dancing number.
