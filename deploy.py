from solcx import compile_standard, install_solc
import json
from web3 import Web3

with open("Verification.sol", "r") as file:
    Data_Existence_file = file.read()

install_solc("0.8.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"Verification.sol": {"content": Data_Existence_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"] # output needed to interact with and deploy contract 
                }
            }
        },
    },
    solc_version="0.8.0",
)
print(compiled_sol)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

#get bytecode
bytecode = compiled_sol["contracts"]["Verification.sol"]["Verification"]["evm"]["bytecode"]["object"]
# get abi
abi = json.loads(compiled_sol["contracts"]["Verification.sol"]["Verification"]["metadata"])["output"]["abi"]

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
address = "0xB2E63cf1D459efC76CB52e717590A7f104471BCA"
private_key = "31301c4259aadc5304c7b340c6303f6108c97f7a5e161bcf6967403f54000de5" # leaving the private key like this is very insecure if you are working on real world project
# Create the contract in Python

# DataExistence = w3.eth.contract(abi=abi, bytecode=bytecode)
# # Get the number of latest transaction
# nonce = w3.eth.get_transaction_count(address)
# # build transaction
# transaction = DataExistence.constructor().build_transaction(
#     {
#         "chainId": chain_id,
#         "gasPrice": w3.eth.gas_price,
#         "from": address,
#         "nonce": nonce,
#     }
# )
# # Sign the transaction
# sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# print("Deploying Contract!")

# transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)

# transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
# print(f"Contract deployed to {transaction_receipt.contractAddress}")

# contractaddress= transaction_receipt.contractAddress
contact_list = w3.eth.contract(address='0x95D4Ef570615a3074a88169A507Dc330253485C6', abi=abi)

# add= w3.eth.accounts[0]
# # store_data = contact_list.functions.isIssuer(add).build_transaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce + 1})
uid= '1'
# iadd= '0x453AE06e7927CF439B0636c3E7c8E6ef27Fe0416'
# uadd= '0x' + 'd6C1280c15b78764db3E928D23189575f8fEd238'
# hash= '2'
name= 'Vamsi'
issuer= 'Monika'


#store_data = contact_list.functions.isIssuer().call({"from":address})
# # nonce = nonce +1
# store_data = contact_list.functions.registerUser(name).build_transaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": w3.eth.get_transaction_count(address)})

# sign_store_contact = w3.eth.account.sign_transaction(store_data, private_key=private_key)

# send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
# transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_contact)
# # tx_hash = contact_list.functions.registerIssuer(name).transact()
# # # # Wait for the transaction to be mined
# # w3.eth.waitForTransactionReceipt(tx_hash)
store_data = contact_list.functions.getIssuedByCount().call({"from":address})
# build_transaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": w3.eth.get_transaction_count(address)})

# sign_store_contact = w3.eth.account.sign_transaction(store_data, private_key=private_key)

# send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
# transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_contact)

print(store_data)

# useradd= 0x453AE06e7927CF439B0636c3E7c8E6ef27Fe0416
# userpriv= 6f88b61349bf315f66d44c6efe1be3b4979c4110ec68901ec131a9908fc99266
#user add= 0x2E72F949367DF9F1e0eEe6310810dE06EE64bd05
# 07be3414a317194440d9e23dc3a9dbd730bf389b3f5d63f13b74b5c89d253aa6
#user name =Mahi

# issueradd= 0xB2E63cf1D459efC76CB52e717590A7f104471BCA
# issuerpriv= 31301c4259aadc5304c7b340c6303f6108c97f7a5e161bcf6967403f54000de5
#issuer monika
#issuer 2 add= 0x03bCf87Bc66bD8B762f7c8837E90e82FAB2479Ef
#issuer 2 priv key= 2679a36d0dffc331215adb6b4af271e3acde869c85881d941121f3249725df6b

