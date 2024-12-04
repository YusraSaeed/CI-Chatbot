from fastapi import FastAPI
from dummy import users

app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello" : "World"}

@app.get("/users")
def get_all_users():
    return {
        "data" : users
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {
                "data" : user
            }
        
@app.post("/users")
def create_user(user: dict):
    users_count = len(users)
    new_user = {
        "id" : users_count+1,
        "name" : user["name"],
        "email" : user["email"]
    }
    users.append(new_user)
    return {
        "data" : new_user
    }

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {
                "data" : users
            }
        
@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    for i in range(len(users)):
        if users[i]["id"] == user_id:
            users[i]["name"] = user["name"]
            users[i]["email"] = user["email"]
            return {
                "data" : users[i]
            }