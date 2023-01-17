#!/usr/bin/python3
import json

'''
This script exists to take raw exported state from innuendo-4 chain, zero the interchainstaking and interchainquery state, and ibc connections/channels/clients.
It also burns the qAsset and ibc/denom balances



Chain ID is set to innuendo-5 and the genesis time is set to 1605 UTC on 17/01/2023.
'''

with open('export-innuendo-4-608612.json') as file:
  input = json.load(file)
  file.close()

coins_to_burn = {}
## remove qatoms and ibc denoms
print("⚛️  Removing uqatom and ibc denoms from account balances")
balances = input.get('app_state').get('bank').get('balances')
for account_index, account in enumerate(balances):
  balance = account.get('coins', [])
  for coin_index, coin in enumerate(account.get('coins', [])):
    if coin.get('denom') != "uqck":
      coins_to_burn.update({coin.get('denom'): coins_to_burn.get(coin.get('denom'), 0)+int(coin.get('amount'))})
      print("  ⚛ Removing {} from {}".format(coin, account.get('address')))
      balance.remove(coin)
      account.update({'coins': balance})

print("⚛️  Coins to remove from supply")
print(coins_to_burn)

supply = input.get('app_state').get('bank').get('supply')
print("⚛️  Supply before migration")
print(supply)
for denom, amount in coins_to_burn.items():
  print("  ⚛ Removing {} from supply".format({"amount": str(amount), "denom": denom}))
  supply.remove({"amount": str(amount), "denom": denom})

print("⚛️  Supply post migration")
print(input.get('app_state').get('bank').get('supply'))

print("⚛️  Removing ibc channels, clients, connections and capabilities")
## remove ibc capabilities, clients, connections, channels
input.get('app_state').update({'capability': {"index": "1"}})
input.get('app_state').get('ibc').update({"channel_genesis": {"channels": [],"acknowledgements": [],"commitments": [],"receipts": [],"send_sequences": [],"recv_sequences": [],"ack_sequences": [],"next_channel_sequence": "0"}, "client_genesis": {"clients": [], "clients_consensus": [], "clients_metadata": [], "params": {"allowed_clients": ["06-solomachine","07-tendermint"]}, "create_localhost": False, "next_client_sequence": "0"}, "connection_genesis": {"connections": [],"client_connection_paths": [],"next_connection_sequence": "0","params": {"max_expected_time_per_block": "30000000000"}}})
input.get('app_state').get('transfer').update({'denom_traces': []})
input.get('app_state').get('interchainaccounts').update({"controller_genesis_state": {"active_channels": [],"interchain_accounts": [],"ports": [],"params": {"controller_enabled": True}},"host_genesis_state": {"active_channels": [],"interchain_accounts": [],"port": "icahost","params": {"host_enabled": False,"allow_messages": []}}})

## remove interchainstaking / interchain query entries
print("⚛️  Zeroing interchainstaking and interchainquery state")
input.get('app_state').get('interchainquery').update({'queries': []})
input.get('app_state').update({'interchainstaking': {'params': input.get('app_state').get('interchainstaking').get('params')}})

## reset epochs
print("⚛️  Zeroing epoch state")
input.get('app_state').get('epochs').get('epochs')[0].update({"start_time": "0001-01-01T00:00:00Z", "current_epoch": "0", "current_epoch_start_time": "0001-01-01T00:00:00Z", "epoch_counting_started": False, "current_epoch_start_height": "0"})
input.get('app_state').get('epochs').get('epochs')[1].update({"start_time": "0001-01-01T00:00:00Z", "current_epoch": "0", "current_epoch_start_time": "0001-01-01T00:00:00Z", "epoch_counting_started": False, "current_epoch_start_height": "0"})





## chain id and genesis time
print("⚛️  Setting chain id and genesis time")
input.update({'chain_id': 'innuendo-5', 'genesis_time': '2023-01-17T16:05:00Z'})

with open("genesis.json", "w+") as file:
  json.dump(input, file)
  file.close()
