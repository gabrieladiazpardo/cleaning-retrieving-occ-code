# Cleaning and Retrieving Occupational Codes

This is a branch created based on the code originally written by Jyldyz Djumalieva, `Arthur
Turrell <http://aeturrell.github.io/home>`__, David Copple, James
Thurgood, and Bradley Speigner; and upon the efficiency changes made by Martin Wood <http://MartinWoodONS.github.io>

Aim:  Given a job title, job description, and job sector the algorithm assigns
a UK 3-digit standard occupational classification (SOC) code to the job.
The algorithm uses the **SOC 2010** standard, more details of which can
be found on `the ONS'
website <https://www.ons.gov.uk/methodology/classificationsandstandards/standardoccupationalclassificationsoc/soc2010>`__.


CHANGES:
    .Fixes debugging problems when importing values from a dataset
    .Includes file of package requirements
    .Comprehensive cleaning program over job description, job title and job sector, inclufing cleaning features for HTML text 
    .Replicability for any arguments for input and output data
    .Flexibility on any variable names for job description, job title and job sector


## Installation via terminal

First of all, clone this repo and navigate to the root folder.

Creating and activating a virtual environment is recommended:

### Windows:
```cmd
    pip install virtualenv
    python -m venv venv
    venv/Scripts/activate
```

### Mac:
```cmd
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
```

Then execute:

```cmd
    python setup.py sdist
    cd sdist
    pip install occupationcoder-<version>.tar.gz
```


The first line creates the .tar.gz file, the second navigates to the
directory with the packaged code in, and the third line installs the
package. The version number to use will be evident from the name of the
.tar.gz file.


And install extra dependencies in root folder as follows:
```cmd
    cd ..
    pip install -r requirements.txt
```

## How to use:

After the installation you can open a terminal and execute next command:
```cmd
    python main.py <input_file_path> <output_file_path> <title_column> <sector_column> <description_column>
```

Where title_column, sector_column and description_column are optional. If these arguments are not included, the default values will be 'job_title', 'job_sector' and 'job_description' respectively.

The output file will be accesible in the specified path and it will be a new dataframe with SOC code entries appended in a new column.


Pre-requisites
~~~~~~~~~~~~~~

occupationcoder is built on top of `NLTK <http://www.nltk.org/>`__ and
uses 'Wordnet' (a corpora, number 82 on their list) and the Punkt
Tokenizer Models (number 106 on their list). When the coder is run, it
will expect to find these in their usual directories. If you have nltk
installed, you can get them corpora using ``nltk.download()`` which will
install them in the right directories or you can go to
`http://www.nltk.org/nltk_data/ <http://www.nltk.org/nltk_data/>`__ to
download them manually (and follow the install instructions).


File and folder description
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``occupationcoder/coder.py`` applies SOC codes to job descriptions
-  ``occupationcoder/cleaner.py`` contains helper function which mostly
   manipulate strings
-  ``occupationcoder/createdictionaries`` turns the ONS' index of SOC
   code into dictionaries used by ``occupationcoder/coder.py``
-  ``occupationcoder/dictionaries`` contains the dictionaries used by
   ``occupationcoder/coder.py``
-  ``occupationcoder/outputs`` is the default output directory
-  ``occupationcoder/tests/test_vacancies.csv`` contains 'test' vacancies 
   to run the code on, used by unittests, accessible by you!



---------------------------------------------------------------------------------------

This code originally written by Jyldyz Djumalieva, `Arthur
Turrell <http://aeturrell.github.io/home>`__, David Copple, James
Thurgood, and Bradley Speigner. If you use this code please cite:

Turrell, A., Speigner, B., Djumalieva, J., Copple, D., & Thurgood, J.
(2019). `Transforming Naturally Occurring Text Data Into Economic
Statistics: The Case of Online Job Vacancy
Postings <https://www.nber.org/papers/w25837>`__ (No. w25837). National
Bureau of Economic Research.

::

    @techreport{turrell2019transforming,
      title={Transforming naturally occurring text data into economic statistics: The case of online job vacancy postings},
      author={Turrell, Arthur and Speigner, Bradley and Djumalieva, Jyldyz and Copple, David and Thurgood, James},
      year={2019},
      institution={National Bureau of Economic Research}
    }

* Documentation: https://occupationcoder.readthedocs.io.


