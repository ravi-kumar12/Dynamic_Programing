**This directory contain all dynamic programming competitive knapsack based problem.**

Dynamic apporoach is used when we want to try all the possibilities and after that we want to select most optimal one from that all possibilities. Process decreases time
complexity significantly from brute force algorithm.

**How to recognise the problem is knapsack based:**
1. If a sequence of array is given and we have given some optimal result problem.
2. Problem involve selection of some element which very much mean that for every element in array we have option of either including it or not.

If we have given a single array, we very much to consider it similar to weight array.

**Problem included:**
1.  0/1 knapsack
2.  Unbounded Knapsack
3.  Subset Sum Problem
4.  Equal Sum Partition Problem
5.  Count the Subset Sum with Given Sum
6.  Minimun Subset Sum Different
7.  Count the No Of Subset with A Given Difference
8.  Target Sum
9.  Rod Cutting Problem
10. Coin Change Problem:Maximum No Of Ways
11. Coin Change Problem:Minimun No Of Coins

(3-8) is on 0/1 Knapsack.
(9-11) is on Unbounded Knapsack.

The only different in b/w two above knapsack is that in Unbounded there is unlimited supply of element whereas in 0/1, we can include each element once.

Each Problem Solve Using Three Approach:
**1.TOP-DOWN:**
            Filling a table from including 0 element to all element and finding the optimal result according to question in per step. Y-axis represent arrays element. 0 y-axis 
            mean no element included and last index on Y-axis mean all element included. X-axis of table mean contraint ranging from 0 to max.
            Since we have to fill an entire 2-d table and hence *time complexity is n**2.*
            
**2.Recursion+Memonisation:**
            By continous recursive calling minimising the problem to smallest possible problem and solving the smallest problem and passing their result to larger problem so 
            that they can be solved. In this with each recursive call, we store the result in a table so that when the function is called again with same attribute, we can fetch
            the value from table and henceforth minimising the work load of program and therefor minimising time complexity.
            Without memonization, its *time complexity is 2^n but with menomisation, the time complexity reduce to n^2.
            
**3.Recursion(only):**
            Same mentioned above.*Time complexity is 2*n* that mean for every n element we try each possibility of whether to take it or not. Hence 2*2*2...n times i.e 2^n.
        
            
**OUTPUT:**
          Integer giving total element included result and the result itself.
          
          
**How To Recognise a Problem is Knapsack Based aor not:**
           If these condition apply:
           1.An array of element is given.
           2.If given to find optimal result.
           3.Output is int or array type.

