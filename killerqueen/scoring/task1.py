import requests
import time
import json

validators = {}

def process_block(block_json):
  commit = block_json.get('result').get('block').get('last_commit')
  height = commit.get('height')
  for signature in commit.get("signatures"):
    addr = signature.get('validator_address')
    if addr != '':
      old = validators.get(addr, {'blocks': [], 'first': 100})
      blocks = old.get('blocks')
      first = old.get('first')
      if first > int(height):
        first = int(height)
      blocks.append(int(height))
      validators.update({addr: {"blocks": blocks, "first": first}}) 
  print(height)          


for block in range(1,101):
  req = requests.get("https://rpc.killerqueen-1.quicksilver.zone/block?height={}".format(block+1), timeout=10)
  res = req.json()
  process_block(res)
  time.sleep(1)

for k,v in validators.items():
  print("{}, {}, {}".format(k, v.get('first'), len(v.get('blocks'))))
