#!/usr/bin/env python3

import psycopg2

DBNAME = 'news'


def db_connect():
    """
    Creates and returns a connection to the database defined by DBNAME,
    as well as a cursor for the database.
    Returns:
        db, c - a tuple. The first element is a connection to the database.
                The second element is a cursor for the database.
    """
    db = psycopg2.connect("dbname={}".format(DBNAME))
    c = db.cursor()
    return db, c


def execute_query(query):
    """
    execute_query takes an SQL query as a parameter.
    Executes the query and returns the results as a list of tuples.
    args:
    query - an SQL query statement to be executed.

    returns:
    A list of tuples containing the results of the query.
    """
    db, c = db_connect()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_top_articles():
    """Prints out the top 3 articles of all time."""
    query = '''select title, count(*) as views from log, articles
        where path = concat('/article/',articles.slug)
        group by title
        order by views desc limit 3 '''
    results = execute_query(query)
    print("The top 3 most popular articles:")
    for (title, views) in results:
        print('{} -- {} views'.format(title, views))
    print('')


def print_top_authors():
    """Prints a list of authors ranked by article views."""
    query = '''select name, count(path) as views from authors, articles, log
        where authors.id = articles.author
        and path = concat('/article/',articles.slug)
        group by authors.id
        order by views desc '''
    results = execute_query(query)
    print("The most popular authors:")
    for (name, views) in results:
        print('{} -- {} views'.format(name, views))
    print('')


def print_errors_over_one():
    """
    Prints out the days where
    more than 1% of logged access requests were errors."""
    query = '''select to_char(time, 'DD Mon YYYY') as day,
        round(100*sum(case when status='404 NOT FOUND' then 1 else 0 end)
            /count(time), 2) as percentage
        from log group by day
        having sum(case when status='404 NOT FOUND' then 1 else 0 end)
            >= 0.01*count(time)
        order by day '''
    results = execute_query(query)
    print('Days that more than 1% of requests are errors:')
    for (date, percentage) in results:
        print('{} -- {}% errors'.format(date, percentage))


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
