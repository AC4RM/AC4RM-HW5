### Introduction
- This the week 5 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Define a function `list_comp(input_list)`, that uses list comprehension to assign `a` to the numbers greater than 8; `b` to the numbers less or equal to 8 and greater than 5; `c` to everything else.
   - E.g. `list_comp(list(range(1, 11)))` => `['c', 'c', 'c', 'c', 'c', 'b', 'b', 'b', 'a', 'a']`
2. Write the sql query to do the following. You can assume that we have the `payment` and `clients` table from the lecture.
   - Find the name of the customer who made the largest payment.
3. Using the iris datasets from the sklearn package, try to group the observations into clusters using all the features.
   - The four columns in the iris dataset are `sepal length`, `sepal width`, `petal length`, `petal width`.
   - Draw the elbow plot to figure out the optimal value of K (K within the range of 1 to 10). 
   - Return the K-means model re-fitted with the optimal K.
4. - Write a regex pattern with named groups that can extract the month, date and year from the string.
   - The groups should be named `month`, `date`, `year` correspondingly. For example:
     - `result = re.search(regex_pattern, '05/31/2023')`
     - `result.group('month')` == `05`
5. Implement a new strategy in `double_bettor(initial_funds, initial_wager, intended_rounds)` that:
   - When the player loses, the player doubles the previous bet size. This is called a Martingale strategy.
   - The doubling continues until a win, then the bet size returns to the initial wager.
   - Return the path of the player fund.
