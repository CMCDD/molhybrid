#!/usr/bin/env python3

from rdkit import Chem
from rdkit.Chem import AllChem, rdDistGeom
import random
from queue import Queue
from threading import Thread

class MoleculeOptimizer:
    def __init__(self, molecules, num_threads=8):
        self.molecules = molecules
        self.num_threads = num_threads
        self.input_queue = Queue()
        self.results_queue = Queue()
        self.threads = []

    def optimize_structure(self, mol):
        try:
            mol = Chem.AddHs(mol)
            embed = AllChem.EmbedMolecule(mol, maxAttempts=200)
            error = False

            if embed == -1:
                embed = AllChem.EmbedMolecule(mol, useRandomCoords=True, maxAttempts=2000, enforceChirality=False)
            
            if embed == -1:
                confs = rdDistGeom.EmbedMultipleConfs(mol, numConfs=20, maxAttempts=2000, enforceChirality=False, useRandomCoords=True)
                if len(confs) < 1:
                    confs = rdDistGeom.EmbedMultipleConfs(mol, numConfs=40, maxAttempts=2000, enforceChirality=False, useRandomCoords=True)
                if len(confs) < 1:
                    confs = rdDistGeom.EmbedMultipleConfs(mol, numConfs=60, maxAttempts=2000, enforceChirality=False, useRandomCoords=True)
                if len(confs) >= 1:
                    AllChem.UFFOptimizeMolecule(mol, confId=random.randint(0, len(confs) - 1), maxIters=500)
                else:
                    error = True
            else:
                AllChem.UFFOptimizeMolecule(mol, maxIters=500)
        
        except BaseException as e:
            print('Failed:', e)
            error = True
        
        if error:
            print('Failed: Unable to embed molecule')
        
        return mol
    
    class SimulationThread(Thread):
        def __init__(self, input_queue, results_queue, optimizer):
            super().__init__()
            self.input_queue = input_queue
            self.results_queue = results_queue
            self.optimizer = optimizer
        
        def run(self):
            for data in iter(self.input_queue.get, "STOP"):
                mol = self.optimizer.optimize_structure(data)
                self.results_queue.put(mol)
    
    def run_optimization(self):
        # Populate queue with molecules
        for mol in self.molecules:
            self.input_queue.put(mol)
        
        # Start threads
        for _ in range(self.num_threads):
            thread = self.SimulationThread(self.input_queue, self.results_queue, self)
            thread.start()
            self.threads.append(thread)
        
        # Stop threads when done
        for _ in range(self.num_threads):
            self.input_queue.put("STOP")
        
        for thread in self.threads:
            thread.join()
        
        # Collect results
        optimized_molecules = []
        while not self.results_queue.empty():
            optimized_molecules.append(self.results_queue.get())
        
        return optimized_molecules
