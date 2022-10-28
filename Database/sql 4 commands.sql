-- order by
select StudentId, Fname as FullName from Student order by studentId asc; 

select StudentId, Fname as FullName from Student order by studentId desc; 

select 
StudentId, Fname as FullName 
from Student 
order by Fname asc, studentId desc;

-- group by
select 
Address, count(StudentId) as TotalStudents
from Student
group by Address;

