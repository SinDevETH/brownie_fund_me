from brownie import FundMe, accounts
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me

def fund():
    fund_me = FundMe[-1]
    print(fund_me.address)
    # fund_me = deploy_fund_me()
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f'The current entrance fee is {entrance_fee}')
    print("FUNDING ... ")
    fund_me.fund({"from":account, "value": entrance_fee})


def withdraw():
    print("WITHDRAWING ...")
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from":account})

def main():
    fund()
    withdraw()