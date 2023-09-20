# Intro
In Trigo's solution there are many proprietary sensors based on embedded microcontrollers running bare-metal OS under hard resources limit (low cpu, low memory). Those sensors cannot run any modern tools such as Docker, Consul agents and so on but do expose an http server with a dedicated metrics endpoint.

In addition, the store operators can change the participating sensors so the inventory of sensors can be updated quite often.

In this excersie we are going to implement custom service discovery for prometheus so even when the sensors configuration is changed continously, prometheus will keep monitoring the right sensor's inventory.

# Exercise
The [inventory service](https://github.com/trigovision/interview_exercises/tree/main/devops/prometheus_custom_sd/inventory_server) will be used to expose an http endpoint that yields a list of hosts of the current active sensors.

Specifically, invoking the following command:
```
curl -XGET http://localhost:1337/inventory
```
will yield the current sensors hostnames to monitor:
```
[
    "sensor_1",
    "sensor_2",
    "sensor_12",
    ...
]
```

Your goal in this excersice is to:
* Implement a custom service discovery for prometheus which queries the described endpoint (in the `inventory service`) and yields a target group containing the sensors targets
* Write a minimal docker-compose / helm chart which runs the entire stack, having a prometheus instance trying to scrape the sensors inventory with an exposed http port (tcp/9090)



# Additional Notes
* Don't change the `inventory service` code.
* Fork this repository and upload your solution then provide us with a link.
* Feel free to code it in any language you would like and use any framework / library / snippet of code you find.
* We are avaialbe for any question you have so feel free to ask.
