-- For this challenge you need to create a VIEW. This VIEW is used by a sales store to give out vouches to members who have spent over $1000 in departments that have brought in more than $10000 total ordered by the members id. The VIEW must be called members_approved_for_voucher then you must create a SELECT query using the view. 

create view members_approved_for_voucher as
select memb.id, memb.name, email, total_spending
from
(
select member_id as "id", m.name, email, sum(price) as "total_spending"
from sales s 
join products p on (s.product_id = p.id)
join members m on (s.member_id = m.id)
join
(
  select department_id as "id", sum(price)
  from sales s 
  join products p on (s.product_id = p.id)
  join departments d on (s.department_id = d.id)
  group by s.department_id
  having sum(price) > 10000
  ) d on (s.department_id = d.id)
group by s.member_id, m.name, email
having sum(price) > 1000
) memb;

select id, name, email, total_spending
from members_approved_for_voucher
order by id;
