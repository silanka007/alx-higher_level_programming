#!/usr/bin/python3
"""this module contain the add_attribute function"""


def add_attribute(class_obj, attr_name, attr_value):
    """
    Add a new attribute to an object if possible.
    Args:
        class_obj (any): The object to add an attribute to.
        attr_name (str): The name of the attribute to add to obj.
        attr_value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(class_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(class_obj, attr_name, attr_value)
