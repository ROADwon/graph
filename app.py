from flask import Flask, request, render_template, jsonify
from flask_restx import Api, Resource
import pandas as pd
from controller.index import index as index_controller

app = Flask(__name__)
api = Api(app, version='1.0', title='File Processing API',
          description='A simple API for uploading and processing files')

ns = api.namespace('files', description='File operations')

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type='FileStorage', required=True)
upload_parser.add_argument('file_type', type=str, required=True, help='Type of the file (CSV or TXT)')


class Processing:
    @staticmethod
    def load_file(file, file_type):
        if file_type.upper() == "CSV":
            data = pd.read_csv(file)
        elif file_type.upper() == "TXT":
            data = pd.read_csv(file, sep="\t")
        return data

    @staticmethod
    def preprocessing_file(data):
        if data.isnull().sum().sum() > 0:
            data = data.dropna()
        return data

    @staticmethod
    def extract_imu_data(data):
        df = data[["Robot.X", "Robot.Y", "Robot.Z"]]
        return df["Robot.X"].values.tolist(), df["Robot.Y"].values.tolist(), df["Robot.Z"].values.tolist()


@app.route("/upload")
def upload_file():
    return render_template("upload.html")

@ns.route("/upload")
class FileUpload(Resource):
    @api.expect(upload_parser)
    def post(self):
        file = request.files["file"]
        file_type = request.form["file_type"]
        data = Processing.load_file(file, file_type)
        data = Processing.preprocessing_file(data)
        x, y, z = Processing.extract_imu_data(data)
        return jsonify(x=x, y=y, z=z)

app.add_url_rule('/index', 'index', index_controller)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
