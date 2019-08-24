# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(n):
            if (i + 1) % 3 == 0:
                if (i + 1) % 5 == 0:
                    ans.append("FizzBuzz")
                else:
                    ans.append("Fizz")
            elif (i + 1) % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i + 1))
        
        return ans
