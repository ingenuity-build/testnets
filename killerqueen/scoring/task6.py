from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import bech32

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://data.killerqueen-1.quicksilver.zone/v1/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    query MyQuery {
      message(where: {type: {_eq: "cosmos.staking.v1beta1.MsgBeginRedelegate"}}) {
        value
      }
    }
    """
)

# Execute the query on the transport
result = client.execute(query)

def compare(a, b):
  if len(a) != len(b):
    return False
  for i in range(len(a)):
    if a[i] != b[i]:
      return False
  return True

for message in result.get('message'):
  delg = message.get('value').get('delegator_address')
  val = message.get('value').get('validator_src_address')
  hrp, delg_dec = bech32.bech32_decode(delg)
  hrp, val_dec = bech32.bech32_decode(val)  
  if compare(val_dec, delg_dec):
    print(delg)
