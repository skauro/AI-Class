Näite väljund : Solution for 8-Queens: [5, 3, 6, 0, 2, 4, 1, 7]

 .  .  .  Q  .  .  .  .
 .  .  .  .  .  .  Q  . 
 .  .  .  .  Q  .  .  . 
 .  Q  .  .  .  .  .  . 
 .  .  .  .  .  Q  .  . 
 Q  .  .  .  .  .  .  . 
 .  .  Q  .  .  .  .  . 
 .  .  .  .  .  .  .  Q 


Kasutan randomizationit alguses asetamiseks ja kui ei suuda 1000 sammuga ära lahendada
siis teen uue random asetamise, Seda kordan kuni max 50 korda. 

Väiksemate suuruste laudadega toimib ilusti aga minnes 100 poole läheb lahendusel juba liiga kaua aega.

Väikesed lauad lahendab kõik ära, suuremad võtavad liiga kaua.

Testisin kuni 50ni ja need korrad mis testisin sai kõik hakkama.
Testisin ka 100ga aga võttis liiga kaua ning pole kindel kas seda enam suudab.
Niiet 50ni on 100% lahendamise võimalus.(Vähemalt nendel test caseidel.)
Kuigi kui ta korra juba lahendab suudab ta 50randomiga sama lahenduse peale tulla küll.
