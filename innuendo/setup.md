# Full Node

### Prerequisites:

Recommended hardware will depend on use cases and desired functionalities. However, the minimum specifications **required** are as follows: 

2+ vCPU

4+ GB RAM

120+ GB SSD

### Installing Node:

Before installing your node, please verify you meet all the prerequisites to participating in Killer Queen above. 

Operators can install the `quicksilverd` binary from the source.

```
sudo apt update && sudo apt upgrade --yes

sudo apt install make clang pkg-config libssl-dev build-essential git jq ncdu bsdmainutils htop net-tools lsof --yes

```
ver="1.18.1"
wget "https://golang.org/dl/go$ver.linux-amd64.tar.gz"
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf "go$ver.linux-amd64.tar.gz"
rm "go$ver.linux-amd64.tar.gz"
echo "export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin" >> $HOME/.bash_profile
source $HOME/.bash_profile
go version
```

Once you have your environment setup correctly, clone the Quicksilver repository and install the binary:

```
git clone https://github.com/ingenuity-build/quicksilver.git --branch v0.6.1

cd quicksilver && make install
```

The `quicksilverd` binary will be installed into your `$GOPATH/bin` directory.

Finally, verify your quicksilverd version:

```
quicksilverd version
```

Verify you are using **v0.6.1** for the `innuendo-1` testnet.

To initialize your node,
```
# Replace moniker with your desired node's moniker.

quicksilverd init NAME --chain-id killerqueen-1
```

Once initialized, overwrite the default genesis.json file with genesis state file for the particular network that you are joining. You may retrieve the genesis state file from the Quicksilver repository or another trusted source:

```
cd ~/.quicksilverd/config

wget https://raw.githubusercontent.com/ingenuity-build/testnets/main/innuendo/genesis.json

## verify the downloaded file matches the following hash:

fbdd75dfea60bc17d4c4966cd2b2146b6a5aa282f5f4b1af46ae4e6d9d38c37c  genesis.json

```

### Keyring

Before creating a validator, you must create an operator key. This will be used to identify your validator in the Quicksilver network. 

```go
quicksilverd keys add <key-name> [flags]
```

By default, quicksilver will store keys in your OS-backed keyring. You can change this behavior by specifying the `--keyring-backend` flag.

To import an existing key via a mnemonic - for example if you generated and submitted a genesis transaction, you can provide a `--recover` flag and the `keys add` command will prompt you for the BIP39 mnemonic.

**SECURITY NOTE:** _Keep separate mnemonics and keys for testnet purposes. Never reuse mnemonics or keys associated with live wallets or mainnets. It poses a great security risk to do so!_

Visit the Cosmos SDK's keyring [documentation](https://docs.cosmos.network/v0.43/run-node/keyring.html) for more information.

For a secure keyring setup, using Ledger, you can follow this guide by a community member (approved by our dev team):

[https://github.com/rishisidhu/Quicksilver-guides/blob/main/generating_quicksilver_address.md](https://github.com/rishisidhu/Quicksilver-guides/blob/main/generating_quicksilver_address.md)
