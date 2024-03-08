import requests

product_id = input("Enter product_id you want to delete\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = f"http://127.0.0.1:8001/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)

    # 204 -> delete
    print(get_response.status_code, get_response.status_code == 204)