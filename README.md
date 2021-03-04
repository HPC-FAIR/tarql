# Tarql: SPARQL for Tables

Tarql is a command-line tool for converting CSV files to RDF using SPARQL 1.1 syntax. It's written in Java and based on Apache ARQ.

**See http://tarql.github.io/ for documentation.**

## Building

Get the code from GitHub: http://github.com/tarql/tarql

Tarql uses Maven. To create executable scripts for Windows and Unix in `/target/appassembler/bin/tarql`:

    mvn package appassembler:assemble

Otherwise it's standard Maven.

## Testing

There are a few sample csv files and the corresponding sparql configuration files.

First export path to tarql in your environment.

Just type 
```
cd sample-csv
make all
```

All RDF files will be generated from CSV files.

Reference output files are stored under

./sample-csv/referenceOutput


## Lessons of Using this tool

CSV files need some preprocessing:
* remove space and special characters in column names. Or the parser will fail
* each row should already have a unique id for each record. Or you can add a new first column and use row id as the unique ID.

The generated file is .nt , notation3 or N3 syntax of RDF. 

https://rdf-translator.appspot.com/ can convert .nt file into json-ld or any other file formats.

The online convert needs Input to be selected as N3. Automatic recognition may not work.

 
