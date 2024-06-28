# from processing import *
# from flask import Flask, render_template, request
#
# app = Flask(__name__)
# @app.route("/")
# def upload_file():
#     return render_template("upload.html")
#
# @app.route("/uploader", metho= ['POST'])
# class report:
#     def upload_file_post():
#         if request.method =="POST":
#             file = request.files["file"]
#             file_type=request.form["file_type"]
#             data = processing.load_file(file_path = file, file_type = file_type)
#             data = processing.preprocessing_file(data)
#             img = processing.plot_data_IMU(data)
#
#             return send_file(img, mimetypes="image/png")
