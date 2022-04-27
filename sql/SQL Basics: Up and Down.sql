-- Given a table of random numbers as follows:

-- numbers table schema: id, number1, number2
-- Your job is to return table with similar structure and headings, where if the sum of a column is odd, the column shows the minimum value for that column, and when the sum is even, it shows the max value. You must use a case statement.

-- output table schema: number1, number2

select (case when MOD(SUM(number1),2)=0 then max(number1) else min(number1) end) as number1, 
(case when MOD(SUM(number2),2)=0 then max(number2) else min(number2) end) as number2 from 
numbers;
