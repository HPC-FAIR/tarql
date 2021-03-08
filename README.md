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

After that, just type 
```
cd sample-csv
make all
```

All RDF files will be generated from sample CSV files.

Reference output RDF files (.nt files) are stored under

./sample-csv/referenceOutput


## Lessons of Using this tool

CSV files need some preprocessing:
* remove space and special characters in column names. Or the parser will fail
* each row should already have a unique id for each record. Or you can add a new first column and use row id as the unique ID.


To encode unit information, we use structured values, i.e. value with unit information.
The units are provided by the QUDT ontologies. 

For example, to encode a product has a weight of 2.4 kilograms

```
# the value of the weight is a structured value with 3 fields
# type: qudt quantity value
# value: 2.4
# unit : kilo gram
exproduct:item10245 exterms:weight [ rdf:type qudt:QuantityValue ; 
                                     qudt:value "2.4"^^xsd:float;
                                     qudt:unit exunits:kilograms ] .
```



The generated file is .nt , notation3 or N3 syntax of RDF. 

https://rdf-translator.appspot.com/ can convert .nt file into json-ld or any other file formats.

The online convert needs Input to be selected as N3. Automatic recognition may not work.

 
