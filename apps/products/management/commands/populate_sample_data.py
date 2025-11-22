"""
Django management command to populate the database with sample data.
Run with: python manage.py populate_sample_data
"""
import os
import django
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.products.models import Category, Product
from apps.cart.models import Cart, CartItem
from apps.orders.models import Order, OrderAddress
from decimal import Decimal

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the database with sample data for testing and demonstration'

    def handle(self, *args, **options):
        self.stdout.write('Starting to populate sample data...')
        
        # Create sample users
        self.create_sample_users()
        
        # Create sample categories
        self.create_sample_categories()
        
        # Create sample products
        self.create_sample_products()
        
        # Create sample carts and orders
        self.create_sample_carts_and_orders()
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )

    def create_sample_users(self):
        """Create sample users for testing"""
        self.stdout.write('Creating sample users...')
        
        # Create regular customers
        customers = [
            {
                'username': 'john_doe',
                'email': 'john.doe@example.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'password': 'testpass123'
            },
            {
                'username': 'jane_smith',
                'email': 'jane.smith@example.com',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'password': 'testpass123'
            },
            {
                'username': 'mike_wilson',
                'email': 'mike.wilson@example.com',
                'first_name': 'Mike',
                'last_name': 'Wilson',
                'password': 'testpass123'
            }
        ]
        
        for customer_data in customers:
            if not User.objects.filter(username=customer_data['username']).exists():
                user = User.objects.create_user(
                    username=customer_data['username'],
                    email=customer_data['email'],
                    first_name=customer_data['first_name'],
                    last_name=customer_data['last_name'],
                    password=customer_data['password']
                )
                self.stdout.write(f'Created customer: {user.username}')

        # Create admin user if not exists
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(f'Created admin user: {admin_user.username}')

    def create_sample_categories(self):
        """Create sample product categories"""
        self.stdout.write('Creating sample categories...')
        
        categories = [
            {'name': 'Electronics', 'slug': 'electronics'},
            {'name': 'Clothing', 'slug': 'clothing'},
            {'name': 'Books', 'slug': 'books'},
            {'name': 'Home & Garden', 'slug': 'home-garden'},
            {'name': 'Sports & Fitness', 'slug': 'sports-fitness'},
            {'name': 'Beauty & Health', 'slug': 'beauty-health'},
        ]
        
        for category_data in categories:
            category, created = Category.objects.get_or_create(
                slug=category_data['slug'],
                defaults={'name': category_data['name']}
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')

    def create_sample_products(self):
        """Create sample products"""
        self.stdout.write('Creating sample products...')
        
        products = [
            # Electronics
            {
                'name': 'Smartphone Pro Max 128GB',
                'slug': 'smartphone-pro-max-128gb',
                'category_slug': 'electronics',
                'description': 'Latest flagship smartphone with advanced camera system, A16 chip, and all-day battery life.',
                'price': Decimal('899.99'),
                'stock': 25,
            },
            {
                'name': 'Wireless Bluetooth Headphones',
                'slug': 'wireless-bluetooth-headphones',
                'category_slug': 'electronics',
                'description': 'Premium noise-canceling headphones with 30-hour battery life and crystal-clear audio.',
                'price': Decimal('199.99'),
                'stock': 50,
            },
            {
                'name': 'Laptop Gaming Pro 16-inch',
                'slug': 'laptop-gaming-pro-16inch',
                'category_slug': 'electronics',
                'description': 'High-performance gaming laptop with RTX graphics, 32GB RAM, and 1TB SSD.',
                'price': Decimal('1299.99'),
                'stock': 15,
            },
            
            # Clothing
            {
                'name': 'Premium Cotton T-Shirt',
                'slug': 'premium-cotton-tshirt',
                'category_slug': 'clothing',
                'description': 'Comfortable 100% organic cotton t-shirt available in multiple colors and sizes.',
                'price': Decimal('29.99'),
                'stock': 100,
            },
            {
                'name': 'Denim Jeans Classic Fit',
                'slug': 'denim-jeans-classic-fit',
                'category_slug': 'clothing',
                'description': 'Classic fit denim jeans made from premium denim fabric with modern styling.',
                'price': Decimal('79.99'),
                'stock': 75,
            },
            {
                'name': 'Winter Jacket Waterproof',
                'slug': 'winter-jacket-waterproof',
                'category_slug': 'clothing',
                'description': 'Insulated waterproof jacket perfect for winter outdoor activities.',
                'price': Decimal('149.99'),
                'stock': 30,
            },
            
            # Books
            {
                'name': 'Python Programming Mastery',
                'slug': 'python-programming-mastery',
                'category_slug': 'books',
                'description': 'Complete guide to Python programming from beginner to advanced level.',
                'price': Decimal('49.99'),
                'stock': 40,
            },
            {
                'name': 'Web Development Complete Course',
                'slug': 'web-development-complete-course',
                'category_slug': 'books',
                'description': 'Learn modern web development with HTML, CSS, JavaScript, and popular frameworks.',
                'price': Decimal('59.99'),
                'stock': 35,
            },
            
            # Home & Garden
            {
                'name': 'Smart Home Security Camera',
                'slug': 'smart-home-security-camera',
                'category_slug': 'home-garden',
                'description': 'WiFi-enabled security camera with night vision and mobile app control.',
                'price': Decimal('129.99'),
                'stock': 20,
            },
            {
                'name': 'Indoor Plant Collection Set',
                'slug': 'indoor-plant-collection-set',
                'category_slug': 'home-garden',
                'description': 'Set of 5 easy-care indoor plants perfect for home and office decoration.',
                'price': Decimal('89.99'),
                'stock': 25,
            },
            
            # Sports & Fitness
            {
                'name': 'Professional Yoga Mat',
                'slug': 'professional-yoga-mat',
                'category_slug': 'sports-fitness',
                'description': 'High-quality non-slip yoga mat with excellent grip and cushioning.',
                'price': Decimal('39.99'),
                'stock': 60,
            },
            {
                'name': 'Fitness Tracker Smartwatch',
                'slug': 'fitness-tracker-smartwatch',
                'category_slug': 'sports-fitness',
                'description': 'Advanced fitness tracker with heart rate monitoring and GPS.',
                'price': Decimal('249.99'),
                'stock': 30,
            },
        ]
        
        for product_data in products:
            category = Category.objects.get(slug=product_data['category_slug'])
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults={
                    'name': product_data['name'],
                    'category': category,
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock': product_data['stock'],
                    'available': True,
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

    def create_sample_carts_and_orders(self):
        """Create sample carts and orders"""
        self.stdout.write('Creating sample carts and orders...')
        
        # Get sample users
        john = User.objects.get(username='john_doe')
        jane = User.objects.get(username='jane_smith')
        mike = User.objects.get(username='mike_wilson')
        
        # Get sample products
        smartphone = Product.objects.get(slug='smartphone-pro-max-128gb')
        headphones = Product.objects.get(slug='wireless-bluetooth-headphones')
        tshirt = Product.objects.get(slug='premium-cotton-tshirt')
        jeans = Product.objects.get(slug='denim-jeans-classic-fit')
        
        # Create carts
        john_cart, created = Cart.objects.get_or_create(user=john)
        if created:
            CartItem.objects.create(cart=john_cart, product=smartphone, quantity=1)
            CartItem.objects.create(cart=john_cart, product=headphones, quantity=2)
            self.stdout.write(f'Created cart for {john.username}')
        
        jane_cart, created = Cart.objects.get_or_create(user=jane)
        if created:
            CartItem.objects.create(cart=jane_cart, product=tshirt, quantity=3)
            CartItem.objects.create(cart=jane_cart, product=jeans, quantity=1)
            self.stdout.write(f'Created cart for {jane.username}')
        
        # Create sample orders
        orders_data = [
            {
                'user': mike,
                'product': smartphone,
                'quantity': 1,
                'is_ordered': True,
                'address': {
                    'address_line_1': '123 Main Street',
                    'city': 'Manila',
                    'state': 'Metro Manila',
                    'postal_code': '1000',
                    'country': 'Philippines'
                }
            },
            {
                'user': john,
                'product': tshirt,
                'quantity': 2,
                'is_ordered': True,
                'address': {
                    'address_line_1': '456 Oak Avenue',
                    'city': 'Quezon City',
                    'state': 'Metro Manila',
                    'postal_code': '1100',
                    'country': 'Philippines'
                }
            },
            {
                'user': jane,
                'product': headphones,
                'quantity': 1,
                'is_ordered': False,
                'address': {
                    'address_line_1': '789 Pine Road',
                    'city': 'Makati',
                    'state': 'Metro Manila',
                    'postal_code': '1200',
                    'country': 'Philippines'
                }
            }
        ]
        
        for order_data in orders_data:
            # Check if order already exists to avoid duplicates
            existing_order = Order.objects.filter(
                user=order_data['user'],
                product=order_data['product']
            ).first()
            
            if not existing_order:
                order = Order.objects.create(
                    user=order_data['user'],
                    product=order_data['product'],
                    quantity=order_data['quantity'],
                    is_ordered=order_data['is_ordered']
                )
                
                OrderAddress.objects.create(
                    order=order,
                    address_line_1=order_data['address']['address_line_1'],
                    city=order_data['address']['city'],
                    state=order_data['address']['state'],
                    postal_code=order_data['address']['postal_code'],
                    country=order_data['address']['country']
                )
                
                self.stdout.write(f'Created order for {order.user.username}: {order.product.name}')