from .base import Base, Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import orm
from sqlalchemy.types import Enum


class Entity_Type(Model, Base):
    name = Column(String(50))

    _printed_keys = [
        'name',
        'id'
    ]


class Element_Type(Model, Base):
    name = Column(String(50))

    _printed_keys = [
        'name',
        'id'
    ]


class Skill(Model, Base):
    name = Column(String(50))
    element_id = Column(Integer, ForeignKey('element_type.id'))
    element = orm.relationship('Element_Type',
                               cascade='all, delete')
    target_type = Column(Enum(
        'single_enemy', 'single_ally', 'all_enemies', 'all_allies',
        name='target_types'))
    cost = Column(Integer)
    cost_type = Column(Enum('hp', 'sp', name='cost_type'))


class Repel_Element(Model, Base):
    element_id = Column(Integer, ForeignKey('element_type.id'))
    entity_id = Column(Integer, ForeignKey('entity.id'))
    elements = orm.relationship('Element_Type',
                                cascade='all, delete')

    _printed_relations = [
        'elements'
    ]


class Resist_Element(Model, Base):
    element_id = Column(Integer, ForeignKey('element_type.id'))
    entity_id = Column(Integer, ForeignKey('entity.id'))
    elements = orm.relationship('Element_Type', backref='Repels',
                                cascade='all, delete')

    _printed_relations = [
        'elements'
    ]


class Absorb_Element(Model, Base):
    element_id = Column(Integer, ForeignKey('element_type.id'))
    entity_id = Column(Integer, ForeignKey('entity.id'))
    elements = orm.relationship('Element_Type',
                                cascade='all, delete')

    _printed_relations = [
        'elements'
    ]


class Weakness_Element(Model, Base):
    element_id = Column(Integer, ForeignKey('element_type.id'))
    entity_id = Column(Integer, ForeignKey('entity.id'))
    elements = orm.relationship('Element_Type',
                                cascade='all, delete')

    _printed_relations = [
        'elements'
    ]


class Void_Element(Model, Base):
    element_id = Column(Integer, ForeignKey('element_type.id'))
    entity_id = Column(Integer, ForeignKey('entity.id'))
    elements = orm.relationship('Element_Type',
                                cascade='all, delete')

    _printed_relations = [
        'elements'
    ]


class Entity_Skills(Model, Base):
    entity_id = Column(Integer, ForeignKey('entity.id'))
    skill_id = Column(Integer, ForeignKey('skill.id'))
    skills = orm.relationship('Skill',
                              cascade='all, delete')


class Entity(Model, Base):
    name = Column(String(50))
    level = Column(Integer)
    strength = Column(Integer)
    magic = Column(Integer)
    endurance = Column(Integer)
    agility = Column(Integer)
    luck = Column(Integer)
    arcana_id = Column(ForeignKey('entity_type.id'), nullable=False)
    arcana = orm.relationship('Entity_Type', backref='entities',
                              cascade='all, delete')
    weaknesses = orm.relationship('Weakness_Element',
                                  cascade='all, delete')
    resists = orm.relationship('Resist_Element',
                               cascade='all, delete')
    absorbs = orm.relationship('Absorb_Element',
                               cascade='all, delete')
    voids = orm.relationship('Void_Element',
                             cascade='all, delete')
    repels = orm.relationship('Repel_Element',
                              cascade='all, delete')
    skills = orm.relationship('Entity_Skills',
                              cascade='all, delete')

    _printed_keys = [
        'id',
        'name',
        'level',
        'strength',
        'magic',
        'endurance',
        'agility',
        'luck'
    ]

    _printed_relations = [
        'arcana',
        'weaknesses',
        'resists',
        'absorbs',
        'voids',
        'repels',
    ]
