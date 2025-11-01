link ="https://www.youtube.com/watch?v=XIdQ6gO3Anc"

from pydantictutorial import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, v):
        if v <= 0:
            raise ValueError(f"account_id must be positive: {v}")
        return v

data = [
    {"name": "Amirul", 
     "email": "ami@email.com", 
     "account_id":21},
    {"name": "Daniel", 
     "email": "dan@email.com", 
     "account_id":22}     
     ]
    



user1 = User(
    name="Zachary",
    email="Zach@email.com",
    account_id="26"
)
user2 = User(
    name="Faris",
    email="faris@gmail.com",
    account_id=25
)

user3 = User(**data[1])




# print(f"{user1.name}'s email is {user1.email} and his account id is {user1.account_id}")


# print(f"{user3.name}'s email is {user3.email} and his account id is {user3.account_id}")


print(user1.model_dump(exclude="email"))

print(user1.model_dump_json(exclude="account_id"))


raw_json = user1.model_dump_json()

user4 = User.model_validate_json(raw_json)

print(user4)