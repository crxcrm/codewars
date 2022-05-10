
-- you will be given a table 'kata' with columns 'n', 'x', and 'y'. Return the 'id' and your result in a column named 'res'.

select id, 
  case when ((n % x = 0) AND (n % y = 0)) THEN true ELSE false
  end as res
from kata
