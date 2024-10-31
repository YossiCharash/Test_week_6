from datetime import datetime

from graphene import ObjectType, Int, Field, Schema, List, String, Date
from db.database import db_session
from db.models.country import Country
from db.models.target import Target, Missions, City
from gql.models_type import MissionModel


class Query(ObjectType):
    mission_by_id = Field(MissionModel, mission_id=Int(required=True))
    missions_by_date = List(MissionModel, start_date=String(required=True),end_date=String(required=True))
    missions_by_country = List(MissionModel, country=String(required=True))
    mission_by_target_industry = List(MissionModel, target_industry=String(required=True))



    def resolve_mission_by_id(self, info, mission_id):
        return db_session.query(Missions).get(mission_id)

    def resolve_missions_by_date(self, info, start_date, end_date):
        start = datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.strptime(end_date, '%Y-%m-%d').date()
        return db_session.query(Missions).filter(
            Missions.mission_date.between(start, end)
        ).all()



    def resolve_mission_by_country(self, info, country):
        return (db_session.query(Missions)
                .join(Target)
                .join(City, City.city_id == Target.city_id)
                .join(Country,Country.country_id == City.country_id)
                .filter(
                Target.city.country.name == country
                ).all())


    def resolve_mission_by_target_industry(self, info, target_industry):
        return (db_session.query(Missions)
                .join(Target,Target.mission_id == Missions.mission_id)
                .filter(Target.target_industry == target_industry).all())

schema = Schema(query=Query)