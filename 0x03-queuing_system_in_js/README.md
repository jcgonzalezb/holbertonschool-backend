# JavaScript - Queuing System in JS

## Description of the files inside this folder:

0. Download, extract, and compile the latest stable Redis version
- Start Redis in the background with src/redis-server
- Make sure that the server is working with a ping src/redis-cli ping
- Using the Redis client again, set the value School for the key Holberton
- Kill the server with the process id of the redis-server (hint: use ps and grep)
- Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.

1. Install node_redis using npm. Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:
- It should log to the console the message Redis client connected to the server when the connection to Redis works correctly
- It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work

2. In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).
Add two functions:
- setNewSchool:
	- It accepts two arguments schoolName, and value.
	- It should set in Redis the value for the key schoolName
	- It should display a confirmation message using redis.print
- displaySchoolValue:
	- It accepts one argument schoolName.
	- It should log to the console the value for the key passed as argument

- At the end of the file, call:
	- displaySchoolValue('Holberton');
	- setNewSchool('HolbertonSanFrancisco', '100');
	- displaySchoolValue('HolbertonSanFrancisco');


3. In a file 2-redis_op_async.js, let’s copy the code from the previous exercise (1-redis_op.js). Using promisify, modify the function displaySchoolValue to use ES6 async / await. Same result as 1-redis_op.js. It

4. In a file named 4-redis_advanced_op.js, let’s use the client to store a hash value
### Create Hash:
Using hset, let’s store the following:
- The key of the hash should be HolbertonSchools
- It should have a value for:
	- Portland=50
	- Seattle=80
	- New York=20
	- Bogota=20
	- Cali=40
	- Paris=2
- Make sure you use redis.print for each hset

### Display Hash:

Using hgetall, display the object stored in Redis. It should return the following:

5. In a file named 5-subscriber.js, create a redis client:
- On connect, it should log the message Redis client connected to the server
- On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
- It should subscribe to the channel holberton school channel
- When it receives message on the channel holberton school channel, it should log the message to the console
- When the message is KILL_SERVER, it should unsubscribe and quit

In a file named 5-publisher.js, create a redis client:
- On connect, it should log the message Redis client connected to the server
- On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
- Write a function named publishMessage:
	- It will take two arguments: message (string), and time (integer - in ms)
	- After time millisecond:
		- The function should log to the console About to send MESSAGE
		- The function should publish to the channel holberton school channel, the message passed in argument after the time passed in arguments
- At the end of the file, call:

6. In a file named 6-job_creator.js:

- Create a queue with Kue
- Create an object containing the Job data
- Create a queue named push_notification_code, and create a job with the object created before
- When the job is created without error, log to the console Notification job created: JOB ID
- When the job is completed, log to the console Notification job completed
- When the job is failing, log to the console Notification job failed

7. In a file named 6-job_processor.js:
- Create a queue with Kue
- Create a function named sendNotification:
	- It will take two arguments phoneNumber and message
	- It will log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE
- Write the queue process that will listen to new jobs on push_notification_code:
	- Every new job should call the sendNotification function with the phone number and the message contained within the job data

8. In a file named 7-job_creator.js:

Create an array jobs with the soem data inside.


After this array created:

- Create a queue with Kue
- Write a loop that will go through the array jobs and for each object:
	- Create a new job to the queue push_notification_code_2 with the current object
	- If there is no error, log to the console Notification job created: JOB_ID
	- On the job completion, log to the console Notification job JOB_ID completed
	- On the job failure, log to the console Notification job JOB_ID failed: ERROR
	- On the job progress, log to the console Notification job JOB_ID PERCENTAGE% complete

9. In a file named 7-job_processor.js:

Create an array that will contain the blacklisted phone numbers. Add in it 4153518780 and 4153518781 - these 2 numbers will be blacklisted by our jobs processor.

Create a function sendNotification that takes 4 arguments: phoneNumber, message, job, and done:

- When the function is called, track the progress of the job of 0 out of 100
- If phoneNumber is included in the “blacklisted array”, fail the job with an Error object and the message: Phone number PHONE_NUMBER is blacklisted
- Otherwise:
	- Track the progress to 50%
	- Log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE

Create a queue with Kue that will proceed job of the queue push_notification_code_2 with two jobs at a time.

10. In a file named 8-job.js, create a function named createPushNotificationsJobs:
- It takes into argument jobs (array of objects), and queue (Kue queue)
- If jobs is not an array, it should throw an Error with message: Jobs is not an array
- For each job in jobs, create a job in the queue push_notification_code_3
- When a job is created, it should log to the console Notification job created: JOB_ID
- When a job is complete, it should log to the console Notification job JOB_ID completed
- When a job is failed, it should log to the console Notification job JOB_ID failed: ERROR
- When a job is making progress, it should log to the console Notification job JOB_ID PERCENT% complete


11. Now that you created a job creator, let’s add tests:
- Import the function createPushNotificationsJobs
- Create a queue with Kue
- Write a test suite for the createPushNotificationsJobs function:
	- Use queue.testMode to validate which jobs are inside the queue
	etc.

12. 
### Data
Create an array listProducts containing the list of the following products:

- Id: 1, name: Suitcase 250, price: 50, stock: 4
- Id: 2, name: Suitcase 450, price: 100, stock: 10
- Id: 3, name: Suitcase 650, price: 350, stock: 2
- Id: 4, name: Suitcase 1050, price: 550, stock: 5

### Data access
Create a function named getItemById:

- It will take id as argument
- It will return the item from listProducts with the same id

### Server
Create an express server listening on the port 1245. (You will start it via: npm run dev 9-stock.js)

### Products
Create the route GET /list_products that will return the list of every available product with the following JSON format:

### In stock in Redis
Create a client to connect to the Redis server:

- Write a function reserveStockById that will take itemId and stock as arguments:
	- It will set in Redis the stock for the key item.ITEM_ID
- Write an async function getCurrentReservedStockById, that will take itemId as an argument:
	- It will return the reserved stock for a specific item


### Product detail
Create the route GET /list_products/:itemId, that will return the current product and the current available stock (by using getCurrentReservedStockById) with the a JSON format.


### Reserve a product
Create the route GET /reserve_product/:itemId:
- If the item does not exist, it should return:
```
bob@dylan:~$ curl localhost:1245/reserve_product/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$ 
```
- If the item exists, it should check that there is at least one stock available. If not it should return:

```
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Not enough stock available","itemId":1}
bob@dylan:~$ 

```

- If there is enough stock available, it should reserve one item (by using reserveStockById), and return:
```
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Reservation confirmed","itemId":1}
bob@dylan:~$ 
```

## Configuration files:

- .babelrc
- package.json



## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Javascript (ES6), Node v14.
- Style guidelines: [Javascript Standard](https://standardjs.com/rules.html) || [ESLint](https://eslint.org/)

<p align="left"> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
