# Rhapsody Testnet
Quicksilver Testnet Instructions and Config

**If you experience any bugs, issues or problems, please raise an issue here:** https://github.com/ingenuity-build/quicksilver

## Details

 - Chain-ID: `quicktest-2`
 - Launch Date: 2022-05-01
 - Current Version: `v0.1.3`
 - Genesis File: https://raw.githubusercontent.com/ingenuity-build/testnets/main/rhapsody/genesis.json


### Nodes
We are running the following nodes:

 - node01.quicktest-1.quicksilver.zone:26657
 - node02.quicktest-1.quicksilver.zone:26657
 - node03.quicktest-1.quicksilver.zone:26657
 - node04.quicktest-1.quicksilver.zone:26657

Seeds:

 - dd3460ec11f78b4a7c4336f22a356fe00805ab64@seed.quicktest-1.quicksilver.zone:26656


## Configuration

Download and build Quicksilver:

    git clone https://github.com/ingenuity-build/quicksilver.git --branch v0.1.3
    cd quicksilver
    make build

Testnet configuration script (`touch scripts/testnet-conf.sh`):

    #!/bin/bash -i
    
    set -xe
    
    ### CONFIGURATION ###
    
    CHAIN_ID=quicktest-2
    
    GENESIS_URL="https://raw.githubusercontent.com/ingenuity-build/testnets/main/rhapsody/genesis.json"
    SEEDS="dd3460ec11f78b4a7c4336f22a356fe00805ab64@seed.quicktest-1.quicksilver.zone:26656"
    
    BINARY=./build/quicksilverd
    NODE_HOME=$HOME/.quicksilverd
    
    # SET this value for your node:
    NODE_MONIKER="Your_Node"
    
    ### OPTIONAL STATE ###
    
    # if you set this to true, please have TRUST HEIGHT and TRUST HASH and RPC configured
    export STATE_SYNC=false
    # set height
    export TRUST_HEIGHT=
    # set hash
    export TRUST_HASH=""
    export SYNC_RPC="http://node02.quicktest-1.quicksilver.zone:26657,http://node03.quicktest-1.quicksilver.zone:26657,http://node04.quicktest-1.quicksilver.zone:26657"
    
    echo  "Initializing $CHAIN_ID..."
    $BINARY config chain-id $CHAIN_ID --home $NODE_HOME
    $BINARY config keyring-backend test --home $NODE_HOME
    $BINARY config broadcast-mode block --home $NODE_HOME
    $BINARY init $NODE_MONIKER --chain-id $CHAIN_ID --home $NODE_HOME
    
    echo "Get genesis file..."
    curl -sSL $GENESIS_URL > $NODE_HOME/config/genesis.json
    
    if  $STATE_SYNC; then
        echo  "Enabling state sync..."
        sed -i -e '/enable =/ s/= .*/= true/'  $NODE_HOME/config/config.toml
        sed -i -e "/trust_height =/ s/= .*/= $TRUST_HEIGHT/"  $NODE_HOME/config/config.toml
        sed -i -e "/trust_hash =/ s/= .*/= \"$TRUST_HASH\"/"  $NODE_HOME/config/config.toml
        sed -i -e "/rpc_servers =/ s/= .*/= \"$SYNC_RPC\"/"  $NODE_HOME/config/config.toml
    else
        echo  "Disabling state sync..."
    fi
    
    echo "Set seeds..."
    sed -i -e "/seeds =/ s/= .*/= \"$SEEDS\"/"  $NODE_HOME/config/config.toml

Run this script from the quicksilver repository main directory;

Remember to make it executable:

    chmod +x scripts/testnet_conf.sh

Then simply run:

    ./scripts/testnet_conf.sh

## Running your node
At this point you can run the node on the CLI with `./build/quicksilverd start` to ensure everything is configured correctly. At this point you may configure your system to run Quicksilver as a system service or daemon.

## Upgrade to Validator

### Test Wallet
To run as a validator you will need to create a QCK wallet:

    ./build/quicksilverd keys add $YOUR_TEST_WALLET --keyring-backend=test

If you already have a test wallet you want to use run (and enter your mnemonic):

    ./build/quicksilverd keys add $YOUR_TEST_WALLET --recover --keyring-backend=test

### Faucet

Join our discord server to access the faucets for QCK and ATOM. Make sure you are in the appropriate channel:

 - **qck-tap** for QCK tokens;
 - **atom-tap** for ATOM tokens;

To check the faucet address:

    $faucet_address rhapsody

To check your balance:

    $balance $YOUR_TEST_WALLET rhapsody

To request a faucet grant:

    $request $YOUR_TEST_WALLET rhapsody

### Validator Tx

Then simply run the tx to upgrade to validator status:

    ## Upgrade node to validator
    ./build/quicksilverd tx staking create-validator \
      --from=$YOUR_TEST_WALLET \
      --amount=1000000uqck \
      --moniker=$NODE_MONIKER \
      --chain-id=$CHAIN_ID \
      --commission-rate=0.1 \
      --commission-max-rate=0.5 \
      --commission-max-change-rate=0.1 \
      --min-self-delegation=1 \
      --pubkey=$($BINARY tendermint show-validator)


## Using minting qAtoms on Quicksilver

Instructions to come early next week!
