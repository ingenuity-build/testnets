### Validating from Genesis

If you submitted a genesis transaction (gentx) file, you have need to ensure that the `.quicksilverd/config/priv_validator_key.json` from where you created the genesis transaction is present in your full node. 

### Create Validator

If you did NOT submit a genesis transaction, or your genesis transaction was not included because it was invalid, once you have `quicksilverd` running and sync, you can create a validator on the Quicksilver network via a `MsgCreateValidator` transaction:

```go
$ QUICKSILVER_VAL_CONS_KEY=$(quicksilverd tendermint show-validator)

$ quicksilver tx staking create-validator \
--amount=<amount> \
--pubkey=$QUICKSILVER_VAL_CONS_KEY \
--moniker="<moniker>" \
--chain-id="killerqueen-1" \
--commission-rate="<commission>" \
--commission-max-rate="<max-commission>" \
--commission-max-change-rate="<max-commission-rate-change>" \
--min-self-delegation="<min-self-delegation>" \
--fees=<fees> \
--from=<key-name>
```