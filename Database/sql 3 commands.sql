-- Numeric Functions
-- absolute function
select abs(-12);

select * from Student;

-- avg function
select avg(StudentId) as AveragePrice from Student;

-- count function
select count(StudentId) As NumberOfStudents from Student; 

-- sum function
select sum(StudentId) as TotalPrice from Student;

-- Character Function

-- Concat function
select concat("Vinay ", " Kumar ", " Kuresi") as FullName;  

-- insert function
select insert("Garuda Careers", 1, 6, "KVK"); 

-- Lower case
select LCASE("GARUDA CAREERS"); 

-- replace function
select replace("Garuda Careers", "Garuda", "KVK"); 

-- position
select position("u" in "Garuda Careers") as MatchPosition;

-- reverse function
select reverse("1ABCBA2");

-- Date function

-- addDate function
select adddate("2022-10-28", interval 5 day); 

-- addTime 
select addtime("2022-10-28 06:41:30", "30");

-- curDate
select curdate(); 

-- current time
select current_time(); 

-- current timestamp 
select current_timestamp();

-- date
select date("2022-10-28 06:41:30"); 

-- Conversion function

-- convert function
select convert("2022-10-28", date);

select convert(200, char);

select convert(3-5, unsigned);


