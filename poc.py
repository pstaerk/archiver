import wget as w
from decouple import config
from archiver.firefox import database_connect
from archiver.filter import pre_filter
from archiver.archive import archive
import logging

#######################################################################
#                          Proof of concept                           #
#######################################################################
# Logging settings:
logging.basicConfig(level=config('logging_level')) 

# First get links from firefox bookmarks
books = database_connect.perform_query(config('firefox_profile'))

# Deduplicate previous versions
known = archive.get_archived_urls(config)
books = pre_filter.filter_urls(books, known)

# Then download them and place them in the archive
added = archive.archive_urls(books, config)

# Perform cleanup, remember what was saved, etc.
archive.save_archived_urls(added, config)
