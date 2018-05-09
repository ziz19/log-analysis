#!/usr/bin/python3

import psycopg2


db = psycopg2.connect("dbname=news")  # connect to the news database
c = db.cursor()

# Get the most popular three articles of all time
c.execute('''select title, count(*) as counts from log, articles
    where path like concat('%',articles.slug,'%')
    group by title
    order by counts desc limit 3 ''')  # select the top three frequently visited article paths
results = c.fetchall()
print("The top 3 most popular articles:")
for (title, views) in results:   # for each article path
    print('"%s" -- %d views' % (title, views))  # print out its parsed article name and views
print('')

# Get the most popular article authors of all time
c. execute('''select name, count(path) as counts from authors, articles, log
    where authors.id = articles.author
    and path like concat('%',articles.slug,'%')
    group by authors.id
    order by counts desc ''')   # sort author name descendingly by the views of articles
results = c.fetchall()
print("The most popular authors:")
for (name, views) in results:   # for each article path
    print('"%s" -- %d views' % (name, views))  # print out its parsed article name and views
print('')

# Get days when more than 1% of requests lead to errors
c.execute('''select to_char(time, 'DD Mon YYYY') as day,
    sum(case when status='404 NOT FOUND' then 1 else 0 end),
    count(time) from log group by day
    having sum(case when status='404 NOT FOUND' then 1 else 0 end) >= 0.01*count(time)
    order by day ''')
results = c.fetchall()
print('Days that more than 1% of requests are errors:')
for (date, errors_counts, overall_counts) in results:
    print('%s -- %.1f %% errors' % (date, 100*errors_counts/overall_counts))

db.close()  # close the database
