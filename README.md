For information on how to use this project template, check out the [wiki](https://github.com/lionheart/django-template/wiki/Django-1.9).

Let's Get Started
=================

## Python 3.5
At this point you're probably just getting started. You may not have a couple of things that you'll need to have, but by the time you finish with this getting started guide, 
you should be good. First we'll have to install python 3.5.2
https://www.python.org/downloads/
Here you'll find your download whether on a MAC or Windows machine

## IDE
Now you need an IDE and PyCharm is here to help.
https://www.jetbrains.com/pycharm/
You can either download the IDE for Professional Developers or Community. Using an fau.edu email will get you a free copy of the Professional and
I definitely recommend that over the Community editions just because why not.

## Text Editor
You can also use any one of your favorite text ediors be it NotePad++, SublimeText, Brackets, Atom or any other one you can think of, it's mainly
up to your personal preference.

## GitBash
GitBash is something else you will need if you don't have already. It is a Windows terminal with Bash commands and git integration. It's an awesome
tool and python is mainly CLI based so it will be a necessity.

## pip
pip is a package management system which is used to install and manage software packages written in Python. The Python Package Index (PyPI). By default it comes installed with Python 3.4+

```Usage:
  pip  [options]

Commands:
  install       Install packages.
  uninstall     Uninstall packages.
  freeze        Output installed packages in requirements format.
  list          List installed packages.
  show          Show information about installed packages.
  search        Search PyPI for packages.
  zip           Zip individual packages.
  unzip         Unzip individual packages.
  bundle        Create pybundles.
  help          Show help for commands.
  ```

most installations of code you do will be done using pip. There are times where an issues may arise and you must manually download and install these module packages.

For windows this website provides alot of the binaries for different packages-
http://www.lfd.uci.edu/~gohlke/pythonlibs/

## virtualenv
Virtual environments are an awesome and integral tool for python. They function keep the dependencies required by different projects in separate places, by creating virtual Python environments for them.  It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

Virtual Environments are best explained on The Hitchhiker's Guide to Python-
http://docs.python-guide.org/en/latest/dev/virtualenvs/


Installation
============

You've cloned the repo or started a new project with the startproject command. Here's how you actually get started developing. These steps assume you have pip installed. Please also ensure you are using GitBash to do all this stuff, it makes it a bit

1. Install virtualenv.

        $ pip install virtualenv

2. Then, start a virtualenv in the project directory.

        $ virtualenv venv
        $ source venv/scripts/activate # if scripts does not exist, it is bin

3. Install the project requirements.

        (ProjectName) $ pip install -r requirements.txt
        # wait for a couple of minutes, hopefully nothing goes wrong!

If you get an error regarding 'lxml' refer to this link to get around the errors
http://stackoverflow.com/questions/33785755/getting-could-not-find-function-xmlcheckversion-in-library-libxml2-is-libxml2

## Before Proceeding
Please create a new file in your Project Direcory called
`.env`
Do this by using the bash command
`touch .env`
From here, open it up with any text editor, and copy over the content from `env.example`
and fill in what the necessary information.

4. Link the local project settings to local_settings.py. (This creates a reference to whatever settings module you are using whether local.py or production.py)

        (ProjectName) $ ln -s conf/settings/local.py local_settings.py

5. Create your local database. Make sure you run the [steps below](#postgresql-installation) if you haven't already installed PostgreSQL.

        $ psql
        postgres# CREATE ROLE ProjectName_local WITH LOGIN ENCRYPTED PASSWORD 'ProjectName_local';
        postgres# CREATE DATABASE ProjectName_local WITH OWNER ProjectName_local;

    **Note**: If you get a `psql: FATAL:  role "YOUR_USERNAME" does not exist` error, just do the following to save yourself from having to write `--user postgres` every time you want to run `psql`. If, say, your username is `dan` on your development machine, you'd run the following:

        $ createuser -s dan # Create a superuser named `dan`
        $ createdb -O dan dan # Create a database for this user to log into.

    After doing this, re-run the psql commands in step 5.

6. Make manage.py executable and run migrations.

        (ProjectName) $ chmod +x manage.py
        (ProjectName) $ ./manage.py migrate

7. Set up the Git hooks.

        $ git_config/configure.sh

8. Start the local development server.

        (ProjectName) $ ./manage.py runserver
        Performing system checks...

        October 27th, 2016
        Django version 1.9.9, using settings 'settings'
        Starting development server at http://127.0.0.1:8080/
        Quit the server with CONTROL-BREAK.

Map "local.Residency.com" to 127.0.0.1 using DNS. If you haven't yet registered a domain, add the following line to your `/etc/hosts` file.

    127.0.0.1 local.ProjectName.com

After you've done that, open your browser and navigate to "[local.ProjectName.com](http://local.ProjectName.com)". Your project is now running!

PostgreSQL Installation
-----------------------

If you're on a Mac and have [Homebrew](https://github.com/homebrew/homebrew) installed, we'll keep it simple.

    brew install postgresql

If you're in the mood for a longer read or have run into issues, here's a good [article](https://www.codefellows.org/blog/three-battle-tested-ways-to-install-postgresql) on how to install PostgreSQL on your system (covers Mac OS X, Windows, and Ubuntu).
