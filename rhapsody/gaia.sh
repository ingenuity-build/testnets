#!/bin/bash -i
set -e

source vars.sh

### BUILD ###
mkdir -p $DIR

if [[ ! -x $DIR/gaia ]]; then
    git clone https://github.com/cosmos/gaia --branch=$GAIA_VERSION $DIR/gaia
fi

cd $DIR/gaia
make build

### CONFIGURATION ###

CHAIN_ID=qscosmos-1

RPC="http://seed.qscosmos-1.quicksilver.zone:26657"

BINARY=./build/gaiad

$GAIA_BIN config chain-id $CHAIN_ID --home $GAIA_HOME
$GAIA_BIN config keyring-backend test --home $GAIA_HOME
$GAIA_BIN config broadcast-mode block --home $GAIA_HOME

$GAIA_BIN --home $GAIA_HOME keys add gaia > /dev/null
