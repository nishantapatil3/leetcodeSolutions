Kadane's Algorithm is used to solve maximum contiguous array sum
in short largest sub array

simple idea of kadane's algo is to look for positive contiguous segment of arrayand keep track of maximum contiguous array segment among all positive segments. each time we get max_so_far and if it is greater than max_till_here update max_so_far.

