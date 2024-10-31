from flask import Flask
from flask_graphql import GraphQLView
from gql.query import schema
from db.database import connection_url


app = Flask(__name__)
app.debug = True

app.config["SQLALCHEMY_DATABASE_URI"] = connection_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False




app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)



# if __name__ == "__main__":
#     app.run(host='0.0.0.0',
#             # debug=True, #todo: maybe remove because we declared before.
#             port=5001)

if __name__ == '__main__':
    app.run()