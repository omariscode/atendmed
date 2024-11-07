from app import db
from sqlalchemy.orm import Mapped, mapped_column

class Appoitments(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column()
    message: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return self.message[0:50]