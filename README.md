# Cleaning and Retrieving Occupational Codes

This is a branch addressing some bug issues when importing and using the 'occupationalcode' package. It creates a program that exports Job Codes on CSV format after applying a comprehensive text cleaning function over variables in the data.

The program included here is based on the algorithm originally written by Jyldyz Djumalieva, `Arthur
Turrell <http://aeturrell.github.io/home>`, David Copple, James
Thurgood, and Bradley Speigner; and upon the efficiency changes made by  `Martin Wood <MartinWoodONS.github.io>`. 

## Aim

Create a dataset exporting a UK 3-digit standard occupational classification (SOC), given a job title, job description, and job sector.

The algorithm uses the **SOC 2010** standard, more details of which can
be found on `the ONS'
website <https://www.ons.gov.uk/methodology/classificationsandstandards/standardoccupationalclassificationsoc/soc2010>`.


## Changes

   -Addresses debugging and installation issues when running from terminal. 

   -Fix debugging issues when importing datasets in format different from .csv (like .dta)

   -Creation of requirement file to import necessary packages to run the algorithm smoothly

   -Creation of program that exports SOCcode into a .csv file after aplying an extensive text cleaning function that addresses issues related to HTML text encoding.

   -User-friendly syntaxis; just need to provide the necessary arguments for input and output datasets.

   -Flexibility on variable names for job_description, job_title and job_sector to apply the function.


## Installation via terminal

1. Clone this repository on your desired root folder. Open terminal and set path


2. Creating and activating a virtual environment is recommended in the terminal

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

Then execute set up of the package in termina:

```cmd
    python setup.py sdist
    cd sdist
    pip install occupationcoder-<version>.tar.gz
```


The first line creates the .tar.gz file, the second navigates to the
directory with the packaged code in, and the third line installs the
package. The version number to use will be evident from the name of the
.tar.gz file.


And install extra dependencies in root folder after establishing path, as follows:
```cmd
    cd <path repo>
    pip install -r requirements.txt
```

## How to use program:

After the installation in the terminal; user just needs to execute
```cmd
    python new_main.py <input_file_path> <output_file_path> <title_column> <sector_column> <description_column>
```

Where title_column, sector_column and description_column are optional. If these arguments are not included, the default values will be 'job_title', 'job_sector' and 'job_description' respectively.

The output file will be accesible in the specified path and it will be a new dataframe with SOC code entries appended in a new column. 

Necessary to provide the path for input dataset with text and the desired path for output dataset


File and folder description
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``cleaning-retrieving-occ-code/occupationcoder/coder.py`` applies SOC codes to job descriptions
-  ``cleaning-retrieving-occ-code/occupationcoder/cleaner.py`` contains helper function which mostly
   manipulate strings
-  `cleaning-retrieving-occ-code/`occupationcoder/createdictionaries`` turns the ONS' index of SOC
   code into dictionaries used by ``occupationcoder/coder.py``
-  ``cleaning-retrieving-occ-code/occupationcoder/dictionaries`` contains the dictionaries used by
   ``cleaning-retrieving-occ-code/occupationcoder/coder.py``
-  ``cleaning-retrieving-occ-code/occupationcoder/outputs`` is the default output directory
-  ``cleaning-retrieving-occ-code/occupationcoder/tests/test_vacancies.csv`` contains 'test' vacancies 
   to run the code on, used by unittests, accessible by you!
-  ``cleaning-retrieving-occ-code/occupationcoder/new_main_.py`` is the main script to run the program 


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


