=============
Predavanja 02
=============


Podsetnik za list comprehension, razliciti nacini iteracije kroz podatke
========================================================================

Klasična iteracija::

    results = []
    for x in data:
        if x % 2 == 0:
            results.append(x)

List comprehension::

    [x for x in data if x % 2 == 0]

Funkcionalno programiranje, putem ``filter`` funkcije::

    list(filter(lambda x: x % 2 == 0, data))
