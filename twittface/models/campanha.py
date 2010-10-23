# coding: utf-8
#!/usr/bin/env python

from torneira.models.base import Model, Repository
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.databases.mysql import MSBit

class Campanha (Model, Repository):
    __tablename__ = 'tface_campanha'
    
    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String)
    ativo = Column('ativo', MSBit(1), default=0)
    candidata = Column('candidata', MSBit(1), default=0)
    votos = Column("votos", Integer)
    tempo = Column("tempo", Integer)
    inicio = Column("inicio", DateTime)