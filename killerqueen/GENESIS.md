Install quicksilver v0.3.0

``` git clone https://github.com/ingenuity-build/quicksilver.git
cd quicksilver
git checkout v0.3.0
make install```

find the lastest binary in your GOBIN folder(probably ~/go/bin)

# killerqueen-1 Genesis Transaction

In order to become a genesis validator on `killerqueen-1`, you must generate a gentx (genesis transaction) in the following way:

## Init a new Quicksilver instance, using: 

```quicksilverd init <your_moniker> --chain-id 'killerqueen-1'```

- Create, or recover a key, using 

```quicksilverd keys add <keyname>` or `quicksilver keys add <keyname> --recover```

## Fund your account 

```quicksilverd add-genesis-account <keyname> 100000000uqck```

## Create the gentx with 

```quicksilverd gentx <keyname> 100000000uqck --moniker <validatorname> --chain-id killerqueen-1```  

You may use `quicksilverd gentx -h` to see additional flags for setting commission / identities / etc.)

You will receive output such as: `Genesis transaction written to "/tmp/killerqueen/config/gentx/gentx-41eb6aa3ce902adf9603b1a1c55d005790a099c1.json"`

Copy the contents of this file into the registration form.

