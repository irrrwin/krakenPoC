import json

from kraken_futures_rest import RestApiMethods



API_PATH = "https://futures.kraken.com" # futures API URL 
PUB_KEY = "" # futures API public key
PRIV_KEY = "" # futures API private key

FROM_USER_UID = "" # account 1 uid
TO_USER_UID = "" # account 2 uid
FROM_ACCOUNT = "cash" # 'flex' or 'cash'
TO_ACCOUNT = "cash" # 'flex' or 'cash'
UNIT = "USD"

TRANSFER_AMOUNT = 10


def main():
    rest_client = RestApiMethods(
        api_path=API_PATH, 
        api_public_key=PUB_KEY, 
        api_private_key=PRIV_KEY
    )
    response = json.loads(rest_client.transfer_subaccounts(
        fromUser=FROM_USER_UID,
        toUser=TO_USER_UID,
        fromAccount=FROM_ACCOUNT,
        toAccount=TO_ACCOUNT,
        unit=UNIT,
        amount=TRANSFER_AMOUNT
    ))
    print(response)

if __name__ == "__main__":
    main()