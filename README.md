# Cleaning and Retrieving OCC Codes

A tool to assign standard occupational classification codes to job vacancy descriptions. Based on <>

---------------------------------------------------------------------------------------

Given a job title, job description, and job sector the algorithm assigns
a UK 3-digit standard occupational classification (SOC) code to the job.
The algorithm uses the **SOC 2010** standard, more details of which can
be found on `the ONS'
website <https://www.ons.gov.uk/methodology/classificationsandstandards/standardoccupationalclassificationsoc/soc2010>`__.

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

Pre-requisites
~~~~~~~~~~~~~~

See `setup.py` for a full list of Python packages.

occupationcoder is built on top of `NLTK <http://www.nltk.org/>`__ and
uses 'Wordnet' (a corpora, number 82 on their list) and the Punkt
Tokenizer Models (number 106 on their list). When the coder is run, it
will expect to find these in their usual directories. If you have nltk
installed, you can get them corpora using ``nltk.download()`` which will
install them in the right directories or you can go to
`http://www.nltk.org/nltk_data/ <http://www.nltk.org/nltk_data/>`__ to
download them manually (and follow the install instructions).

A couple of the other packages, such as
`rapidfuzz <https://pypi.org/project/rapidfuzz/>`__ do not come
with the Anaconda distribution of Python. You can install these via pip
(if you have access to the internet) or download the relevant binaries
and install them manually.

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

## Installation via terminal

First of all, clone this repo and navigate to the root folder.

Creating and activating a virtual environment is recommended:

### Windows:
```cmd
    pip install virtualenv
    python -m venv venv
    venv/Scripts/activate
```

### UNIX:
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



Credits
-------

The development of this package was supported by the Bank of England.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
