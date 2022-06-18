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

At the end of the file, call:
	- displaySchoolValue('Holberton');
	- setNewSchool('HolbertonSanFrancisco', '100');
	- displaySchoolValue('HolbertonSanFrancisco');










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
