import jwt
import json


def generate_api_token( payload, secret):
    header = {"alg": "HS256", "typ": "JWT"}
    encoded_jwt = jwt.encode(payload, secret, algorithm='HS256', headers=header)
    return json.dumps({"token": encoded_jwt})



def verify_api_token(token, secret):
    try:
        decoded_jwt = jwt.decode(token, secret, algorithms=["HS256"])
        return json.dumps({"payload": decoded_jwt})
    except:
        return {"error": "Invalid signature:"}
    
    
    
    

# example

payload = {"sub": "12364567890", "user": "John Doe"}
secret = "Ravipassword" #securely store secret in production

jwt_json = generate_api_token( payload, secret)
print(jwt_json)

jwt_dict = json.loads(jwt_json)
token = jwt_dict["token"]

decoded_jwt = verify_api_token(token, secret)
print(decoded_jwt)





