from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: int
    username: str
    email: str
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: str = 'pending'
    user_id: Optional[int] = None

    def is_completed(self):
        return self.status == 'completed'

    def complete(self):
        self.status = 'completed'