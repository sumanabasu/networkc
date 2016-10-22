networkc
====

Network Library to calculate degree, closeness, betweenness centrality and sorts them in descending order

* Calculate Degree Centality
* Calculate Closeness Centrality
* Calculate Betweenness Centrality

This library -

1. Calculates one or more centrality measures from the above list
2. Sorts them in descending order of centrality
3. Saves the node ids and corresponding centrality measure in a csv


##Testing Instructions

To test this library use the following command on terminal :
`python networkc/networkc.test.py`

##Command Line Instructions

* `-d` `--degree`
   Choose this option to calculate degree centrality
   Default Value = "False"

* `-c` `--closeness`
   Choose this option to calculate closeness centrality
   Default Value = "False"

* `-b` `--degree`
   Choose this option to calculate betweenness centrality
   Default Value = "False"

##Example

* `networkc -d -c -b edges.csv`

##Output Format

For each centrality measure, output will be a two column table:

| Node ID | Centrality Measure |
