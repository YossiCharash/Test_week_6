from datetime import datetime

from graphene import ObjectType, Int, Field, Schema, List, String, Date
from db.database import db_session
from db.models.missions import Missions
from db.models.target import Target
from gql.models_type import MissionModel


class Query(ObjectType):
    mission_by_id = Field(MissionModel, mission_id=Int(required=True))
    missions_by_date = List(MissionModel, start_date=String(required=True),end_date=String(required=True))
    # missions_by_country = List(MissionModel, country=String(required=True))



    def resolve_mission_by_id(self, info, mission_id):
        return db_session.query(Missions).get(mission_id)

    def resolve_missions_by_date(self, info, start_date, end_date):
        start = datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.strptime(end_date, '%Y-%m-%d').date()
        return db_session.query(Missions).filter(
            Missions.mission_date.between(start, end)
        ).all()



    # def resolve_mission_by_country(self, info, country):
    #     return db_session.query(Missions).filter(
    #         Target.city.country.name == country
    #     ).all()

schema = Schema(query=Query)