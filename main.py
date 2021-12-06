from flask import Flask, request
import math

app = Flask(__name__)


def distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


@app.route('/bestnetworkstation', methods=['POST'])
def root():
    item_dict = {}
    request_json_data = request.get_json(force=True)
    ns = request_json_data['ns']
    d = request_json_data['d']

    '''# ns represents  x and y of Network stations at reach
    ns = [[0, 0, 9], [20, 20, 6], [10, 0, 12], [5, 5, 13], [99, 25, 2]]
    d = [[0, 0], [100, 100], [15, 10], [18, 18], [13, 13], [25, 99]]'''

    maxspeed = 0
    point = {}
    o = 0
    bestnetworkstationpoint = ""
    bestdevicepoint = ""
    for i in range(len(d)):
        point[str(d[i][0]) + "," + str(d[i][1])] = []
        for j in range(len(ns)):

            dis = math.sqrt(((ns[j][0] - d[i][0]) ** 2) + ((ns[j][1] - d[i][1]) ** 2))

            if dis > ns[j][2]:

                point[str(d[i][0]) + "," + str(d[i][1])].append(ns[j][2])

                speed = 0
            else:

                speed = pow((ns[j][2] - dis), 2)
                o = 1
                if maxspeed < speed:
                    maxspeed = speed
                    bestnetworkstationpoint = str(ns[j][0]) + "," + str(ns[j][1])
                    bestdevicepoint = str(d[j][0]) + "," + str(d[j][1])
    print("")
    if o == 1:
        print("Best network station for point ", end="")
        print(bestdevicepoint.split(",")[0], ",", bestdevicepoint.split(",")[1], end="")
        print(" is", bestnetworkstationpoint.split(",")[0], ",", bestnetworkstationpoint.split(",")[1], "with speed",
              maxspeed)
        st = ""
        st = st + "Best network station for point " + bestdevicepoint.split(",")[0] + "," + bestdevicepoint.split(",")[
            1] + " is" + bestnetworkstationpoint.split(",")[0] + "," + bestnetworkstationpoint.split(",")[
                 1] + " with speed " + str(maxspeed)
        item_dict.update({"networkspeed": st})
    else:
        print("No Best Network with speed")
        item_dict.update({"networkspeed": "No Best Network with speed"})
    st1 = ""
    for i in point:
        if len(point[i]) > 0:
            for k in range(len(point[i])):
                print("No network station within recach", point[i][k], "for point", i.split(",")[0], ",",
                      i.split(",")[1])
                st1 = st1 + "No network station within recach" + str(point[i][k]) + "for point" + i.split(",")[
                    0] + "," + i.split(",")[1] + "\n"
    item_dict.update({"nonetworkstation": st1})
    return item_dict


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
