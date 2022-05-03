#!/bin/bash -i
set -e

source vars.sh

if [[ ! -f $QS_BIN ]]; then
    echo "Run 'make init' before running this command."
fi

$QS_BIN --home /tmp/rhapsody/.quicksilver/ start > qs.log 2>&1 &
