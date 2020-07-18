# archiver

Simple web archiver bot.

## Idea

One of the problems with the web is that information gets lost easily.
There are numerous websites dedicated to preserving the knowledge such as the [wayback machine] (http://web.archive.org/).
But one is still dependent on the fact that those websites are always online and won't shut down.
In part inspired by a wonderful [post on "link rot" and archiving websites by gwern](https://www.gwern.net/Archiving-URLs),
I wanted to write a simple bot capable of archiving the webistes that I have bookmarked.
Basically it pulls the bookmarked sites from my firefox profile and uses wget to download them all.
The script currently is able to recognize only new additions to the bookmark list and thus only uses up minimal resources,
making it ideally suited to be run as a cron job every now and then, archiving the posts that you want to save from being gone.

## Usage
To use this script you need to specify a `settings.ini` file in the working directory.
The settings file specifies the logging level as well as the directory used to save the data and the place where your 
firefox profile directory is located at, i.e.:
```ini
[settings]
logging_level=DEBUG
firefox_profile=<path_to_firefox_profile>
archive_folder=./data/archive
```
Make sure that you replace `<path_to_firefox_profile>` with the path to your firefox profile, e.g. for unix based systems this will be
under `/home/<user>/.mozilla/firefox/`, where `<user>` is of course your username.
Then you will be able to simply run `python3 poc.py` and the bot will do its thing, archiving all the websites in a rudimentary format
into the directory specified under `archive_folder`.
