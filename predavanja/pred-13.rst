=============
Predavanja 13
=============


Uvod u distribuirane proračune [nastavak]
=========================================

Celery workflow, tj. taskovi višeg reda
---------------------------------------

- ``group``: distribuirana ``for``-petlja
- ``chain``: uvezivanje više taskova, tako da se distribuirano izvršavaju jedan za drugim
- ``chord``: ``group`` + "reduktor" task (nad rezultatima cele te grupe)

Use case: Matrica ko-faktora i njihovih prostih brojeva
-------------------------------------------------------

- prepravka naših postojećih rešenja ovog problema u distribuirano rešenje

  - rešenje iz prethodne godine https://github.com/petarmaric/pdaj-predavanja-beleske/tree/2020/materijali/pred-10
