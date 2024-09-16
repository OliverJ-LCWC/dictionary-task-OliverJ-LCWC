def task(input): # the value of input is an integer which is the total money available

    result = {
        "needs": (input * 0.5),
        "wants": (input * 0.3),
        "savings": (input * 0.2)
    }

    # Code here...

    return result # result should be a dictionary wiht the correct values

print(task(1032))