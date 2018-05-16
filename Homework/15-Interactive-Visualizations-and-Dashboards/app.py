
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float


# In[2]:


from flask_sqlalchemy import SQLAlchemy
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from sqlalchemy.orm import Session

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///belly_button_biodiversity.sqlite"
db = SQLAlchemy(app)


# In[3]:


engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")


# In[4]:



# In[5]:


Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)


# In[6]:


OTU = Base.classes.otu
Samples = Base.classes.samples
MD = Base.classes.samples_metadata


# In[7]:


@app.route("/")
def home():
    return render_template("index.html")


# In[8]:


@app.route("/names")
def names():
    
    """List of sample names.

    Returns a list of sample names in the format
    [
        "940",
        "941",
        "943",
        "944",
        "945",
        "946",
        "947",
        ...
    ]

    """
    
    results = db.session.query(MD.SAMPLEID).all()
    results = list(np.ravel(results))
    results = list(map(str, results))
    return jsonify(results)


# In[9]:


@app.route("/otu")
def otu():
    
    """List of OTU descriptions.

    Returns a list of OTU descriptions in the following format

    [
        "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
        "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
        "Bacteria",
        "Bacteria",
        "Bacteria",
        ...
    ]
    """
    results = db.session.query(OTU.lowest_taxonomic_unit_found).all()
    results = list(np.ravel(results))
    return jsonify(results)


# In[10]:


@app.route('/metadata/<int:sample>')
def meta(sample):
    
    """MetaData for a given sample.

    Args: Sample in the format: `940`

    Returns a json dictionary of sample metadata in the format

    {
        AGE: 24,
        BBTYPE: "I",
        ETHNICITY: "Caucasian",
        GENDER: "F",
        LOCATION: "Beaufort/NC",
        SAMPLEID: 940
    }
    """
    req = db.session.query(MD.SAMPLEID).all()
    ravel = list(np.ravel(req))
    if sample in ravel:
        results = db.session.query(MD.AGE, MD.BBTYPE, MD.ETHNICITY, MD.GENDER, MD.LOCATION, MD.SAMPLEID).            filter(MD.SAMPLEID == sample).all()
        df = pd.DataFrame(results, columns = ["AGE", "BBTYPE", "ETHNICITY", "GENDER", "LOCATION", "SAMPLEID"])
        return jsonify(df.to_dict(orient="records"))


# In[11]:


@app.route('/wfreq/<int:sample>')
def wash(sample):
    """Weekly Washing Frequency as a number.

    Args: Sample in the format: `940`

    Returns an integer value for the weekly washing frequency `WFREQ`
    """
    req = db.session.query(MD.SAMPLEID).all()
    ravel = list(np.ravel(req))
    if sample in ravel:
        results = db.session.query(MD.WFREQ).            filter(MD.SAMPLEID == sample).all()
        return jsonify(int(np.ravel(results)))


# In[12]:


@app.route('/samples/<int:sample>')
def values(sample):
    
    """OTU IDs and Sample Values for a given sample.

    Sort your Pandas DataFrame (OTU ID and Sample Value)
    in Descending Order by Sample Value

    Return a list of dictionaries containing sorted lists  for `otu_ids`
    and `sample_values`

    [
        {
            otu_ids: [
                1166,
                2858,
                481,
                ...
            ],
            sample_values: [
                163,
                126,
                113,
                ...
            ]
        }
    ]
    """
    req = db.session.query(MD.SAMPLEID).all()
    ravel = list(np.ravel(req))
    if sample in ravel:
        results = engine.execute("select otu_id, BB_%s from samples" % sample).fetchall()
        df = pd.DataFrame(results, columns = ["otu_ids", "sample_values"])
        df.sort_values(by="sample_values", ascending = False, inplace = True)
        new_dict = df.to_dict(orient="list")
        return jsonify(new_dict)

if __name__ == "__main__":
    app.run()