import dataclasses as dc


@dc.dataclass(repr=True)
class Record:
    type: str
    name: str
    content: str
    ttl: str
    id: str = ""
