import requests
import time
from datetime import datetime
from config import API_TOKEN


# transaction_id = input("Please provide the transaction ID (hex) you want to process:")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}



def get_readable_address(address):
    url = f"https://toncenter.com/api/v2/packAddress?address={address}"
    try:
        response = requests.get(url)
        # avoid too many requests 
        time.sleep(1)
        if response.status_code == 200:
            data = response.json()
            if "result" in data:
                return data["result"]
            
            else:
                return address
        else:
            return address
    except:
        print("request err")
        

def process_transaction(data):
    sender_address = data['account']['address']
    sender_address_readable = get_readable_address(sender_address)
    
    decoded_op_name = data['in_msg'].get('decoded_op_name')

    if decoded_op_name == "nft_ownership_assigned":
        receiver_address = data['in_msg']['source']['address']
        receiver_address_readable = get_readable_address(receiver_address)
        amount = data['in_msg']['value']
        asset = "NFT"
    elif decoded_op_name == "jetton_notify":
        receiver_address = data['in_msg']['source']['address']
        receiver_address_readable = get_readable_address(receiver_address)
        amount = int(data['in_msg']['decoded_body'].get('amount', 0)) // 10**9
        asset = "Jetton"
    else:
        return

    status = "Success" if data['success'] else "Failure"
    confirm_time = data['utime']
    transaction_time = datetime.fromtimestamp(confirm_time).strftime('%Y-%m-%d %H:%M:%S')

    print("Sender Address:", sender_address_readable)
    print("Receiver Address:", receiver_address_readable)
    print(f"Amount: {amount} {asset}")
    print("Status:", status)
    print("Confirm Time:", transaction_time)
    return transaction_time,status,sender_address,receiver_address,amount,asset


def get_tx_info(txid:str):

    url = f"https://tonapi.io/v2/blockchain/transactions/{txid}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        out_msgs = data.get('out_msgs', [])

        if out_msgs:
            sender_address = data['account']['address']
            sender_address_readable = get_readable_address(sender_address)
            
            receiver_address = data['out_msgs'][0]['destination']['address']
            receiver_address_readable = get_readable_address(receiver_address)
            amount = int(data['out_msgs'][0]['value']) // 10**9
            asset = "TON"
            status = "Success" if data['success'] else "Failure"
            confirm_time = data['utime']
            transaction_time = datetime.fromtimestamp(confirm_time).strftime('%Y-%m-%d %H:%M:%S')

            print("Sender Address:", sender_address_readable)
            print("Receiver Address:", receiver_address_readable)
            print(f"Amount: {amount} {asset}")
            print("Status:", status)
            print("Confirm Time:", transaction_time)
            return transaction_time,status,sender_address,receiver_address,amount,asset
        else:
            return process_transaction(data)
    else:
        print("Request failed with status code:", response.status_code)
        
#NFT: b811cf201eea9aa49b7648e709b1caf3c03c25f6c56d00e47eba52779999d717
#TON: 0d90d5fc328a01b91074b8d8942be6e5b4901fe89fbcaa20667d1d0e85ca8160
#Jetton: 87e48d95f4442c9fe42a502a380f4269a366d30a2e959985b000c2f878b0bd00