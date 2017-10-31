Onion Web Crawler

Description:

The simple web crawler written in Python 3, connects to Tor browser,
then accesses URL http://nzxj65x32vh2fkhk.onion/all and
stores the most recent "pastes" in a structured data format. The pastes
are stored in the sqllite3 database that contains the table 'onion'
and the following columns:

Author
Title
Content
Date


The web crawler crawls the site every 4 hours, and updates the database with
the new pastes.

In the crawler_lists.py file we are establishing the connection, then
crawl the site and create the lists. In the crawler_tests.py, we
create the new database that contains the onion table with the respective
columns, then insert the data into the columns. After that, we use the
basic 'select * from onion' query to make sure the data was inserted successfully.


Environment:

The following libraries need to be installed in order for the project to run:

requests
bs4
apscheduler

Use 'pip install' in order to install the required dependencies.

The Tor browser runs on port 9150 so we are defining proxies like so:

proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}









