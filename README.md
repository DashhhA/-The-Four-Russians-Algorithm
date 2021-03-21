# The Four Russians Algorithm

Algorithm complexity: O(n^3/log(n)).

Algorithm implement boolean matrix multiplication in main method: four_russian_algo
which get 2 square matrices with size: size(in sample = 13), before this method
we need to prepare our matrices(first and second) by splitting them into matrices with size M = ROUNDDOWN(log10(N)).
For testing algo we create random matrices and multiply them by default multiplication and The Four Russians algo,
and check if they are equal.

To run the algorithm firstly go to the directory four-russians-dusklyarova and doubleclick on main.py 
or use console and write command: python3 main.py/test.py if you want to run tests. 

Literature which I used: https://louridas.github.io/rwa/assignments/four-russians/