CS 3364 Design and Analysis of Algorithms
Project (Total: 150 points)
Due December 5th, 2024
Submission requirements:
• A .zip file containing your source code. You may use any language you
would like.
• A PDF (submitted separately to the Blackboard assignment) containing each item below that is listed as a Deliverable. For each item
contained in your PDF, clearly mark which deliverable it is associated
with. Plots should be clearly labeled and have descriptive captions.
Part 1: Hybrid Sorting Methods [100 points]
In class, we’ve seen that divide-and-conquer methods can be used to create blazingly fast sorting algorithms such as Mergesort and Quicksort with
average-case (sometimes worst-case) time complexity Θ(n log n). What we
haven’t discussed as much is the fact that for small arrays, the elementary
sorting algorithms (insertion sort, bubble sort, selection sort) aren’t really
1
all that slow, even though they have worst-case time complexity of Θ(n
2
). In
fact, it can happen that the best elementary sorting algorithms are actually
faster than Mergesort on very small arrays. What can we do with this fact?
We can use Mergesort to handle large arrays, and then when the arrays in
Mergesort’s recursion get small enough, pass them to an elementary sorting
algorithm like Insertion sort to finish up. This is known as hybrid sorting
since we’re combining two types of sorting algorithm. If the implementations are good, the combination of the two can be faster in general than
either algorithm individually. This project will explore this phenomenon.
Your task:
Create a new sorting algorithm HybridSort(A[n],K) that takes two inputs:
• A[n]: A numerical array of length n.
• K: A length threshold; note that you must have K ≥ 1. If n ≤ K, your
algorithm should sort it using Insertion Sort. If n > K, your algorithm
should sort it using Mergesort.
Since it is a sorting algorithm your algorithm should return or compute a
new array that contains exactly the same elements as the input array and
is sorted ascending. Your algorithm may operate in-place or return a new
sorted array; the choice is yours.
The high-level operation of your algorithm should work as follows, given
correctly-implemented subroutines InsertionSort(A[n]) and Merge(B[p],C[q]):
2
Task 1: Implement the provided algorithm in a language of your choice,
also providing your own implementations of InsertionSort and Merge. Test
your implementation thoroughly for correctness (e.g., use your programming
language’s built-in sorting algorithm and make sure it agrees with your algorithm on every input).
Deliverable 1.1: Your implementation’s code and your verification of
correctness. (20 points)
Task 2: Generate a plot (or plots) which depicts your algorithm’s average
running time as a function of K and n on input arrays that you generate
randomly (i.e., input arrays for this deliverable should not be pre-sorted in
any way). Your “mental model” here should be that K will be relatively small
(under 100) and n will be relatively large (as large as your implementation can
handle in a reasonable amount of time). As you are running the tests, select
values of K and n which showcase interesting phenomena. For example, you
might expect very low and very high values of K to have poor performance,
but moderate values to have good performance. If that intuition holds, make
sure you plot your running times in such a way that this phenomenon is
3
clearly depicted in your plot. Finally, a note on “average running time”: for
a specific value of K and n, a single run of your algorithm is not enough to
tell you anything about its average running time. To compute an average for
a specific value of n, you’ll need to generate several random arrays of length
n, feed them all to the algorithm for your fixed value of K, then compute
the average of the running times you obtained.
Deliverable 1.2: A plot showing the average run time of your algorithm
as a function of K, with a separate trace for at least 5 representative values
of n. (20 points)
Task 3: Identify the optimal value of K as a function of array length n.
This should be informed by (or answered by) your analysis in the previous
step. How much does the best choice of K depend on n? Note: depending
on your implementation, it could happen that this optimal K will be the
same for all n. If that’s the case, report it anyway. Try to understand any
relationship (or lack of relationship) that you find.
Deliverable 1.3: A plot showing the optimal value of K as a function
of array length n. Explain why you think the relationship between n and
optimal K is the way that it is. (30 points)
Task 4: Repeat deliverables 2 and 3; however, this time, test your algorithm only on sorted arrays. How do the results differ from what you
reported in Deliverables 2 and 3? Explain these differences to the best of
your ability.
Deliverable 1.4: Your observations and findings from Task 4. (30
4
points)
Further Reading: The default sorting algorithm used in Python is
called “Timsort” after its creator Tim Peters, who created it for Python.
A version of Timsort is still used as Python’s native sorting algorithm to
this day. It is hybrid, and also highly optimized (it does advanced things
like looking for already-sorted subarrays so it can adaptively skip things it
doesn’t need to do). Read more here.
Instructions for Generating Plots
Python with Matplotlib:
1. Install the required libraries:
pip install matplotlib
2. Use the following template to plot:
import matplotlib.pyplot as plt
K_values = [...] # Fill with your K values
avg_times = [...] # Fill with your average times
plt.plot(K_values, avg_times)
5
plt.title(’HybridSort Performance’)
plt.xlabel(’K Value’)
plt.ylabel(’Average Time (s)’)
plt.grid(True)
plt.show()
Excel:
1. Input your data into columns: one for K values and another for average
times.
2. Highlight the data columns.
3. Go to the ”Insert” tab and select ”Line Chart”.
4. Label your axes, and provide a title.
R:
1. Install ggplot2:
install.packages("ggplot2")
2. Use this template to plot:
6
library(ggplot2)
data = data.frame(K=..., avg_time=...) # Fill with your data
ggplot(data, aes(x=K, y=avg_time)) + geom_line() +
ggtitle(’HybridSort Performance’) +
xlab(’K Value’) +
ylab(’Average Time (s)’)
Tips:
• Label all axes for clarity.
• If plotting multiple values of n, consider using different colors or styles.
Part 2: Packing for the Trip (Knapsack Problem) [50 points]
Background
Assume we are in the year 3089, intergalactic travel has become a reality.
As a travel planner for ”Galaxy Getaways,” you are tasked with planning
a grand tour for a group of space tourists. Your challenges include for the
7
trip ensuring that tourists get the best experiences within their luggage constraints.
Scenario:
Planet Xanadu offers various unique experiences, each requiring different
equipment. Tourists need to maximize their experiences while adhering to
their luggage weight restrictions.
Experiences and Equipment:
Experience ID Weight Value (Enjoyment Points)
1 8 1500
2 7 1600
3 6 1700
4 5 1800
5 4 3000
Luggage Weight Limit: W = 20
Tasks:
1. State Definition (10 Points): Define the subproblems in terms of
maximizing the total enjoyment points without exceeding the luggage
weight limit.
Deliverable 2.1: A written definition that clearly outlines the subproblems in the context of maximizing enjoyment points within the
luggage weight limit.
8
2. Recurrence Relation (10 Points): Develop the recurrence relation
for the knapsack problem given the weights and values of the experiences.
Deliverable 2.2: A detailed explanation of the recurrence relation
derived for this specific Knapsack problem, clearly showing how the
weights and values influence the decision-making process.
3. Implementation (20 Points): Propose a dynamic programming solution to calculate the maximum enjoyment points achievable within
the weight constraint.
Deliverable 2.3: Code implementing a dynamic programming solution to compute the maximum enjoyment points within the weight
limit. The code should be well-commented to explain each step.
4. Analysis (10 Points): Detail which experiences were chosen for the
optimal solution and provide a rationale for your selections.
Deliverable 2.4: A written analysis listing the experiences chosen for
the optimal solution, with a clear rationale for why these experiences
maximize enjoyment within the weight constraint.
Remember, the primary goal of this task is to demonstrate
your understanding of dynamic programming, specifically Knapsack problems. Focus on clarity, logical flow, and thoroughness in
your solutions.
