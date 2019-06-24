# CREATE TABLE - lauseet

```
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        email varchar(200) NOT NULL
)

CREATE TABLE product  (
        id INTEGER NOT NULL,
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL,
        description VARCHAR(500),
        onSale BOOLEAN NOT NULL,
        FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE offer  (
        id INTEGER NOT NULL,
        date_created DATETIME, 
        date_modified DATETIME, 
        price INTEGER NOT NULL, 
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(product_id) REFERENCES product (id)
)

CREATE TABLE tag  (
        id INTEGER NOT NULL,
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR NOT NULL, 
)

CREATE TABLE tagProduct  (
        id INTEGER NOT NULL,
        date_created DATETIME, 
        date_modified DATETIME, 
        FOREIGN KEY(product_id) REFERENCES product (id),
        FOREIGN KEY(tag_id) REFERENCES tag (id)
)
