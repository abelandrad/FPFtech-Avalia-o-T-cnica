(select name, customers_number
from lawyers
order by customers_number desc
limit 1)
UNION ALL
(select name, customers_number
from lawyers
order by customers_number
limit 1)
UNION ALL
(select
 'Average' as name,
 round(avg(customers_number)) as customers_number
 from lawyers limit 1)