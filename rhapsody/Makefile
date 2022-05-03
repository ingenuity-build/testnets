#!/usr/bin/make -f

init:
	./quicksilver.sh
	./gaia.sh

clean:
	rm -rf /tmp/rhapsody

keys:
	./keys.sh

balances:
	./balances.sh

start:
	./start.sh
stop:
	pkill quicksilverd

logs:
	tail -f qs.log

validate:
	./validate.sh
