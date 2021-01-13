# tech_support
We try to create project for technical service of some devices. I think for medical devices, because I'm good in it))

TODO LIST:
1. Add new column created_dt for orders;
2. Add delete/update/get methods for orders manager;
3. Add consumer for RabbitMQ.

# ORDER CREATION MECHANISM
So, we can create order by two ways:
- by api endpoint: this way is approved for simple users;

For example you are the authorized person on customer side and you have the problem with device: you can send post 
request via api-endpoint;

- by sending messages to RabbitMQ queue: this way is good for B2B platforms.

For example you are service distributor of technics and you collect service reports on your side. Some of them needs
to be proccessed by tech_system. So you can send special message to queue for creation new service order.
