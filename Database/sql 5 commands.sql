-- Inner join

select
StudentId, Fname as FirstName, Student.StudentId as Stu_StudentId, Computer.StudentId as Com_StudentId, Model
from Student inner join Computer on Student.StudentId = Computer.StudentId;
