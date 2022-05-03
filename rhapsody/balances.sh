#!/bin/bash -i
set -e

source vars.sh

if [[ ! -f $QS_BIN ]]; then
    echo "Run 'make init' before running this command."
fi

if [[ ! -f $GAIA_BIN ]]; then
    echo "Run 'make init' before running this command."
fi

QS_KEY=$($QS_BIN --home $QS_HOME keys show validator --output=json | jq .address -r)
GAIA_KEY=$($GAIA_BIN --home $GAIA_HOME keys show gaia --output=json | jq .address -r)

echo "Balance of $QS_KEY on $CHAIN_ID:"
$QS_BIN --home $QS_HOME q bank balances $QS_KEY --node http://seed.quicktest-1.quicksilver.zone:26657 --output=json | jq .balances
echo
echo "Balance of $GAIA_KEY on qscosmos-1:"
$GAIA_BIN --home $GAIA_HOME q bank balances $GAIA_KEY --node http://seed.qscosmos-1.quicksilver.zone:26657 --output json | jq .balances

