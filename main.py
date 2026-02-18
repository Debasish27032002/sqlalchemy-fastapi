from models import create_table
from services import *
create_table()

create_user("Swarnalata", "swarnalata@example.com")
user = get_single_user(1)
print(user)

users = get_all_user()
print(users)

user = update_user_email(1, "Debasish@gmail.com")
print(user, "Email updated successfully")

delete_user(1)