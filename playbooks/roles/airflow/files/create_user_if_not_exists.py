#!/usr/bin/python3

import sys
import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser


def has_user(session, username):
    users = session.query(models.User)
    with_name = users.filter(models.User.username == username)
    return with_name.count() > 0


username = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

session = settings.Session()

if not has_user(session, username):
    new_user = PasswordUser(models.User())
    new_user.username = username
    new_user.email = email
    new_user.password = password

    session.add(new_user)
    session.commit()

    print('user created')

session.close()

