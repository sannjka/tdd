Provisioning a new site
=======================

## Required pachages:

* nginx
* Python 3.8
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python3.8 python3.8-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g. staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g. staging.my-domain.com
* replace SEKRIT with email password
* replace EMAILADDRESS with email address

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
