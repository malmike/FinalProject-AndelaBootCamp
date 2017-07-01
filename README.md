# FinalProject-AndelaBootCamp
[![Build Status](https://travis-ci.org/malmike/FinalProject-AndelaBootCamp.svg?branch=master)](https://travis-ci.org/malmike/FinalProject-AndelaBootCamp)
[![Coverage Status](https://coveralls.io/repos/github/malmike/FinalProject-AndelaBootCamp/badge.svg?branch=master)](https://coveralls.io/github/malmike/FinalProject-AndelaBootCamp?branch=master)
[![Code Health](https://landscape.io/github/malmike/FinalProject-AndelaBootCamp/master/landscape.svg?style=flat)](https://landscape.io/github/malmike/FinalProject-AndelaBootCamp/master)
[![Code Climate](https://codeclimate.com/github/malmike/FinalProject-AndelaBootCamp/badges/gpa.svg)](https://codeclimate.com/github/malmike/FinalProject-AndelaBootCamp)
[![Issue Count](https://codeclimate.com/github/malmike/FinalProject-AndelaBootCamp/badges/issue_count.svg)](https://codeclimate.com/github/malmike/FinalProject-AndelaBootCamp)

This is the repository for the final project of the Andela Boot Camp

## PROJECT DESCRIPTION

When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. In this exercise you will be required to digitize and randomize a room allocation system for one of Andela Kenya’s facilities called The Dojo.

## CONSTRAINTS

The Dojo has rooms, which can be offices or living spaces. An office can accommodate a maximum of 6 people. A living space can accommodate a maximum of 4 people.

A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not.

This system will be used to automatically allocate spaces to people at random.

## Installation Instructions
- You should have [git](https://git-scm.com/downloads), [python](https://www.python.org/downloads/) with [pip](https://pip.pypa.io/en/stable/installing/) and [virtual env](https://virtualenv.pypa.io/en/stable/installation/) installed on your local machine
- Run your command console for windows or bash console for a linux based system
- Change to the directory where you wish to store it and [clone this repository](https://help.github.com/articles/cloning-a-repository/)
- Change into the created directory and [create a virual environment within the repository using virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Call the folder that contains the settings of the virtual environment .venv
- Start the virtual environment
- You can now start the application by typing in **python main.py start**
- You can then type **help** to access the usage commands for the system.

### Sample Usage Commands
- create_room <room_type> <room_name>...
- add_person <first_name> <last_name> \<position> [\<Y> | \<N>]
- print_room <room_name>
- print_allocations [-o \<filename>]
- print_unallocated [-o \<filename>]
- save_state [--db <sqlite_database>]
- save_state <sqlite_database>





