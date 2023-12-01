from flask import Flask,request,render_template,jsonify
from encode import encode_dataframe
from handle_null import handle_null_val
from load_data import load_dataframe
from remove_skew import rem_skew
from scale import scale_df
from dimension_reduction import apply_pca
import datetime
import seaborn as sns

import os
app=Flask(__name__)

@app.route('/home',methods=["GET","POST"])
def home_page():
    return render_template("index.html")

@app.route("/get_data",methods=["GET","POST"])
def transform_data():
    data=request.files["file"]
    print(data.filename)
    file_name=data.filename
    dataframe=load_dataframe(file_name)
    print(dataframe.head(3))
    df=handle_null_val(dataframe)
    print(df.head(3))
    encoded_dataframe=encode_dataframe(df)
    print(encoded_dataframe.head(3))
    df_skewed=rem_skew(encoded_dataframe)
    print(df_skewed.head(3))
    scaled_dataframe=scale_df(df_skewed)
    print(scaled_dataframe.head(3))
    reduced_df=apply_pca(scaled_dataframe)
    print(reduced_df.head(3))
    reduced_df.to_csv(r"C:\Users\ADITI GUPTA\Desktop\project_1\output_data\{filename}.csv".format(filename=file_name),index=False)
    return 'Data Transformation is done'

if __name__=="__main__":
    app.run(debug=True,port=8080)