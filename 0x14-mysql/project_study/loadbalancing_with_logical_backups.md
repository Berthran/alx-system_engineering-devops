Your assumption is accurate and aligns well with how load balancing typically works in database architectures involving replicas. Let's explore this concept in more detail to understand how it works in real-life scenarios.

### How Load Balancing Works with Database Replicas

1. **Primary Database**:
   - Also known as the master or write database.
   - Handles all write operations (INSERT, UPDATE, DELETE).
   - Ensures data consistency by being the single source of truth for write operations.

2. **Replica Databases**:
   - Also known as read replicas or slave databases.
   - Handle read operations (SELECT).
   - Replicate data from the primary database to provide the same data for read operations.

### Example Use Case

Imagine you have a web application that allows users to view and purchase products. The database needs to handle user data, product information, and order details. Here’s how load balancing can be implemented:

1. **Write Operations (Primary Database)**:
   - When a user adds a product to their cart or makes a purchase, these actions require writing data to the database.
   - These write operations are directed to the primary database to ensure data integrity and consistency.
   - Example:
     ```sql
     INSERT INTO orders (user_id, product_id, quantity, order_date) VALUES (1, 101, 2, '2024-07-23');
     ```

2. **Read Operations (Replica Databases)**:
   - When users browse products or view their order history, these actions are read-only.
   - These read operations can be distributed across multiple replica databases to balance the load.
   - Example:
     ```sql
     SELECT * FROM products WHERE category = 'electronics';
     ```

### Real-Life Implementation

In real-world applications, implementing this kind of load balancing typically involves:

1. **Database Configuration**:
   - Setting up a primary database and one or more replica databases.
   - Configuring replication settings to ensure replicas are kept up-to-date with the primary.

2. **Application Logic**:
   - Modifying the application to route write operations to the primary database.
   - Modifying the application to route read operations to replica databases.
   - This routing can be managed through database connection settings, middleware, or load balancers.

3. **Load Balancer**:
   - A load balancer can be used to distribute read requests among the replicas.
   - Ensures even distribution of load to avoid any single replica being overwhelmed.

### Tools and Middleware

Several tools and middleware solutions can help manage this setup:

- **ProxySQL**: An intelligent database proxy that can handle read/write splitting, connection pooling, and more.
- **HAProxy**: A high-availability load balancer that can distribute database read traffic across replicas.
- **ORMs (Object-Relational Mappers)**: Many ORMs (like Hibernate, SQLAlchemy, etc.) offer built-in support for read/write splitting.

### Example Code Snippet

Here’s a conceptual example of how this might look in a Python application using SQLAlchemy:

```python
from sqlalchemy import create_engine, text

# Create engine for primary (write) database
primary_engine = create_engine('mysql+pymysql://user:password@primary_db:3306/mydb')

# Create engines for replica (read) databases
replica_engines = [
    create_engine('mysql+pymysql://user:password@replica1_db:3306/mydb'),
    create_engine('mysql+pymysql://user:password@replica2_db:3306/mydb')
]

def execute_write(query, params):
    with primary_engine.connect() as conn:
        conn.execute(text(query), params)

def execute_read(query, params):
    # Simple round-robin load balancing for reads
    replica_engine = replica_engines.pop(0)
    replica_engines.append(replica_engine)
    with replica_engine.connect() as conn:
        return conn.execute(text(query), params)

# Example usage
write_query = "INSERT INTO orders (user_id, product_id, quantity, order_date) VALUES (:user_id, :product_id, :quantity, :order_date)"
write_params = {'user_id': 1, 'product_id': 101, 'quantity': 2, 'order_date': '2024-07-23'}
execute_write(write_query, write_params)

read_query = "SELECT * FROM products WHERE category = :category"
read_params = {'category': 'electronics'}
result = execute_read(read_query, read_params)
for row in result:
    print(row)
```

### Summary

- **Primary Database**: Handles all write operations to maintain data integrity.
- **Replica Databases**: Handle read operations to distribute the load and improve performance.
- **Load Balancer**: Distributes read requests across replicas to ensure balanced load.

This approach improves performance, scalability, and availability of your application by leveraging multiple database instances for read-heavy workloads while ensuring data consistency through a single primary database for write operations.
