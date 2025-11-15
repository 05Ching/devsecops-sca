def greet(name="world"):
    try:
        print(f"hello, {name}")
    except Exception as e:
        print(f"error: {e}")


greet()
