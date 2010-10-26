# coding: utf-8
#!/usr/bin/env python

from torneira.models.base import Model, Repository
from sqlalchemy import Column, Integer, String, DateTime

class Usuario (Model, Repository):
    __tablename__ = 'tface_usuario'
    
    id = Column("id", Integer, primary_key=True)
    id_twitter = Column("id_twitter", String)
    image_url = Column("image_url", String)
    login = Column("login", String)
