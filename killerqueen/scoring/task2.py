#curl 'https://data.killerqueen-1.quicksilver.zone/v1/graphql' \
#  -H 'content-type: application/json' \
#  -H 'x-hasura-admin-secret: myadminsecretkey' \
#  --data-raw '{"query":"\nquery MyQuery {validator_signing_info(where: {jailed_until: {_eq: \"1970-01-01 00:00\"}, tombstoned: {_eq: false}}, order_by: {index_offset: asc}) {validator_address jailed_until start_height }}","variables":null,"operationName":"MyQuery"}' \
#  --compressed

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://data.killerqueen-1.quicksilver.zone/v1/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    query MyQuery {validator_signing_info(where: {jailed_until: {_eq: "1970-01-01 00:00"}, tombstoned: {_eq: false}}, order_by: {index_offset: asc}) {validator_address jailed_until start_height index_offset}}
    """
)

# Execute the query on the transport
result = client.execute(query)

for validator in result.get('validator_signing_info'):
  print('{}, {}, {}'.format(validator.get('validator_address'),validator.get('start_height'),validator.get('index_offset')))
