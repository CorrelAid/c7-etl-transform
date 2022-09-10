Track [X] Challenge [Y]
================


# Setup

## Dependencies

Create a virtual environment with python, activate and install requirements:

```
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Access data
To access the data for this challenge, you first need to get secrets/passwords.

To get them, proceed as follows:

1. Check the Slack channel for the "secret link" for your challenge
2. We'll share the password to decrypt the message on-site 
3. Click on the link and enter the password to decrypt the message
4. Follow the specific instructions for your data below.

### Supabase/Postgres + Limesurvey

To connect to the Supabase Postgres and Maria DB (Limesurvey) database, you need to store your credentials in an `.env` file which you create.

Copy the content from the decrypted secret link. It should look something like this:

```
# logins for supabase
SUPAB_NAME='postgres'
SUPAB_HOST='your-supabase-url' 
SUPAB_PORT='5432'
SUPAB_USER='postgres'
SUPAB_PASSWORD='your-supabase-pw'
# logins for limesurvey
LIMESURVEY_SSH_IP="102.203.20.10"
LIMESURVEY_SSH_USER="user"
LIMESURVEY_SSH_PASSWORD="password"
LIMESURVEY_SQL_USER="test"
LIMESURVEY_SQL_PASSWORD="password"
```

Now run load.py to get access to the MariaDB.

# Developer information
Just kept here for continuing after the hackathon :)

## Documentation
Documentation of the data transformations and functionality can be found in the project [Wiki](https://github.com/CorrelAid/c7-etl-transform/wiki/Contents).

## Definition of Done

Default Definition of Done can be found
[here](https://github.com/CorrelAid/definition-of-done). Adapt if
needed.

