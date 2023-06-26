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


@dataclass
class Params:
    properties: dict
    required: list

    def properties_dict(self):
        _properties = {}
        for key, value in self.properties.items():
            _properties[key] = value.__dict__
            _properties[key]["type"] = types_lookup[_properties[key]["type"]]
            if not _properties[key].get("enum"):
                del _properties[key]["enum"]

        return _properties

