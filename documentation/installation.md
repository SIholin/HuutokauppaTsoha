## Asennusohjeet

Sovelluksen saa käynnistettyä paikallisesti kloonaamalla sen githubista tietokoneelle ja lataamalla siihen vaaditut vaatimukset. Alla on terminaalissa käytettävät komennot sovelluksen lataamiseen githubista ja käynnistämiseen. 

```
git clone git@github.com:SIholin/HuutokauppaTsoha.git
cd HuutokauppaTsoha
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 run.py

```

Sovelluksen saa toimimaan Herokussa painamalla Readme:ssä olevaa linkkiä, jonka jälkeen sovellus käynnistyy. 

## Käyttöohjeet

Sovelluksen käynnistäessä pääsee sovelluksen etusivulle. Etusivulta löytyy mahdollisuudet sisäänkirjautumiseen, rekisteröitymiseen ja tuotteiden sekä tägien listaukseen. Rekisteröityessä tulee täyttää vaaditut tiedot ja sovelllus ilmoittaa virhetilanteista, jos vaikka käytttäjänimi on jo varattu. Rekisteröinnin jälkeen voi kirjautua sisään omilla tunnuksilla. Sisäänkirjautunut käyttäjä voi tehdä tarjouksia toisten käyttäjien tuotteista ja laittaa omia myynti-ilmoituksia. Omien myynti-ilmoitusksia voi poistaa ja kuvauksia muuttaa. Omien tuotteiden huutokaupan voi myös päättää. Tuotteita voi listata ja hakea 'Listaa tuotteet'-sivulla. Sisäänkirjautunut käyttäjä voi vaihtaa salasanansa sivulla 'Vaihda salasana'. Ulos pääsee kirjautumaan painamalla 'Kirjaudu ulos'. Admin-käyttäjä näkee etusivullaan yhteenvetokyselyitä, hän pystyy poistamaan muita käyttäjiä ja tägejä sekä tekemään myös heistä Admin-käyttäjiä.

Tarkemmat käyttöohjeet löytyvät täältä -> [Käyttöohjeet](https://github.com/SIholin/HuutokauppaTsoha/blob/master/documentation/usage.md)
