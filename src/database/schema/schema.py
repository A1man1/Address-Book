from src.database.repository import BaseSchema, CreateTimeModelMixin, ModifiedTimeModelMixin
 
class UserAddress(BaseSchema):
			name: str
			fullname : str
			address: str
			latitude: float
			longitude: float
			
class UserAddressCreate(UserAddress, CreateTimeModelMixin):
			pass

class UserAddressUpdate(UserAddress, ModifiedTimeModelMixin):
			pass

class UserAddressOut(UserAddressCreate,UserAddressUpdate):
    pass

   
        

