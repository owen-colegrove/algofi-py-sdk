# This sample is provided for demonstration purposes only.
# It is not intended for production use.
# This example does not constitute trading advice.
from algofi.config import ordered_symbols, decimals, scale
from algofi.v1.client import TestnetClient
from algofi.v1.repay_borrow import prepare_repay_borrow_transactions
from algofi.utils import TransactionGroup
from algosdk import mnemonic

# Hardcoding account keys is not a great practice. This is for demonstration purposes only.
# See the README & Docs for alternative signing methods.
sender = {
    'address': 'P4YQ75KCRZT6FF72AF4VZXZ5JDSQA6MVPN5EMCN3H6Z66DK3BRWUO3UQCI',
    'mnemonic': 'noodle learn crack outdoor salon acoustic blind creek panther elegant alone curve surface pair little salute steak above nature cook account chat column above universe'
}

client = TestnetClient(user_address=sender['address'])
client.init_params()
client.opt_in_all(mnemonic.to_private_key(sender['mnemonic']))
init_global_state = client.get_global_states()

print("~"*100)
print("Processing repay_borrow transactions for all assets")
print("~"*100)
for asset_name in ordered_symbols:
    print("Processing transaction for asset = %s" % (asset_name))
    txn_group = TransactionGroup(prepare_repay_borrow_transactions(sender['address'], mnemonic.to_private_key(sender['mnemonic']), client.params, 1*decimals[asset_name], asset_name))
    txn_group.set_transaction_keys([mnemonic.to_private_key(sender['mnemonic'])]*len(txn_group.transactions))
    txn_group.sign(sign_last_wlogic=False)
    result = client.submit(txn_group.signed_transactions, wait=True)

print("~"*100)
print("Global contract states after calling repay_borrow")
print("~"*100)
final_global_state = client.get_global_states()
for asset_name in ordered_symbols:
    print("Printing global state for asset = ", asset_name)
    print('initial underlying_cash=', init_global_state[asset_name]['underlying_cash']/decimals[asset_name])
    print('final underlying_cash=', final_global_state[asset_name]['underlying_cash']/decimals[asset_name])
    print('initial underlying_borrowed=', init_global_state[asset_name]['underlying_borrowed']/decimals[asset_name])
    print('final underlying_borrowed=', final_global_state[asset_name]['underlying_borrowed']/decimals[asset_name])
    print('initial total_borrow_interest_rate=', init_global_state[asset_name]['total_borrow_interest_rate']/scale)
    print('final total_borrow_interest_rate=', final_global_state[asset_name]['total_borrow_interest_rate']/scale)
    print("~"*100)

print("~"*100)
print("User local states after calling repay_borrow")
print("~"*100)
final_user_state = client.get_user_state()
print('final_user_state=', final_user_state)
for asset_name in ordered_symbols:
    print("Printing global state for asset = ", asset_name)
    print('user_bank_minted=', final_user_state[asset_name]['user_bank_minted']/decimals[asset_name])
    print('user_bank_pending_claim_mint=', final_user_state[asset_name]['user_bank_pending_mint']/decimals[asset_name])
    print('user_bank_pending_claim_burn=', final_user_state[asset_name]['user_underlying_pending_burn']/decimals[asset_name])
    print('user_active_collateral_amount=', final_user_state[asset_name]['user_active_collateral_amount']/decimals[asset_name])
    print('user_borrowed_amount=', final_user_state[asset_name]['user_borrowed_amount']/decimals[asset_name])
    print("~"*100)
