import networkx as nx
import pandas as pd
import operator
import matplotlib.pyplot as plt
import argparse

def readGraph(csv_file):
    df = pd.read_csv(csv_file)
    l = []
    for i, row in df.iterrows():
        r = str(row['Source']) + " " + str(row['Target'])
        l.append(r)
    G = nx.parse_edgelist(l, nodetype=str)
    return G

def rev(dc):
    sorted_x = reversed(sorted(dc.items(), key=operator.itemgetter(1)))
    x = list(sorted_x)
    return pd.DataFrame(x)

def calcCentrality(G, d, c, b):
    if d == True:
        dcD = rev(nx.degree_centrality(G))
    if c == True:
        dcC = rev(nx.closeness_centrality(G))
    if b == True:
        dcB = rev(nx.betweenness_centrality(G))
    return dcD, dcC, dcB

def writetoCSV(d, c, b, dcD, dcC, dcB):
    if d == True:
        print "Degree Centrality :"
        print dcD.to_csv(index=False, header=False)
    if c == True:
        print "Closeness Centrality :"
        print dcD.to_csv(index=False, header=False)
    if b == True:
        print "Betweenness Centrality :"
        print dcB.to_csv(index=False, header=False)


def main():
    parser = argparse.ArgumentParser(description='Graph Centrality')
    parser.add_argument('-d', '--degree', help="Enter -d to calculate degree centrality", action='store_true')
    parser.add_argument('-c', '--closeness', help="Enter -c to calculate closeness centrality", action='store_true')
    parser.add_argument('-b', '--betweenness', help="Enter -b to calculate betweenness centrality", action='store_true')
    parser.add_argument('file', type=str, help="Enter the file name with path information")
    arg = parser.parse_args()

    G = readGraph(arg.file)
    dcD, dcC, dcB = calcCentrality(G, arg.degree, arg.closeness, arg.betweenness)

    writetoCSV(arg.degree, arg.closeness, arg.betweenness, dcD, dcC, dcB)

if __name__ == "__main__":
    main()