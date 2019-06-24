## Rekisteröitymätön käyttäjä

**Tuotteiden listaus**
+ Valitse 'Listaa tuotteet'
```SQL
SELECT * FROM product;
```

**Tuotteiden haku nimen perusteella**
+ Valitse 'Listaa tuotteet'
+ Täytä kenttään hakusana
+ Paina 'Hae'
```SQL
SELECT * FROM product
WHERE product.name LIKE :word
```

**Käyttäjän rekisteröinti**
+ Valitse 'Rekisteröidy'
+ Täytä nimi (5-50 merkkiä), käyttäjänimi (uniikki, 3-50 merkkiä) ja salasana (5-50 merkkiä)
+ Paina 'Luo tunnus'
+ Käyttäjälle kerrotaan jos rekisteröityminen epäonnistuu
```SQL
INSERT INTO account (name, username, password, email)
VALUES (?, ?, ?, ?);
```
## Rekisteröitynyt käyttäjä

**Kirjautuminen**
+ Valitse 'Kirjaudu'
+ Täytä käyttäjänimi ja salasana
+ Paina 'Kirjaudu sisään'
+ Käyttäjälle kerrotaan jos kirjautuminen epäonnistuu 
```SQL
SELECT * FROM account
WHERE account.usernme = ? AND account.password = ?;
```

**Salasanan vaihtaminen**
+ Valitse 'Vaihda salasana'
+ Täytä uusi salasana
+ Täytä uusi salasanan uudelleen
+ Paina 'Vaihda salasana'
```SQL
UPDATE account SET password = ? WHERE account.id = ?;
```

**Omien tuotteiden listaus**
+ Valitse 'Listaa omat tuotteet'
```SQL
SELECT * FROM product
WHERE product.account_id = account.id;
```

**Tuotteen lisäys**
+ Valitse 'Lisää tuote'
+ Täytä kentät
+ Paina nappia 'Lisää uusi tuote'
```SQL
INSERT INTO product (name, description, price)
VALUES (?, ?, ?);
```

**Kuvauksen muutos**
+ Valitse 'Listaa tuotteet'
+ Etsi listasta tuote 
+ Paina tuotteen nimeä
+ Vaihda kenttään haluamasi kuvaus
+ Paina 'Vaihda kuvaus'
```SQL
UPDATE product SET description = ? WHERE product.id = ?;
```

**Tuotteen poisto**
+ Valitse 'Listaa tuotteet'
+ Etsi listasta tuote 
+ Paina tuotteen nimeä
+ Paina 'Poista'
```SQL
DELETE FROM product WHERE product.id = ?;
```

**Tarjouksen tekeminen**
+ Valitse 'Listaa tuotteet'
+ Etsi listatsta tuote 
+ Paina tuotteen nimeä
+ Täytä kenttään tarjous
+ Paina 'Tarjoa'
```SQL
INSERT INTO offer (price, account_id, product_id);
```

**Uloskirjautuminen**
+ Valitse 'Kirjaudu ulos'
