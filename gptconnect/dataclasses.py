from dataclasses import dataclass


# Not fully tested
types_lookup = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
    list: "array",
    dict: "object",
}


@dataclass
class Property:
    type: type
    description: str
    enum: list = None

    def __post_init__(self):
        if not self.enum:
            self.enum = []


@dataclass
class Params:
    properties: dict
    required: list

    def properties_dict(self):
        _properties = {}
        for key, value in self.properties.items():
            _properties[key] = value.__dict__
            _properties[key]["type"] = types_lookup[_properties[key]["type"]]
        return _properties

