from ansible.errors import AnsibleFilterError

def to_hcl(value, indent_level=0):
    indent = " " * (indent_level * 2)
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, list):
        if not value:
            return "[]"
        else:
            items = ",\n".join([f"{indent}  {to_hcl(item, indent_level+1)}" for item in value])
            return f"[\n{items}\n{indent}]"
    elif isinstance(value, dict):
        if not value:
            return "{}"
        elif all(key.startswith("_") for key in value.keys()):
            items = "\n".join([f"{indent}{to_hcl(val, indent_level)}" for val in value.values()])
            return f"{items}"
        else:
            items = "\n".join([f"{indent}  {key} = {to_hcl(val, indent_level+1)}" for key, val in value.items()])
            return f"{{\n{items}\n{indent}}}"
    else:
        raise AnsibleFilterError(f"Unsupported type: {type(value)}")

class FilterModule(object):
    def filters(self):
        return {'to_hcl': to_hcl}
