# Log Analysis
---
log_analysis is written in python which connects to a news database and make one query each to answer the following three questions:

 What are the most popular three articles of all time?

 Who are the most popular article authors of all time?

 On which days did more than 1% of requests lead to errors?


## Environment Setup
---
Python 3.X

'psycopg2' package installed on python3

[download the news database and unzip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Virtual box and Vagrant installed

[download the VM configuration files and unzip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)

## Run the Program
---
Make sure you put the `log_analysis.py` and `newsdata.sql` under **FSND-Virtual-Machine/vagrant/**

1. Use `cd` to change directory to the **FSND-Virtual-Machine/vagrant/**
2. Start up the vagrant virtual machine by running 'vagrant up'
3. `vagrant ssh` to log in
4. `cd /vagrant` to access the shared folder
5. If this is the first time you run the program, you need to build the database by `psql -d news -f newsdata.sql`
6. Run the python script by either `python3 reporting_tool.py` or `python reporting_tool.py` depend on your setup
