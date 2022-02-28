from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development','ganache-local']
FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork','mainnet-fork-dev']

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_mocks():
    print("deploying mocks")
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks Deployed")