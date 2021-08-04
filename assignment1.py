>>> n = int(input("Enter number of elements : "))
Enter number of elements : 6
>>> # Below line read inputs from user using map() function
>>> a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

Enter the numbers : 4 5 6 7 8 9 4 5
>>> print("\nList is - ", a)

List is -  [4, 5, 6, 7, 8, 9]
>>> minimum=min(a)
>>> print(minimum)
4
>>> maximum=max(a)
>>> print(maximum)
9
>>> print('Sum og Array',sum(a))
Sum og Array 39
>>> print('length of array',len(a))
length of array 6
>>> print('Average of array',(sum(a)/len(a))
... )
Average of array 6.5