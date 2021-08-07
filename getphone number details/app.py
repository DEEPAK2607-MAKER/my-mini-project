import phonenumbers
from phonenumbers import carrier ,geocoder,timezone
mobileno = input("enter the mobile number  with the country code")
mobileno = phonenumbers.parse(mobileno)

print(timezone.time_zones_for_number(mobileno))

print(carrier.name_for_number(mobileno,"en"))

print(geocoder.description_for_number(mobileno,"en"))

print("valid mobile number :",phonenumbers.is_valid_number(mobileno))

print("checking possibility of number :",phonenumbers.is_possible_number(mobileno))