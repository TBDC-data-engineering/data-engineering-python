import inspect


def do_something(name: str) -> str:
    """
    This function does something.
    Args:
        name (str): The name of the person to do something with.
    Returns
        str: A string indicating what was done with the name.
    Raises:
        ValueError: If the name is "silvio".
    """
    if name == "silvio":
        raise ValueError("Silvio is not allowed to do this!")

    out_variable = f"Doing something...{name}"
    print(out_variable)
    return out_variable



# get docstring of the function
doc_string = inspect.getdoc(do_something)
print(doc_string)