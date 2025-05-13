OMANIK - KAUR ANDRO ORGUSAAR

213461IACB



Kodutöö 1 : tulemused on +1 arvuga(loendan teisiti)

Tulemused kinnitavad, et A* on kõige efektiivsem algoritm suurte kaartide puhul. 
Kui eesmärk on lihtsalt leida mingi tee kiiresti, võib kasutada Greedy search'i.
BFS on ka efektiivne aga aeglasem.

Muidu oli väga lahe näha kuidas saab kasutada selliseid algorütme, tulemused kui jooksutan programmi : 
(Esimesed on testid etteantud lühikeste tabelite peal testimine)


BFS - Iterations: 202, Time: 0.0050s, Path length: 16
Greedy - Iterations: 16, Time: 0.0010s, Path length: 16
A* - Iterations: 16, Time: 0.0000s, Path length: 16
BFS - Iterations: 192, Time: 0.0020s, Path length: 32
Greedy - Iterations: 53, Time: 0.0019s, Path length: 32
A* - Iterations: 116, Time: 0.0021s, Path length: 32

Testing on cave300x300
BFS - Iterations: 47233, Time: 0.4311s, Path length: 555
Greedy - Iterations: 3358, Time: 0.0229s, Path length: 983
A* - Iterations: 8202, Time: 0.0608s, Path length: 555

Testing on cave600x600
BFS - Iterations: 197804, Time: 1.2761s, Path length: 1248
Greedy - Iterations: 6293, Time: 0.0538s, Path length: 1974
A* - Iterations: 60472, Time: 0.6485s, Path length: 1248

Testing on cave900x900
BFS - Iterations: 450414, Time: 3.4905s, Path length: 1844
Greedy - Iterations: 29496, Time: 0.2596s, Path length: 4130
A* - Iterations: 93999, Time: 1.0070s, Path length: 1844
