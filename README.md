# Logs Analysis Project
### submitted by James Chychota

This is project three of the Udacity Full Stack Web Developer Nanodegree.

## Project Overview
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Resources

* [Udacity - Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004/) - Udacity information about the Nanodegree program.
* [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) - A list of dos and don'ts for Python programs.
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) - Coding conventions for Python code.
* [Udacity - Writing READMEs](https://www.udacity.com/course/writing-readmes--ud777) - Free Udacity course on building well-structured READMEs.

## Getting Started

Run using python2.7

1. What are the most popular three articles of all time?

```sh
$ python pop_articals.py
"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views
$
```
create view command:
```sh
create view gettopthree as select a.title, count(*) as views from articles a join log l on l.path like '%' || a.slug group by a.title order by views desc limit 3;
```

2. Who are the most popular article authors of all time?
```sh
$ python pop_authors.py
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views
$
```
create view command:
```sh
create view getauthors as select b.name, count(*) as views from articles a join authors b on a.author = b.id join log c on c.path like '%' || a.slug group by b.name order by views desc;
```

3. On which days did more than 1% of requests lead to errors?
```sh
$ python request_errors.py
July 17,2016 - 2.3% errors
$
```
create view command:
```sh
create view geterrordays as select to_char(a.adate, 'FMMonth DD,YYYY'), round(a.num * 100.0 / (b.total * 1.0),1) as percenterr from (select date(time) as adate, count(*) as num from log where status != '200 OK' group by adate) as a join (select date(time) as bdate, count(*) as total from log group by bdate) as b on a.adate = b.bdate where round(a.num * 100.0 / (b.total * 1.0),1) > 1.0;
```


