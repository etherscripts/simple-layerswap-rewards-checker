# Coded by: https://t.me/CryptoResearchLab

import requests

layer_swap_endpoint = "https://bridge-api.layerswap.io//api/campaigns/2/rewards/{}"


def check_address_for_rewards(address, endpoint):
    try:
        url = endpoint.format(address)
        response = requests.get(url)
        return response.json()
    except Exception as error:
        print(f"Возникла ошибка: {error}.")


def process_addresses(file_path):
    try:
        with open(file_path, 'r') as file:
            addresses = file.read().splitlines()

        for address in addresses:
            layer_swap_rewards = check_address_for_rewards(address, layer_swap_endpoint)

            total_amount = layer_swap_rewards['data']['user_reward']['total_amount']
            total_pending_amount = layer_swap_rewards['data']['user_reward']['total_pending_amount']
            period_pending_amount = layer_swap_rewards['data']['user_reward']['period_pending_amount']

            print(f"{address} | Total Earnings: {total_amount} | Pending Earnings: {total_pending_amount}"
                  f" | Period Pending Amount: {period_pending_amount}")

    except Exception as error:
        print(f"Возникла ошибка: {error}.")


if __name__ == "__main__":
    file_path = "addresses.txt"
    process_addresses(file_path)
