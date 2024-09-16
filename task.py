def task(input): # the value of input is an integer which is the total money available

    result = {
        "Needs": (input * 0.5),
        "Wants": (input * 0.3),
        "Savings": (input * 0.2)
    }

    # Code here...

    return result # result should be a dictionary wiht the correct values