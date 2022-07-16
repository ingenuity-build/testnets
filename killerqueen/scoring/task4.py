from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://data.killerqueen-1.quicksilver.zone/v1/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    query MyQuery {
      message(where: {type: {_eq: "cosmos.staking.v1beta1.MsgEditValidator"}, value: {_cast: {String: {_like: "%0.059%"}}}}) {
        value
      }
    }
    """
)

# Execute the query on the transport
result = client.execute(query)

for message in result.get('message'):
  print(message.get('value').get('validator_address'))
