## Example CrowdFunding project.


1. advert list
2. company list
3. advert moderation
4. filtering by locations

Not implemented apps:

- donations (payments/resources)
- roles and participants
- dashboard module
- user room

### Project requirements
- Python 3.5
- Django 1.11.5
- Postgres


### Quick start
- Create local settings file:

    touch src/local_setting.py
    
- Override default config if need

#### Create virtualenv and install packages:
    make venv

#### Create superuser:
    make user

#### Loadi fixtures:
    make fixtures

#### Migrations:
    make migrate

#### Rum development server on `8000` port:
    make server
