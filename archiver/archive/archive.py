import json
import os
import wget
import logging

def get_list_dir(config):
    """Get the path to the list directory.
    """
    return config('archive_folder')+'url_list.json'

def get_archived_urls(config):
    """Get the list of archived urls, so that one does not download them
    for the n-th time.

    :returns: dictionary of already archived urls, of the form name:url
    """
    list_dir = get_list_dir(config)

    # If list is not yet initialized, create it
    if not os.path.exists(list_dir):
        with open(list_dir, 'w') as f:
            json.dump({}, f)

    # Next open it, and return contents
    with open(list_dir) as f:
        return json.load(f)

def save_content(name, url, config):
    """Method saving the content under url, giving it the name of
    name.

    This method changes the working directory to the archive!

    :name: name of the resource
    :url: url of the resource
    :returns: archive folder that resource can be found under

    """
    logging.info(f'Attempting to save: {url} for {name}')
    if name == '' or name == None: # Sometimes content is not named, then use url
        name = url
    save_name = name.replace(' ', '')
    save_name = name.replace('/', '')
    save_path = os.path.join(f"{config('archive_folder')}", f"{save_name}")
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    os.chdir(save_path)

    logging.info(f'The savepath is {save_path}/{save_name}.html')
    # Perform the actual download
    os.system(f"""wget  --unlink --continue --page-requisites --timestamping {url}""")
    return save_path

def archive_urls(books, config):
    """Archive the content in the web as given by the dictionary 
    books.

    :books: dict = {name:url} of to-be-saved-content
    :config: config, specifying the place to store the content
    :returns: dict of successfully archived files, with added path
    """
    saved = {}

    # Remember the working directory to jump back to it, every time a
    # download is done.
    wdir = os.getcwd()
    for name, url in books.items():
        save_path = save_content(name, url, config)
        saved[name] = (url, save_path)
        os.chdir(wdir) # change working directory back.
    return saved

def save_archived_urls(added, config):
    """Save the archived urls.

    :added: dictionary of name and urls that were saved this round
    :config: config info

    """
    list_dir = get_list_dir(config)
    # First read what we had already in the archive:
    with open(list_dir) as f:
        cur_add = json.load(f)
        for n, v in cur_add.items():
            added[n] = v

    # Then save the dictionary to file
    with open(list_dir, 'w') as f:
        json.dump(added, f)
