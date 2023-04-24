from typing import Type
import sqlalchemy

from src.database.repository import BaseRepository
from src.database.schema.tables import UserAddreses
from src.database.schema.schema import UserAddressCreate , UserAddressUpdate , UserAddressOut

# opreations system for collection inhreted by base repo

class UserAddressOperation(BaseRepository):
    @property
    def _table(self) -> sqlalchemy.Table:
        return UserAddreses

    @property
    def _schema_out(self) -> Type[UserAddressOut]:
        return UserAddressOut

    @property
    def _schema_create(self) -> Type[UserAddressCreate]:
        return UserAddressCreate

    @property
    def _schema_update(self) -> Type[UserAddressUpdate]:
        return UserAddressUpdate
