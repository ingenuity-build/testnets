# Innuendo-5 chain restart instructions

Chain restart is due at 1605 UTC on Tuesday 17th January 2023. We will use `quicksilverd v1.3.0` to export and restart the chain. You must upgrade before the export, else the export will fail. For build instructions, see below.

1. `git fetch && git checkout v1.3.0`
2. `make install`
3. `quicksilverd export --for-zero-height --height 608612 > export-innuendo-4-608612.json`
4. `jq . export-innuendo-4-608612.json -S -c | shasum -a256`
5. Check output matches `7df73ba5fdbaf6f4b5cced3f16b8f44047ad8f42a7a6f87f764413b474e81c54`
6. Run `python3 migrate-genesis.py`
7. `jq . genesis.json -S -c | shasum -a256`
8. Check output matches `cab2352d12f9e388bc633d909a26eaea8fc52904990405cd20d72077415a51d2`
9. `cp genesis.json ~/.quicksilverd/config/genesis.json` (be sure to replace `~/.quicksilverd` with your node's `HOME`).
10. `quicksilverd tendermint unsafe-reset-all`
11. If you use an external signer, update the chain_id and reset state.
12. `quicksilverd start` or, if using systemd, `systemctl start quicksilver`