In this first technique’s implementation, we start with the basic Rocket company app that currently only supports 1 tenant and build on it gradually making it multi-tenant. 
By the end, it is supposed to be able to use the same code base, one database, and one schema to handle multiple tenants.

# All tenants with a shared database and schema
In this multi-tenancy implementation technique, the data for all our tenants reside in one database and share the same schema. 
To tell each tenant’s data apart, we tag their records in the database with their foreign key. 
The foreign key is then used whenever a tenant wants to retrieve data; We first check the tenant’s foreign key and match it to the data stored using that foreign key. 
Then we return that data to the tenant who made the request. The same applies to when they want to perform other CRUD operations in the Rocket company app.

![image](https://github.com/Sajeyks/Educative-multitenancy-1/assets/47979791/76e1bb51-1320-48fc-a5f1-b8df6a418581)
