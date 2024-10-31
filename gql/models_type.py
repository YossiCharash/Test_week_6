import graphene as g
from graphene_sqlalchemy import SQLAlchemyObjectType
from db.models.missions import Missions


class MissionModel(SQLAlchemyObjectType):
    class Meta:
        model = Missions
        interfaces = (g.relay.Node,)



