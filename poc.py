import wget as w
from decouple import config
from archiver.firefox import database_connect
from archiver.filter import pre_filter
from archiver.archive import archive

#######################################################################
#                          Proof of concept                           #
#######################################################################

# First get links from firefox bookmarks
books = database_connect.perform_query(config('firefox_profile'))

# Deduplicate previous versions
known = archive.get_archived_urls(config)
books = pre_filter.filter_urls(books, known)

# Then download them and place them in the archive
added = archive.archive_urls(books, config)
print(added)


# Perform cleanup, remember what was saved, etc.

