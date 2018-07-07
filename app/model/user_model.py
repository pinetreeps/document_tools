# _*_ coding:utf-8 _*_

from flask_login import UserMixin


# define profile.json constant, the file is used to
#  save user name and password_hash

class User(UserMixin):
    def __init__(self, uid=None, uname=None, usergroup=None):
        self.uid = uid
        self.uname = uname
        self.usergroup = usergroup

    def to_dict(self):
        return self.__dict__

    def get_id(self):
        return self.uid
