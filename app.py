from flask import Flask, request, jsonify
from main import main

app = Flask(__name__)

@app.route('/getScoreData/<fromDate>/<toDate>/<league>', methods=['GET'])
def getAcmeSportData(fromDate, toDate, league):
    print(fromDate,toDate,league)
    result = main(fromDate, toDate, league)
    data = {'data': result}
    return jsonify(data)

if __name__ == "__main__":
    app.run()
