=============
Predavanja 07
=============


Alternativni pristupi u paralelizaciji proračuna
================================================

- ``concurrent.futures`` biblioteka, tj. futures/promises execution pattern

  - prednosti i mane u odnosu na ``multiprocessing.Pool.imap`` i ``multiprocessing.Pool.imap_unordered``

Benchmarking
------------

- izmeriti ponasanje svih programa za razlicite scenarije ``--max-num`` in ``[10, 100, 1000, 10000]``

Use case: Matrica ko-faktora i njihovih prostih brojeva [nastavak]
------------------------------------------------------------------

- sekvencijalno resenje:

  - ``seq.py``: sekvencijalno resenje, optimizovano upotrebom generator/iterator protokola

- sekvencijalno resenje + memoizacija:

  - ``seq_memo.py``: optimizacija sekvencijalnog resenja, pre bilo kakvih pokretanja proracuna kesira sve proste brojeve do ``max_num**2 + 1``

- paralelizovano resenje, via ``concurrent.futures.ThreadPoolExecutor.map``

  - ``thr_map_v1.py``: osnovno paralelizovano resenje, default ``chunksize``
  - ``thr_map_v2.py``: "optimizacija" prethodnog resenja, ``chunksize`` param too small
  - ``thr_map_v3.py``: "optimizacija" prethodnog resenja, ``chunksize`` param too big
  - ``thr_map_v4.py``: "optimizacija" prethodnog resenja, try to *guess*timate the optimal chunk size

- paralelizovano resenje, via ``concurrent.futures.ProcessPoolExecutor.map``

  - ``proc_map_v1.py``: osnovno paralelizovano resenje, default ``chunksize``
  - ``proc_map_v2.py``: "optimizacija" prethodnog resenja, ``chunksize`` param too small
  - ``proc_map_v3.py``: "optimizacija" prethodnog resenja, ``chunksize`` param too big
  - ``proc_map_v4.py``: "optimizacija" prethodnog resenja, try to *guess*timate the optimal chunk size

- paralelizovano resenje, via ``concurrent.futures.ProcessPoolExecutor.submit``

  - ``proc_sub.py``: osnovno paralelizovano resenje, direktno kreira po jedan ``Futures`` objekat sa svaku iteraciju
