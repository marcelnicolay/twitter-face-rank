# coding: utf-8
#!/usr/bin/env python

from torneira.models.base import Model, Repository
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.databases.mysql import MSBit
from torneira.core.meta import TorneiraSession
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime

class CampanhaRepository(Repository):
    
    def ativaCampanha(self, candidatas=[]):
        session = TorneiraSession()
        
        try:
            session.begin()
            campanha_ativa = session.query(Campanha).filter(Campanha.ativo==True).one()
            campanha_ativa.ativo = False
            campanha_ativa.save()
            
            campanha = session.query(Campanha).filter(Campanha.candidata==True).order_by(Campanha.votos.desc()).first()
            campanha.ativo = True
            campanha.inicio = datetime.now()
            campanha.save()
            
            session.execute("UPDATE tface_campanha SET candidata = 0 ")
            
            for candidata in candidatas:
                c = Campanha()
                c.nome = candidata
                c.candidata = True
                c.save()
                
            session.commit()
        except NoResultFound:
            pass
        except Exception, e:
            session.rollback()
            raise(e)
            
    def getAtiva(self):
        session = TorneiraSession()
        campanha_ativa = session.query(Campanha).filter(Campanha.ativo==True).one()
        return campanha_ativa

    def listaCandidatas(self):
        session = TorneiraSession()
        result = session.query(Campanha).filter(Campanha.candidata==True).all()
        return [row.as_dict() for row in result]

    def votar(self, id):
        session = TorneiraSession()
        session.execute("UPDATE tface_campanha SET votos = votos + 1 where id = %s" % id)
        
    def as_dict(self):
        return {"id": self.id,
                "nome": self.nome,
                "ativo": self.ativo,
                "candidata": self.candidata,
                "votos": self.votos,
                "tempo": self.tempo,
                "inicio": self.inicio}
    
class Campanha (Model, CampanhaRepository):
    __tablename__ = 'tface_campanha'
    
    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String)
    ativo = Column('ativo', MSBit(1), default=0)
    candidata = Column('candidata', MSBit(1), default=0)
    votos = Column("votos", Integer)
    tempo = Column("tempo", Integer, default=60)
    inicio = Column("inicio", DateTime)