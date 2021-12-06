from flask import app

import main as ns


@app.route("/unittest")
def unittest():
    item_dict = {}
    if (ns.distance([0, 3], [0, 4]) == 1 and ns.distance([5, 3], [1, 3]) == 4 and ns.distance([5, 4], [1,1]) == 5 and ns.distance(
            [4, 0], [1, 0]) == 3):
        print("Unit test passed")
        item_dict.update({"unit test": "passed"})
        return item_dict
    else:
        print("unit test failed")
        item_dict.update({"unit test": "failed"})
        return item_dict
