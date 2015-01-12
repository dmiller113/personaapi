from .base import Base, Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import orm
from sqlalchemy.types import Enum


class Entity_Type(Model, Base):
    name = Column(String(50))
    entities = orm.relationship('Entity')


class Element_Type(Model, Base):
    name = Column(String(50))


class Skill(Model, Base):
    name = Column(String(50))
    element_id = Column(Integer, ForeignKey('element_type.id'))
    element = orm.relationship('Element_Type')
    target_type = Column(Enum(
        'single_enemy', 'single_ally', 'all_enemies', 'all_allies',
        name='target_types'))
    cost = Column(Integer)
    cost_type = Column(Enum('hp', 'sp', name='cost_type'))


class Repel_Element(Model, Base):
    element_id = Column(Integer, ForeignKey('element_type.id'))
    entity_id = Column(Integer, ForeignKey('entity.id'))
    elements = orm.relationship('Element_Type')


class Resist_Element(Model, Base):
    element_id = Column(Integer, ForeignKey('element_type.id'))
    entity_id = Column(Integer, ForeignKey('entity.id'))
    elements = orm.relationship('Element_Type')


class Weakness_Element(Model, Base):
    element_id = Column(Integer, ForeignKey('element_type.id'))
    entity_id = Column(Integer, ForeignKey('entity.id'))
    elements = orm.relationship('Element_Type')


class Void_Element(Model, Base):
    element_id = Column(Integer, ForeignKey('element_type.id'))
    entity_id = Column(Integer, ForeignKey('entity.id'))
    elements = orm.relationship('Element_Type')


class Entity_Skills(Model, Base):
    entity_id = Column(Integer, ForeignKey('entity.id'))
    skill_id = Column(Integer, ForeignKey('skill.id'))
    elements = orm.relationship('Skill')


class Entity(Model, Base):
    name = Column(String(50))
    level = Column(Integer)
    strength = Column(Integer)
    magic = Column(Integer)
    endurance = Column(Integer)
    agility = Column(Integer)
    luck = Column(Integer)
    arcana = Column(ForeignKey('entity_type.id'), nullable=False)
    weaknesses = orm.relationship('Weakness_Element')
    resists = orm.relationship('Resist_Element')
    voids = orm.relationship('Void_Element')
    repels = orm.relationship('Repel_Element')
    skills = orm.relationship('Entity_Skills')
