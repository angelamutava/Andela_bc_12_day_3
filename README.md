# Andela_bc_12_day_3
##Tasks for the day
-Andela Labs<br/>
1. Binary search<br/>
2. Missing number<br/>
-Front End Web<br/>
1.A simple front end appliaction created using CSS and HTML

##Binary search
This is a search mechanism that starts by searching the middle element.The best case is when the middle element is the element we are looking for.It uses the ordered nature of the list to eliminate half of the list.If for instance the element we are searching for is greater than the middle element then the middle and lower half are eliminated.We then move to the middle element in the upper half and repeat the process until we get the element we are looking for.The same applies for the other case where the element being searched for is lower than the middle element.

##Asymptotic Analysis of Binary search
Binary search eliminates about half of the elements out every comparison.This means the comparison will go eliminating for n elements n/2,n/4,n/8,n/16,n/32 and so on.Lets say there are i comparisons that means we will perforn n/2**i comparisons.
The best scenario in this case is when the middle element is what we are looking for and the worst case the log(n)

##Missing Number
This is a simple function that returns the missing number by comparing two lists.the number that is missing in both lists is returned.

##Front End Web Design
This is a simple two page application that demonstrates few fuctionalities kenyans portray.It is designed using css, html and javasript.
