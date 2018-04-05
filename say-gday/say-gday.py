def say_gday(name, age):
    """
        Hi!
    """
    # your code here
    return "Gday. My name is Alex and I'm 32 years old"


if __name__ == '__main__':
    assert say_hi("Alex", 32) == "Gday. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Gday. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')
