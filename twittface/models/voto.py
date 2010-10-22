# coding: utf-8
#!/usr/bin/env python

from torneira.models.base import Model, Repository
from sqlalchemy import Column, Integer, String, DateTime

class Voto (Model, Repository):
    __tablename__ = 'tface_voto'
    
    id = Column("id", Integer, primary_key=True)
    user = Column("user", String)
    target = Column("target", String)
    rating = Column("rating", Integer)
    context = Column("context", Integer)
    data = Column("data", DateTime)
