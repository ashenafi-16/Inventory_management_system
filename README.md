# Inventory Management System for Retail

## Overview

This project implements an Inventory Management System for retail stores, enabling efficient tracking of products, suppliers, and sales transactions. It uses Python, OOP principles, control flows, and MySQL databases to manage stock levels, generate reports, and forecast demand.

## Key Features

- **Product Management**: Add, update, and delete product details (ID, name, category, price, stock level).
- **Supplier Management**: Add suppliers linked to products.
- **Sales Transactions**: Record purchases and update stock levels.
- **Reports & Analytics**:
  - Low-stock alerts.
  - Demand forecasting.

## Deliverables

1. **Python Code**: Organized script with functions and OOP components.
2. **Database Schema**: MySQL tables for products, suppliers, and sales.
3. **Setup Instructions**: Guide for running the project and database setup.
4. **Terminal Reports**: Revenue, best-sellers, and stock alerts.

## Database Structure

- **Products**: `id`, `name`, `category`, `price`, `stock_level`
- **Suppliers**: `id`, `name`, `contact_info`
- **Sales**: `id`, `product_id`, `quantity`, `sale_date`, `revenue`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ashenafi-16/Inventory_management_system.git
   cd inventory_management_system
   ```