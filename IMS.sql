create database IF NOT EXISTS IMS;
use IMS;
create table suppliers(
    supplier_id INT PRIMARY KEY,
    supplier_name varchar(40),
    address varchar(45),
    phone varchar(20),
    email varchar(45)
);
create table products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name varchar(255),
    catagory VARCHAR(40),
    unit_price FLOAT,
    stock_level INT,
    supplier_id INT,
    FOREIGN key(supplier_id) REFERENCES suppliers(supplier_id)
)AUTO_INCREMENT = 16;

create table sales(
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    sale_date DATE,
    quantity INT,
    revenue FLOAT,
    FOREIGN KEY(product_id) REFERENCES products(product_id)
    
);


