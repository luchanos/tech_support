# tech_support
We try to create project for technical service of some devices. I think for medical devices, because I'm good in it))

TODO LIST:
. Refactoring Sender and Consumer:
    - make is_active flags + dependencies;
    - make retry for sending messages;
    - add prefetch_count;
    - add durable parameter for queue and delivery mode for messages;
    - add manual ack for consumer;
. Add fixture for cleaning tables after test and before test.
. Create Order dataclass + Schema class for order
. add poetry to the project


# ORDER CREATION MECHANISM
So, we can create order by two ways:
- by api endpoint: this way is approved for simple users;

For example you are the authorized person on customer side and you have the problem with device: you can send post 
request via api-endpoint;

- by sending messages to RabbitMQ queue: this way is good for B2B platforms.

For example you are service distributor of technics and you collect service reports on your side. Some of them needs
to be proccessed by tech_system. So you can send special message to queue for creation new service order.

# FOR PACKAGE INSTALLATION
use poetry
1. pip install poetry;
2. if you need to add some dependencies do it in pyproject.toml file.
