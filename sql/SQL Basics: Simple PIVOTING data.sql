-- For this challenge you need to PIVOT data. You have two tables, products and details. Your task is to pivot the rows in products to produce a table of products which have rows of their detail. Group and Order by the name of the Product.

CREATE EXTENSION tablefunc;

SELECT *
FROM  crosstab(
  'SELECT
      products.name, details.detail, COUNT(details.id)
  FROM products 
  JOIN details  ON details.product_id = products.id
  GROUP BY products.id, details.detail
  ORDER BY 1,2',
  $$values ('good'), ('ok'), ('bad')$$)
AS ct (name text, good int, ok int, bad int)
