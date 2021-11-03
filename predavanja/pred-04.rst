=============
Predavanja 04
=============


Uvod u paralelizaciju proračuna
===============================

- ``threading`` biblioteka, i problemi sa njom (Python green threads)
- ``multiprocessing`` biblioteka

Use case: Matrica ko-faktora i njihovih prostih brojeva
-------------------------------------------------------

- problem: 2D parameter sweep (kroz celobrojne koordinate ``x`` i ``y``) i provera da li je ``x * y + 1`` prost broj
- ``seq.py``: sekvencijalno resenje, optimizovano upotrebom generator/iterator protokola
- ``par_v1.py``: osnovno paralelizovano resenje, via ``multiprocessing.Pool.map``
- ``par_v2.py``: "optimizacija" prethodnog resenja, ``pool.map`` ``chunksize`` param too small
- ``par_v3.py``: "optimizacija" prethodnog resenja, ``pool.map`` ``chunksize`` param too big
- ``par_v4.py``: "optimizacija" prethodnog resenja, ``pool.map`` try to *guess*timate the optimal chunk size
