from pydantic import BaseModel


class User(BaseModel):
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str
    estado_clickup: str

    def to_dict(self) -> dict[str, str]:
        return {
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "phone": self.phone,
            "website": self.website,
            "estado_clickup": self.estado_clickup
        }
