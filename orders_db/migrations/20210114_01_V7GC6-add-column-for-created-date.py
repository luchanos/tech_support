"""
add column for created date
"""

from yoyo import step

__depends__ = {'20210111_01_B5uPE-create-table-for-orders'}

steps = [
    step("ALTER TABLE orders ADD COLUMN created_dt TIMESTAMP DEFAULT NOW();",
         "ALTER TABLE orders DROP COLUMN created_dt;")
]
