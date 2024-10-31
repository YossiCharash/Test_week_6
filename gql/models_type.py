import graphene as g
from graphene_sqlalchemy import SQLAlchemyObjectType

from db.models.country import Country
from db.models.target import Target, Missions, City


class MissionModel(g.ObjectType):
    class Meta:
        model = Missions
        interfaces = (g.relay.Node,)


class TargetModel(g.ObjectType):
    class Meta:
        model = Target
        interfaces = (g.relay.Node,)

class CityModel(g.ObjectType):
    class Meta:
        model = City
        interfaces = (g.relay.Node,)


class CountryModel(g.ObjectType):
    class Meta:
        model = Country
        interfaces = (g.relay.Node,)


class TargetType(g.ObjectType):
    class Meta:
        model = Target
        interfaces = (g.relay.Node,)




