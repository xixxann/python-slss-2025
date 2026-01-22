# Weekly Journal
5 December 2025
Angel Li

## Selection Sort

> Given the following list, using selection sort, sort the indicated element. Outline the steps you would follow in a way similar to the notes.

```
The List:

-- indicates that this part of the list is already sorted
** indicates the element that you should sort

Setup:
------
  --  --  **   3    4   5
[-11,  1, 43, 55, 100, 34]
lowest_num = 43
lowest_index = 2

1st Comparison:
---------------
  --  --  **  %%   4   5
[-11,  1, 43, 55, 100, 34]
lowest_num = 43
current_num = 55
lowest_index = 2
"current_num is not lower than 43, move to the next num"

2nd Comparison:
---------------
  --  --  **  3   %%   5
[-11,  1, 43, 55, 100, 34]
lowest_num = 43
current_num = 100
lowest_index = 2
"currrent_num is not lower than 43, move to the next num"


3rd Comparison:
-----------------------
  --  --  **  3    4   %%
[-11,  1, 43, 55, 100, 34]

lowest_num = 43
current_num = 34
lowest_index = 2
"current_nums is lower than 43, set lowest_num to 34 and set lowest_index to 5. We've reached the end!"

Swap!
-----
  --  --  **  3    4   L
[-11,  1, 43, 55, 100, 34]
"swap ** and L"

New values:
  --  --  --  3    4   L
[-11,  1, 34, 55, 100, 43]
```

## Sorting Algorithms

> Check out https://visualgo.net/en/sorting.

17

## Closing Questions

> How are you feeling?

Okay

> Do you have any food sensitivities or food that you avoid?

No

> What's a challenging concept, problem, or idea to understand you remember over the past week in programming?

Overall, I understand most of the code for search and sort. One challenging concept I encountered is understanding the syntax of some parts of the code such as:
```
def selection_sort(l: list[int], ascending=True) -> list[int]:
```

> Happy Friday