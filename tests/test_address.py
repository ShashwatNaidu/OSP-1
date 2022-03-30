import sys
sys.path.append(".")

from osp import Address

residence_number = StringField(required=True,min_length=1,regex= r'[a-zA-Z0-9/, \\]+')
    street = StringField(required=True,min_length=1)
    locality = StringField(required=True,min_length=1)
    pincode = IntField(required=True,min_value=100000,max_value=999999)
    state = StringField(required=True,min_length=1)
    city = StringField(required=True, min_length=1)
print("#### Testing empty fields in address ####\n")
try:
    Address(residence_number="", street="", locality="", pincode="", state="", city="").save()
    print("FAILED: Incorrect address entered.")
except Exception as e:
    for key, value in e.__dict__["errors"].items():
        print(f"{key}: {value}")
    print("PASSED: Exceptions raised successfully.\n")


print("#### Testing invalid fields in address (should raise exceptions) ####\n")
try:
    Address(residence_number="@-402", street="@??", locality="Kukatpally", city="Hyderabad01234", state="Andhra012", pincode="3d34fk").save()
    print("FAILED: Incorrect address entered.")
except Exception as e:
    for key, value in e.__dict__["errors"].items():
        print(f"{key}: {value}")
    print("PASSED: Exceptions raised successfully.\n")

print("#### Testing correct fields in address (should save address successfully) ####\n")
try:
    Address(residence_number="D/704, Lodha Meridian", street="Kukatpally", locality="KPHB", city="Hyderabad", state="Andhra Pradesh", pincode="500072").save()
    print("PASSED: Correct address saved successfully.")
except Exception as e:
    for key, value in e.__dict__["errors"].items():
        print(f"{key}: {value}")
    print("FAILED: Correct address raised exceptions.\n")