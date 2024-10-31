from graphene import ObjectType, Int, Field, Schema

from db.database import db_session
from db.models.missions import Missions
from gql.models_type import MissionModel


class Query(ObjectType):
    mission_by_id = Field(MissionModel, mission_id=Int(required=True))



    def resolve_mission_by_id(self, info, mission_id):
        return db_session.query(Missions).get(mission_id)



schema = Schema(query=Query)