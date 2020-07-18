def filter_urls(books, known):
    """Takes in a dictionary of name urls pairs and filters already archived
    urls.

    :books: dictionary, name:url
    :books: dictionary, name:url, of already archived form
    :returns: cleaned dictionary, name:url

    """
    # For know simply filter the new urls
    books = {name:url for name, url in books.items() if not url in known.values()}
    return books
