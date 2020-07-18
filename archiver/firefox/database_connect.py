import os
import sqlite3

# execute a query on sqlite cursor
def execute_query(cursor, query):
    try:
        cursor.execute(query)
    except Exception as error:
        print(str(error) + "\n " + query)
# get bookmarks from firefox sqlite database file and print all
def get_bookmarks(cursor):
    bookmarks_query = """select url, moz_places.title, rev_host, frecency,
    last_visit_date from moz_places  join  \
    moz_bookmarks on moz_bookmarks.fk=moz_places.id where visit_count>0
    and moz_places.url  like 'http%'
    order by dateAdded desc;"""
    books = {}
    execute_query(cursor, bookmarks_query)
    for row in cursor:
        link = row[0]
        title = row[1]
        books[title] = link
    return books

def perform_query(path):
    """Perform a query to the bookmarks.

    :path: path to where the firefox profile is stored.
    :returns: dictionary, name of resource and url

    """
    bookmarks_path = path
    # get firefox profile
    profiles = [i for i in os.listdir(bookmarks_path) if i.endswith('.default')]
    # get sqlite database of firefox bookmarks
    sqlite_path = bookmarks_path+ profiles[0]+'/places.sqlite'
    os.system(f'cp {sqlite_path} /tmp/')
    sqlite_path = '/tmp/places.sqlite'

    if os.path.exists(sqlite_path):
        firefox_connection = sqlite3.connect(sqlite_path)
    cursor = firefox_connection.cursor()
    books = get_bookmarks(cursor)
    cursor.close()
    return books
