import crawler_lists
import sqlite3
from sqlite3 import Error
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

db_file = 'db_file'
authors, titles, content, dates = crawler_lists.create_multiple_lists()


def db_operations():
    try:
        db = sqlite3.connect(db_file)
        cursor = db.cursor()
        cursor.execute('''DROP TABLE IF EXISTS onion''')

        cursor.execute('''CREATE TABLE onion(author TEXT,title TEXT,
                       content TEXT, date DATETIME )''')

        print("Database created successfully")

        for a, b, c, d in zip(authors, titles, content, dates):
            cursor.execute("INSERT INTO onion"
                           "(author, title, content, date)"
                           "VALUES(?,?,?,?)", (a, b, c, d,))

        db.commit()

        cursor.execute('''SELECT * FROM onion''')
        for row in cursor:
            print(row)

        db.close()

    except Error as e:
        print(e)


@sched.scheduled_job('interval', hours=4)
def timed_job():
    db_operations()
    print('The web crawler will crawl the site very 4 hours.')


def main():
    sched.start()

if __name__ == "__main__":
    main()
