from pydantic import BaseModel, Field
from typing import Dict


class AssessmentSchema(BaseModel):
    user_id: int = Field(..., example=101)


    answers: Dict[str, str] = Field(
        ...,
        example={
            "1": "A",
            "2": "C",
            "3": "B"
        }
    )

    current_question: int = Field(..., example=4)
