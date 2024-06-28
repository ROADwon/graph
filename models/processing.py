# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import mpl_toolkits.mplot3d as plt3d
#
# class processing:
#     def load_file (file_path, file_type):
#         if file_type == "CSV":
#             data = pd.read_csv(file_path)
#         elif file_type =="TXT":
#             data = pd.read_csv(file_path,  sep="\t")
#         return data
#
#     def preprocessing_file(file):
#         if file.isnull().sum().sum() > 0:
#             file = file.dropna()
#         return file
#
#         ## select_file_type function will be used to more file types
#     def select_file_type(value):
#         global f_type
#         if value == "IMU":
#             f_type = 0
#         elif value == "GPS":
#             f_type = 1
#         elif value == "Zyro":
#             f_type = 2
#         elif value == "Encoder":
#             f_type = 3
#         else :
#             f_type = 4
#
#         return f_type
#
#     def plot_data_IMU(data):
#         df = data[["Robot.X", "Robot.Y", "Robot.Z"]]
#         # fig = plt.figure()
#         # ax = fig.add_subplot(111, projection='3d')
#         # ax.scatter(df["Robot.X"], df["Robot.Y"], df["Robot.Z"])
#         # ax.set_xlabel('X Label')
#         # ax.set_ylabel('Y Label')
#         # ax.set_zlabel('Z Label')
#         # plt.show()
#         return df["Robot.X"].values.tollist(), df["Robot.Y"].values.tollist(), df["Robot.Z"].values.tollist()
