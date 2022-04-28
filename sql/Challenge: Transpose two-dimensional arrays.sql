-- Given a table with a following schema
--   Table "public.matrices"
 -- Column |  Type  | Modifiers
-- --------+--------+-----------
-- matrix | text[] | not null
-- which holds a set of two-dimensional text arrays i.e.
--      matrix
-- -------------------
-- {{1,2,3},{4,5,6}}
-- {{a,b,c},{d,e,f}}
-- (2 rows)
-- Your goal is to wite a SELECT statement or a CTE that returns array data in a transposed form

select array_agg(v order by j) matrix
from
(
  select rn,
          j,
         array_agg(v order by i) as v
  from
      (
       select rn,
               i,
               j,
              matrix[i][j] as v
       from
           (
            select generate_subscripts(matrix, 2) j,
                   q.*
            from
                (
                 select row_number() over()     as rn,
                        generate_subscripts(matrix, 1) as i,
                        matrix
                 from matrices) q
            ) r
       )s
group by rn, j
) t
group by rn
order by rn;
