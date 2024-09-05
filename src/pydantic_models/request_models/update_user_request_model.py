from typing import Optional

from pydantic import BaseModel


class UpdateUserRequest(BaseModel):
    name: Optional[str] = None
    job: Optional[str] = None
