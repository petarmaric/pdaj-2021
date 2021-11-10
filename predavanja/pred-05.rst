=============
Predavanja 05
=============


Uvod u paralelizaciju proračuna [nastavak]
==========================================

Benchmarking
------------

- izmeriti ponasanje svih programa za razlicite scenarije ``--max-num`` in ``[10, 100, 1000, 10000]``

Use case: Matrica ko-faktora i njihovih prostih brojeva [nastavak]
------------------------------------------------------------------

- sekvencijalno resenje:

  - ``seq.py``: sekvencijalno resenje, optimizovano upotrebom generator/iterator protokola

- paralelizovano resenje, via ``multiprocessing.Pool.map``

  - ``map_v1.py``: osnovno paralelizovano resenje, default ``chunksize``
  - ``map_v2.py``: "optimizacija" prethodnog resenja, ``chunksize`` param too small
  - ``map_v3.py``: "optimizacija" prethodnog resenja, ``chunksize`` param too big
  - ``map_v4.py``: "optimizacija" prethodnog resenja, try to *guess*timate the optimal chunk size

- paralelizovano resenje + optimizovano upotrebom generator/iterator protokola, via ``multiprocessing.Pool.imap``

  - ``imap_v1.py``: osnovno paralelizovano resenje, default ``chunksize``
  - ``imap_v2.py``: "optimizacija" prethodnog resenja, ``chunksize`` param too small
  - ``imap_v3.py``: "optimizacija" prethodnog resenja, ``chunksize`` param too big
  - ``imap_v4.py``: "optimizacija" prethodnog resenja, try to *guess*timate the optimal chunk size
  - ``imap_v5.py``: "optimizacija" prethodnog resenja, try to *better* guesstimate the optimal chunk size

- paralelizovano resenje + optimizovano upotrebom generator/iterator protokola + unordered rezultati, via ``multiprocessing.Pool.imap_unordered``

  - ``imap_un_v1.py``: osnovno paralelizovano resenje, default ``chunksize``
  - ``imap_un_v2.py``: "optimizacija" prethodnog resenja, ``chunksize`` param too small
  - ``imap_un_v3.py``: "optimizacija" prethodnog resenja, ``chunksize`` param too big
  - ``imap_un_v4.py``: "optimizacija" prethodnog resenja, try to *guess*timate the optimal chunk size
  - ``imap_un_v5.py``: "optimizacija" prethodnog resenja, try to *better* guesstimate the optimal chunk size

- ``imap`` vs ``imap_unordered``:

  - kad ima smisla koristiti ``imap_unordered``?
  - jos bolje receno, kada se uopste *sme koristiti*?!?

- sekvencijalno resenje + memoizacija:

  - ``seq_memo.py``: optimizacija sekvencijalnog resenja, pre bilo kakvih pokretanja proracuna kesira sve proste brojeve do ``max_num**2 + 1``
