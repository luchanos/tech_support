"""
Create table for orders
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""CREATE TABLE orders (order_id SERIAL PRIMARY KEY,
agent_id int,
message text,
serial_no text,
status int)""", """DROP TABLE orders""")
]
