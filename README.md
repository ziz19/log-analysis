# Log Analysis
---
This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

 What are the most popular three articles of all time?

 Who are the most popular article authors of all time?

 On which days did more than 1% of requests lead to errors?


## Environment Setup
---
Python 3.X

'psycopg2' package installed on python3

Links for database: [https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip]

Virtual box and Vagrant installed

Vagrant configuration file already in the repository

## Run the Program
---
Make sure you put the `log_analysis.py` and `newsdata.sql` under **FSND-Virtual-Machine/vagrant/**

1. Use `cd` to change directory to the **FSND-Virtual-Machine/vagrant/**
2. Start up the vagrant virtual machine by running 'vagrant up'. If this is the first time you run vagrant, it will take sometime to download the image.
3. `vagrant ssh` to log in
4. `cd /vagrant/` to access the shared folder
5. If this is the first time you run the program, you need to build the database by `psql -d news -f newsdata.sql`
6. Run the python script by either `python3 reporting_tool.py` or `python reporting_tool.py` depend on your setup
