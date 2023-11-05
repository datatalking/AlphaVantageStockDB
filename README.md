# AlphaVantageStockDB
A simple database to hold stock price data from [AlphaVantage](http://www.alphavantage.co), along with some Python-based control scripts to seed/update the price data.

## Depricated
The codebase is out of date reference [alpha_vantage](https://github.com/RomelTorres/alpha_vantage)


## Some assumptions:
* You have MySQL/MariaDB server installed and running, you have login credentials, and you can create/edit databases.
* You have an AlphaVantage API key.
* You have Python 3.5+ installed, with the following modules installed: Pandas, Numpy, PyMySQL, PyYAML.
* Works in bash-like terminal environments (.sh on Linux, OSX) or Windows (.bat).

This codebase is a work in progress, though functional in current form. There is basic support for pulling intraday data from AlphaVantage and storing it (and appending new data upon subsquent updates), but notice the format of the intraday data differs from the daily data (e.g. no adjusted price/split coefficient/divident amount columns, which will be included as NaN/None when inserting, so that the format of the databases can be consistent).

When identifying tickers, we also provide a datasource for each (where the security symbol is the key of a dictionary, and the datasource is the value). This format allows for addition of new securities from new datasources, if/when any are identified (which will require coding of price-grabbing functions specific to those providers).

The creds_template.yaml (in the code_python folder) should be renamed creds.yaml and then populated with the credentials required to access each database (username, password) and each datasource (website, API key). This file is parsed by the Python update script when seeding/updating data. It is populated with dummy values here on GitHub.

There are several supporting functions included that call SQL stored functions/views/procedures. These exist to feed some basic reporting features into a GUI frontend to the updater that I will include at some point as I iron out its many quirks. Arguably it is not useful to add/delete symbols from the database on an ad-hoc basis. I may opt to simply delete these functions or move them to a separate module when the GUI eventually arrives.

Installation 5 Steps:
1. Clone the repo ([click here if not installed](https://www.freecodecamp.org/news/setup-git-on-mac/)) - go to your
 terminal and enter 'git clone https://github.com/justinclarkhome/AlphaVantageStockDB'
1. Load your ide or from terminal 'cd repopath' and run create_daily.sh and create_intraday.sh (the scripts will prompt
 you to enter
 your db
 username/password).
1. Enter your database/API credentials in /code_python/creds_template.yaml and rename the file creds.yaml.
1. In /code_python, run "python updater.py --daily --intraday" to seed the databases.

Update:
* There's now a simple Jupyter notebook in the /code_python directory with some examples of using the database in Python/Pandas.
