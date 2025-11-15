# API Documentation for Django E-commerce Application

## Overview
This document provides an overview of the API endpoints available in the Django E-commerce application. Each endpoint is described with its method, URL, parameters, and response format.

## Authentication
### Login
- **Method**: POST
- **URL**: `/api/login/`
- **Parameters**:
  - `username`: string (required)
  - `password`: string (required)
- **Response**:
  - `token`: string (JWT token for authentication)

### Logout
- **Method**: POST
- **URL**: `/api/logout/`
- **Response**:
  - `message`: string (confirmation of logout)

## Users
### Create User
- **Method**: POST
- **URL**: `/api/users/`
- **Parameters**:
  - `username`: string (required)
  - `email`: string (required)
  - `password`: string (required)
- **Response**:
  - `id`: integer (user ID)
  - `username`: string
  - `email`: string

### Retrieve User
- **Method**: GET
- **URL**: `/api/users/{id}/`
- **Response**:
  - `id`: integer
  - `username`: string
  - `email`: string

## Products
### List Products
- **Method**: GET
- **URL**: `/api/products/`
- **Response**:
  - `products`: array of product objects
    - `id`: integer
    - `name`: string
    - `price`: decimal
    - `description`: string

### Retrieve Product
- **Method**: GET
- **URL**: `/api/products/{id}/`
- **Response**:
  - `id`: integer
  - `name`: string
  - `price`: decimal
  - `description`: string

## Cart
### Add to Cart
- **Method**: POST
- **URL**: `/api/cart/add/`
- **Parameters**:
  - `product_id`: integer (required)
  - `quantity`: integer (required)
- **Response**:
  - `message`: string (confirmation of addition)

### View Cart
- **Method**: GET
- **URL**: `/api/cart/`
- **Response**:
  - `cart_items`: array of cart item objects
    - `product_id`: integer
    - `quantity`: integer

## Orders
### Create Order
- **Method**: POST
- **URL**: `/api/orders/`
- **Parameters**:
  - `cart_id`: integer (required)
- **Response**:
  - `order_id`: integer
  - `status`: string (order status)

### Retrieve Order
- **Method**: GET
- **URL**: `/api/orders/{id}/`
- **Response**:
  - `order_id`: integer
  - `status`: string
  - `items`: array of order item objects

## Payments
### Process Payment
- **Method**: POST
- **URL**: `/api/payments/`
- **Parameters**:
  - `order_id`: integer (required)
  - `payment_method`: string (required)
- **Response**:
  - `payment_id`: integer
  - `status`: string (payment status)

## Conclusion
This API documentation outlines the key endpoints for user management, product handling, cart operations, order processing, and payment transactions in the Django E-commerce application. For further details, please refer to the individual endpoint documentation.