"""
cd /mnt/back/backhome/rm-permanent/code/uda_cloud_native
source uda/bin/activate

cd /mnt/back/backhome/rm-permanent/code/uda_cloud_native/nd064_course_1/solutions/python-helloworld
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def hello():
    return jsonify {
        OKi : "healthy"
    }, 200

@app.route("/metrics")
def hello():
    return jsonify {
        UserCount: 140, 
        UserCountActive: 23}
    }, 200




"""
Extend the Python Flask application with 
/status and 
/metrics endpoints, considering the following requirements:

    Both endpoints should return an HTTP 200 status code
    Both endpoints should return a JSON response 
    e.g. {"user": "admin"}. (Note: the JSON response can be hardcoded at this stage)
    The /status endpoint should return a response similar to this example: result: OK - healthy
    The /metrics endpoint should return a response similar to this example: data: {UserCount: 140, UserCountActive: 23}


"""






if __name__ == "__main__":
    app.run(host='0.0.0.0')




