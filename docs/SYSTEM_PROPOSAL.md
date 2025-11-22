# System Proposal: Django E-commerce Application

**Course:** IT 403 WMAD - Elective 5 (WST 3)  
**Institution:** Bulacan State University  
**College:** College of Information and Communications Technology  
**Date:** November 22, 2025

## Project Team Members

- **Lead Developer:** [Your Name Here]
- **Team Members:** [Add team member names]
- **Project Supervisor:** [Supervisor Name]

## 1. Executive Summary

The Django E-commerce Application is a comprehensive web-based platform designed to facilitate online product sales and management. Built using Django framework, this system provides a robust solution for businesses to manage their inventory, process customer orders, and handle secure transactions.

## 2. System Description

### 2.1 Project Overview
Our e-commerce platform is designed to serve local businesses looking to establish an online presence. The system supports product catalog management, user authentication, shopping cart functionality, and order processing with integrated payment solutions.

### 2.2 System Objectives
- Provide a user-friendly interface for customers to browse and purchase products
- Enable efficient inventory management for administrators
- Implement secure user authentication and authorization
- Process orders with integrated payment gateway
- Generate comprehensive reports for business analytics

### 2.3 Target Users
- **Customers:** End users who browse and purchase products
- **Administrators:** Business owners and managers who manage inventory and orders
- **Staff:** Employees who handle order fulfillment and customer service

## 3. System Features

### 3.1 Core Features
1. **User Management**
   - User registration and authentication
   - Profile management
   - Role-based access control

2. **Product Management**
   - Product catalog with categories
   - Product search and filtering
   - Inventory tracking
   - Image management

3. **Shopping Cart**
   - Add/remove products
   - Quantity management
   - Cart persistence

4. **Order Processing**
   - Order creation and tracking
   - Address management
   - Order status updates

5. **Payment Integration**
   - Secure payment processing
   - Multiple payment methods
   - Transaction logging

### 3.2 Administrative Features
- Product inventory management
- Order management dashboard
- User management
- Sales reporting
- System configuration

## 4. Technical Specifications

### 4.1 Technology Stack
- **Backend Framework:** Django 4.2
- **Database:** SQLite (Development), PostgreSQL (Production)
- **Frontend:** HTML5, CSS3, JavaScript
- **Authentication:** Django Allauth
- **Payment Processing:** Stripe Integration
- **API:** Django REST Framework

### 4.2 System Requirements
- **Server:** Python 3.8+
- **Database:** SQLite/PostgreSQL
- **Web Server:** Django Development Server/Gunicorn
- **Storage:** Local file system/Cloud storage

## 5. Database Design

### 5.1 Entity Relationship Model
The system utilizes a well-structured relational database with the following main entities:

- **User:** Custom user model extending Django's AbstractUser
- **Category:** Product categorization
- **Product:** Main product information and inventory
- **Cart/CartItem:** Shopping cart functionality
- **Order/OrderAddress:** Order processing and shipping information

### 5.2 Database Schema
Refer to the complete ERD diagram in the project documentation for detailed field specifications and relationships.

## 6. System Architecture

### 6.1 Application Structure
```
django-ecommerce/
├── apps/
│   ├── users/          # User management
│   ├── products/       # Product catalog
│   ├── cart/          # Shopping cart
│   ├── orders/        # Order processing
│   └── payments/      # Payment gateway
├── templates/         # HTML templates
├── static/           # CSS, JS, Images
└── docs/            # Documentation
```

### 6.2 Design Patterns
- **Model-View-Template (MVT):** Django's architectural pattern
- **Repository Pattern:** Data access abstraction
- **Service Layer:** Business logic separation

## 7. Page Flow Diagram

### 7.1 Customer Journey
1. **Home Page** → Browse products by category
2. **Product List** → View available products
3. **Product Detail** → View product specifications
4. **Add to Cart** → Shopping cart management
5. **Checkout** → Order and shipping information
6. **Payment** → Secure payment processing
7. **Confirmation** → Order confirmation and receipt

### 7.2 Admin Workflow
1. **Admin Login** → Authentication
2. **Dashboard** → System overview
3. **Product Management** → Add/edit/delete products
4. **Order Management** → Process and track orders
5. **User Management** → Manage customer accounts
6. **Reports** → View sales and analytics

## 8. Security Features

- **Authentication:** Secure user login and registration
- **Authorization:** Role-based access control
- **Data Protection:** Input validation and sanitization
- **Payment Security:** PCI-compliant payment processing
- **Session Management:** Secure session handling

## 9. Implementation Timeline

- **Week 1-2:** Project setup and user authentication
- **Week 3-4:** Product catalog and cart functionality
- **Week 5-6:** Order processing and payment integration
- **Week 7-8:** Testing, documentation, and deployment

## 10. Testing Strategy

- **Unit Testing:** Individual component testing
- **Integration Testing:** System component interaction
- **User Acceptance Testing:** End-user functionality validation
- **Security Testing:** Vulnerability assessment

## 11. Conclusion

The Django E-commerce Application provides a comprehensive solution for online retail businesses. With its robust architecture, secure payment processing, and user-friendly interface, the system meets the requirements for a modern e-commerce platform while maintaining scalability for future enhancements.

## 12. References

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Stripe API Documentation: https://stripe.com/docs/api
- Python Best Practices: https://www.python.org/dev/peps/