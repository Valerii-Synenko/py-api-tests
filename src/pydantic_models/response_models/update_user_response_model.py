from typing import Optional

from pydantic import BaseModel


class UpdateUseResponse(BaseModel):
    name: Optional[str] = None
    job: Optional[str] = None
    updatedAt: str