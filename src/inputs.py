#!/usr/bin/env python3
def read_linker(filename):
    with open(filename, 'r') as file:
        linkers = []

        for line in file:
            if line.startswith('#l') or line.startswith('#L'):
                words = line.split()
                linkers.append(words[1])

    return linkers


def read_pharmacophores(filename):
    with open(filename, 'r') as file:
        pharms = []

        for line in file:
            if line.startswith('#P') or line.startswith('#p'):
                words = line.split()
                pharms.append(words[1])

    return pharms


def input_molecules(filename):
    p = read_pharmacophores(filename)
    l = read_linker(filename)
    return l + p,len(l)


def read_parameters(filename):
    with open(filename, 'r') as file:
        

        for line in file:
            if line.startswith('#max_hybrids') or line.startswith('#Max_hybrids'):
                words = line.split()
                max_hybrids = words[2]
            if line.startswith('#max_asymble') or line.startswith('#Max_asymble'):
                words = line.split()
                max_asymble = words[2]
    
    return int(max_asymble),int(max_hybrids)
