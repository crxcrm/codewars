-- Given a posts table that contains a created_at timestamp column write a query that returns a first date of the month, a number of posts created in a given month and a month-over-month growth rate.
-- The resulting set should be ordered chronologically by date.

-- Note:
-- percent growth rate can be negative
-- percent growth rate should be rounded to one digit after the decimal point and immediately followed by a percent symbol "%". See the desired output below for the reference.

select date, count, 
round((100.0 * (count - lag(count, 1) over (order by date)) / lag(count, 1) over (order by date)),1) || '%' as percent_growth
from (select CAST(date_trunc('month', created_at) AS DATE) as date, 
      count(id) as count
      from posts
      group by date) tab
order by date asc;
