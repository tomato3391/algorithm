# X city built a new stadium, each day many people visit it and the stats are saved as these columns: id, visit_date, people

# Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).

select * from stadium where (id in (select id from stadium where people >= 100) and id+1 in (select id from stadium where people >= 100) and id+2 in (select id from stadium where people >= 100)) or (id in (select id from stadium where people >= 100) and id-1 in (select id from stadium where people >= 100) and id+1 in (select id from stadium where people >= 100)) or (id in (select id from stadium where people >= 100) and id-1 in (select id from stadium where people >= 100) and id-2 in (select id from stadium where people >= 100))
