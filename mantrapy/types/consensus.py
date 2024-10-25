from dataclasses import dataclass
from datetime import datetime


@dataclass
class SyncInfo:
    latest_block_hash: str
    latest_app_hash: str
    latest_block_height: str
    latest_block_time: datetime
    earliest_block_hash: str
    earliest_app_hash: str
    earliest_block_height: str
    earliest_block_time: datetime
    catching_up: bool

    def __post_init__(self):
        """Validate the data after initialization"""
        if not all(
                isinstance(x, str) for x in [
                    self.latest_block_hash,
                    self.latest_app_hash,
                    self.latest_block_height,
                    self.earliest_block_hash,
                    self.earliest_app_hash,
                    self.earliest_block_height,
                ]
        ):
            raise ValueError('All hash and height values must be strings')

        if not isinstance(self.catching_up, bool):
            raise ValueError('catching_up must be a boolean')

        if not isinstance(self.latest_block_time, datetime) or not isinstance(
                self.earliest_block_time,
                datetime,
        ):
            raise ValueError('Block times must be datetime objects')

    @classmethod
    def from_dict(cls, data: dict) -> 'SyncInfo':
        """Create SyncInfo from dictionary data with error handling"""
        try:
            return cls(
                latest_block_hash=str(data['latest_block_hash']),
                latest_app_hash=str(data['latest_app_hash']),
                latest_block_height=str(data['latest_block_height']),
                latest_block_time=datetime.fromisoformat(
                    data['latest_block_time'].replace('Z', '+00:00'), ),
                earliest_block_hash=str(data['earliest_block_hash']),
                earliest_app_hash=str(data['earliest_app_hash']),
                earliest_block_height=str(data['earliest_block_height']),
                earliest_block_time=datetime.fromisoformat(
                    data['earliest_block_time'].replace('Z', '+00:00'), ),
                catching_up=bool(data['catching_up']),
            )
        except KeyError as e:
            raise ValueError(f'Missing required field: {e}')
        except ValueError as e:
            raise ValueError(f'Invalid data format: {e}')
