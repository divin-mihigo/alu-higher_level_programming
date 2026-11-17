# python-inheritance

This directory contains Python scripts that practice inheritance: using
`dir`, subclassing built-in types, checking classes with `type`,
`isinstance` and `issubclass`, and building a class hierarchy
(`BaseGeometry` -> `Rectangle` -> `Square`).

## Files

| File | Description |
| ---- | ----------- |
| `0-lookup.py` | Returns the attributes and methods of an object |
| `1-my_list.py` | `MyList`, a `list` subclass with `print_sorted` |
| `2-is_same_class.py` | True if an object is exactly an instance of a class |
| `3-is_kind_of_class.py` | True if an object is an instance of a class or a subclass |
| `4-inherits_from.py` | True if an object is an instance of a subclass only |
| `5-base_geometry.py` | Empty class `BaseGeometry` |
| `6-base_geometry.py` | `BaseGeometry` with an unimplemented `area` |
| `7-base_geometry.py` | `BaseGeometry` with `integer_validator` |
| `8-rectangle.py` | `Rectangle` with validated private width and height |
| `9-rectangle.py` | `Rectangle` with `area` and a description |
| `10-square.py` | `Square` inheriting from `Rectangle` |
| `11-square.py` | `Square` with its own description |
| `tests/1-my_list.txt` | Doctests for `1-my_list.py` |
| `tests/7-base_geometry.txt` | Doctests for `7-base_geometry.py` |

## Tests

```
python3 -m doctest -v ./tests/1-my_list.txt
python3 -m doctest -v ./tests/7-base_geometry.txt
```

## Requirements

- Python 3 (interpreter `/usr/bin/python3`)
- Files start with `#!/usr/bin/python3` and are executable
- No modules are imported
- Modules, classes and functions are documented
- Code follows the PEP8 style (`pycodestyle`)
