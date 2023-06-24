create view real_time_confirmed as 
select confirmed_date as date, province, city, infection_case, count(*) as confirmed 
from patientinfo 
group by confirmed_date, province, city, infection_case 
order by confirmed_date desc;

select * from real_time_confirmed;