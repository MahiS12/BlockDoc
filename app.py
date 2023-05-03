# ------------------------------------------------------------------------------
# Imports
from flask import Flask, render_template,request, redirect
from PIL import Image
import imagehash
import json
from solcx import compile_standard, install_solc
from web3 import Web3
import imagepro
import os

# ------------------------------------------------------------------------------
# Flask App

app = Flask(__name__)

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


...
# For connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
# address = "0xd6C1280c15b78764db3E928D23189575f8fEd238"
# private_key = "f694ffddc3b2d6e28b3bd620d4363bfad7ff2950f07d69454835941f28127479" # leaving the private key like this is very insecure if you are working on real world project
# Create the contract in Python

DataExistence = w3.eth.contract(address='0x95D4Ef570615a3074a88169A507Dc330253485C6', abi=abi)

@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')


# @app.route('/admin')
# def admin():
#     return render_template("admin.html")

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template("about.html")

@app.route('/verify', methods=['GET','POST'])
def verify():
    if request.method== "POST":
        uid= request.form['uid']
        Iadd= request.form['I_add']
        Uadd= request.form['U_add']
        hash=request.files['hash']
        filen=hash.filename
        hash.save(os.path.join("./uploads-v", filen))
        hash_new=imagepro.generate_hashv(filen)
        

        # converted = imagehash.average_hash(hash)
        data = DataExistence.functions.verifyCertificate(uid,Iadd,Uadd,hash_new).call({ "from": Iadd})
# {% if data %}
#         <p>Certificate is valid.</p>
#     {% else %}
#         <p>Certificate is not valid.</p>
#     {% endif %}
        return render_template('verify.html', data=data)
    return render_template('verify.html')
    

@app.route('/get_certificate', methods=['GET','POST'])
def getcertificate():
    if request.method== "POST":
        uid= request.form['uid']
        Iadd= request.form['I_add']
        # converted = imagehash.average_hash(hash)
        store_data = DataExistence.functions.getCertificate(uid).call({"from":Iadd})
        error ="Successful"
        if store_data[4]== True:
            valid= "Yes"
        else:
            valid ="No"
        data= "Name: "+ store_data[0] + "\n" + "Issuer: " + store_data[1] + "\n"+ "User: " + store_data[2] + "\n"+ "Uid " + store_data[3] + "\n"+ "Is it Valid? " + valid 

        return render_template('get_certificate.html', data=data)
    return render_template('get_certificate.html')

@app.route('/issue',methods=['GET','POST'])
def issue():
    if request.method== "POST":
        name=request.form['name']
        Uadd= request.form['U_add']
        Iadd= request.form['I_add']
        uid= request.form['uid']
        
        
        hash=request.files['hash']
        filen=hash.filename
        hash.save(os.path.join("./uploads-i", filen))
        hash_new=imagepro.generate_hashi(filen)

        private_key=request.form['private']

        # converted = imagehash.average_hash(hash)
        store_data = DataExistence.functions.issueCertificate(name,Uadd,uid,hash_new).build_transaction({"chainId": chain_id, "from": Iadd, "gasPrice": w3.eth.gas_price, "nonce": w3.eth.get_transaction_count(Iadd)})

        sign_store_contact = w3.eth.account.sign_transaction(store_data, private_key=private_key)

        send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_contact)

        return render_template('issue.html', error =transaction_receipt)
    return render_template('issue.html')

@app.route('/invalidate',methods=['GET','POST'])
def invalidate():
    if request.method== "POST":
        uid= request.form['uid']
        Iadd= request.form['I_add']
        private_key=request.form['private']

        store_data = DataExistence.functions.invalidateCertificate(uid).build_transaction({"chainId": chain_id, "from": Iadd, "gasPrice": w3.eth.gas_price, "nonce": w3.eth.get_transaction_count(Iadd)})

        sign_store_contact = w3.eth.account.sign_transaction(store_data, private_key=private_key)

        send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_contact)

        return render_template('invalid.html', error =store_data)
    return render_template('invalid.html')

# @app.route('/connect-metamask')
# def connect_metamask():
#     if w3.is_connected():
#         # get the current account connected to MetaMask
#         accounts = w3.eth.accounts
#         if len(accounts) > 0:
#             return accounts[0]
#     return 'MetaMask not connected'

# nonce = w3.eth.get_transaction_count(address)
        # store_data = contact_list.functions.storeData(data).build_transaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce })

        # #Sign the transaction
        # sign_store_contact = w3.eth.account.sign_transaction(store_data, private_key=private_key)

        # send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)

        # transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_contact)
if __name__ == '__main__':
    app.run(debug=True)
