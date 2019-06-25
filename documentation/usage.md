## Rekisteröitymätön käyttäjä

**Tuotteiden listaus**
+ Valitse 'Tuotteet'
```SQL
SELECT * FROM product;
```

**Tagien listaus**
+ Valitse 'Tagit'
```SQL
SELECT * FROM tag;
```

**Tuotteiden listaus tagin perusteella**
+ Valitse 'Tagit'
```SQL
SELECT * FROM product
WHERE product.tag_id = ?
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
+ Valitse 'Oma profiili'
```SQL
SELECT * FROM product
WHERE product.account_id = account.id;
```

**Tuotteen lisäys**
+ Valitse 'Lisää tuote'
+ Täytä kentät
+ Paina nappia 'Lisää uusi tuote'
```SQL
INSERT INTO product (name, description)
VALUES (?, ?, ?);
```

**Kuvauksen muutos**
+ Valitse 'Listaa tuotteet'
+ Etsi listasta tuoteesi 
+ Paina tuotteen nimeä
+ Vaihda kenttään haluamasi kuvaus
+ Paina 'Vaihda kuvaus'
```SQL
UPDATE product SET description = ? WHERE product.id = ?;
```

**Tuotteen poisto**
+ Valitse 'Listaa tuotteet'
+ Etsi listasta tuoteesi 
+ Paina tuotteen nimeä
+ Paina 'Poista tuote'
```SQL
DELETE FROM product WHERE product.id = ?;
```

**Tarjouksen tekeminen**
+ Valitse 'Tuotteet'
+ Etsi listatsta tuote 
+ Paina tuotteen nimeä
+ Täytä kenttään tarjous
+ Paina 'Tarjoa'
```SQL
INSERT INTO offer (price, account_id, product_id)
VALUES (?, ?, ?);
```

**Tagin lisääminen tuotteelle**
+ Valitse 'Tuotteet'
+ Etsi listasta tuoteesi
+ Paina tuotteen nimeä
+ Valitse listasta tagi
+ Paina 'Lisää tuotteelle tägi'
```SQL
INSERT INTO tagProduct (product_id, tag_id)
VALUES (?, ?);
```

**Uloskirjautuminen**
+ Valitse 'Kirjaudu ulos'

## Admin käyttäjä

**Tägin poisto**
+ Valitse 'Tagit'
+ Etsi listasta tagi
+ Paina 'Poista'
```SQL
DELETE FROM tag WHERE tag.id = ?;
```

**Listaa käyttäjät**
+ Valitse 'Käyttäjät'
```SQL
SELECT * FROM account
```

**Käyttäjän poisto**
+ Valitse 'Käyttäjät'
+ Etsi listalta käyttäjä
+ Paina 'Poista'
```SQL
DELETE FROM account WHERE account.id = ?
```

**Käyttäjälle Admin oikeudet**
+ Valitse 'Käyttäjät'
+ Etsi listasta käyttäjä
+ Paina 'Tee käyttäjästä Admin'
```SQL
UPDATE account SET role = ? WHERE account.id = ?
```
