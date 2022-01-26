from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Table, text


from sqlalchemy.orm import relationship


from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import create_engine


from sqlalchemy.orm import sessionmaker



db_string = "postgresql://postgres:root@localhost:5432/AlimConfiance"


db = create_engine(db_string, echo=True)



Session = sessionmaker(db)  


session = Session()

Base = declarative_base()
Base.metadata.create_all(db)



class Activite(Base):

    __tablename__ = 'activite'


    idactivite = Column(Integer, primary_key=True)

    libelle_activite = Column(String(200))

    categorie_frais = Column(Boolean)



class Etablissement(Base):
    __tablename__ = 'etablissement'


    idetablissement = Column(Integer, primary_key=True)

    siret = Column(String(200))

    siren = Column(String(200))

    libelle_etablissement = Column(String(200))

    adresse = Column(String(200))

    code_postal = Column(String(200))

    departement = Column(String(200))

    commune = Column(String(200))

    geores = Column(String(200))

    nb_agrements = Column(Integer)

    commune_norm = Column(String(200))



class MotsCle(Base):
    __tablename__ = 'mots_cles'


    idmotcle = Column(Integer, primary_key=True)

    motcle = Column(String(200))



class Inspection(Base):
    __tablename__ = 'inspection'


    idinspection = Column(Integer, primary_key=True)

    numero_inspection = Column(String(200))

    date_inspection = Column(Date)

    synthese_eval = Column(String(200))

    numero_agrement = Column(String(200))

    synthese_ai = Column(String(200))

    date_synt_ai = Column(Date)

    idetablissement = Column(ForeignKey('etablissement.idetablissement'), nullable=False)

    idactivite = Column(ForeignKey('activite.idactivite'), nullable=False)


    activite = relationship('Activite')

    etablissement = relationship('Etablissement')

    mots_cles = relationship('MotsCle', secondary='motcle_inspection')



t_motcle_inspection = Table(

    'motcle_inspection', Base.metadata,

    Column('idinspection', ForeignKey('inspection.idinspection'), primary_key=True, nullable=False),

    Column('idmotcle', ForeignKey('mots_cles.idmotcle'), primary_key=True, nullable=False)
)