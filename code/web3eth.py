from web3 import Web3

# Connection a ganache
ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.is_connected()

# Comptes de ganache
account1 = "0xfBEB2fAC03cCC40243fD6bF4407BA20156D75CcB"
account2= "0x19dBbA921C62E484B0d713ceBb93F237beBbB1D9"
private_key_1 = "0x9a94c0d0dff621b1cacf8d9d4adae4e21ec9de6eae64b3c7fb0896a03c0f084b"

# Prendre le nonce
nonce = web3.eth.get_transaction_count(account1)
print(f'Nonce: {nonce}')

# Creer la transaction
tx = {
    "nonce": nonce,
    "to": account2,
    "value": Web3.to_wei(1, "ether"),
    "gas": 21000,
    "maxFeePerGas": 800000000,
    "maxPriorityFeePerGas": 10,
    "chainId": web3.eth.chain_id
}
# Signer la transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key_1)
print(f'Signed Transaction: {signed_tx}')

# Envoyer la transaction et Recevoir le hash de la transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(f'Transaction Hash: {tx_hash}')


