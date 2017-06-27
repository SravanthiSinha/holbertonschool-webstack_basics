# 0x02. Javascript Basics

 Web Stack programming ― Warmup

THe following code is  semistandard compliant (version 11.0.0). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/Flet/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)

Task 0: A script that prints 3 lines:

* The first line: "C is fun"
* The second line: "Python is cool"
* The third line: "Javascript is amazing"

File: 0-multi_languages.js

```
$ ./0-multi_languages.js
C is fun
Python is cool
Javascript is amazing
$
```

Task 1: A script that prints a message depending of the number of arguments passed:

* If no arguments are passed to the script, print "No argument"
* If only one argument is passed to the script, print "Argument found"
* Otherwise, print "Arguments found"

File : 1-arguments.js

```
$ ./1-arguments.js
No argument
$ ./1-arguments.js Holberton
Argument found
$ ./1-arguments.js Holberton School
Arguments found
$
```

Task 2: A script that prints the first argument passed to it:

* If no arguments are passed to the script, print "No argument"

File : 2-value_argument.js

```
$ ./2-value_argument.js
No argument
$ ./2-value_argument.js Holberton
Holberton
$
```

Task 3: A script that prints "My number: " if the first argument can be converted to an integer:
* If the argument can't be converted to an integer, print "Not a number"

File : 3-to_integer.js

```
$ ./3-to_integer.js
Not a number
$ ./3-to_integer.js 89
My number: 89
$ ./3-to_integer.js "89"
My number: 89
$ ./3-to_integer.js 89.89
My number: 89
$ ./3-to_integer.js Holberton
Not a number
$
```

Task 4:  A script that prints a square

* The first argument is the size of the square
* If the first argument can't be converted to an integer, print "Missing size"
* You must use the character X to print the square

File : 4-square.js

```
$ ./4-square.js
Missing size
$ ./4-square.js Holberton
Missing size
$ ./4-square.js 2
XX
XX
$ ./4-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$ ./4-square.js -3
$
```
Task 5: Update this script to replace the value 12 with 89

File : 5-object.js

```
$ cat 5-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

$ ./5-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
$
```

Task 6: A function that returns the addition of 2 integers.

* The function must be visible from outside
The name of the function must be add

File : 6-add.js

```
$ cat 6-main.js
#!/usr/bin/node
const add = require('./6-add').add;
console.log(add(3, 5));
$ ./6-main.js
8
$
```

Task 7: A class Rectangle that defines a rectangle:

* You must use the function notation for defining your class
* The constructor must take 2 arguments w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h

File : 7-rectangle.js

```
#!/usr/bin/node
const Rectangle = require('./7-rectangle').Rectangle;

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

$ ./7-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
$
```
Task 8: Write a class Rectangle that defines a rectangle:

* You must use the function notation for defining your class
* The constructor must take 2 arguments w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h
* If w or h is equal to 0 or not a positive integer, create an empty object

File : 8-rectangle.js

```
$ cat 8-main.js
#!/usr/bin/node
const Rectangle = require('./8-rectangle').Rectangle;

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

$ ./8-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
$
```

Task 9: Write a class Rectangle that defines a rectangle:

* You must use the function notation for defining your class
* The constructor must take 2 arguments: w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h
* If w or h is equal to 0 or not a positive integer, create an empty object
* Create an instance method called print() that prints the rectangle using the character X

File : 9-rectangle.js

```
$ cat 9-main.js
#!/usr/bin/node
const Rectangle = require('./9-rectangle').Rectangle;

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

$ ./9-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
$
```
Task 10: Write a script that reads and prints the content of a file.

* The first argument is the file path
* The content of the file must be read in utf-8
* If an error occurred during the reading, print the error object

File : 10-readme.js

```
$ ./10-readme.js cisfun
C is super fun!
$ cat cisfun
C is super fun!
$ ./10-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
$
```
Task 11: Write a script that writes a string to a file.

* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in utf-8
* If an error occurred during while writing, print the error object
File : 11-writeme.js

```
$ ./11-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt ; echo ""
Python is cool
$
$
```

Task 12: Write a script that imports an array and computes a new array.

* Your script must import list from the file 100-data.js
* A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
* Print both the initial list and the new list

File : 100-map.js

```
$ cat 100-data.js
#!/usr/bin/node
exports.list = [1, 2, 3, 4, 5];
$ ./100-map.js
[ 1, 2, 3, 4, 5 ]
[ 0, 2, 6, 12, 20 ]
$
```

Task 13: Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

* Your script must import dict from the file 101-data.js
* In the new dictionary:

  * A key is a number of occurrences
  * A value is the list of user ids


* Print the new dictionary at the end

File : 101-sorted.js

```
$ cat 101-data.js
#!/usr/bin/node
exports.dict = {
  89: 1,
  90: 2,
  91: 1,
  92: 3,
  93: 1,
  94: 2
};
$ ./101-sorted.js
{ '1': [ '89', '91', '93' ], '2': [ '90', '94' ], '3': [ '92' ] }
$
```

Task 14: Write a script that concats 2 files.

*  The first argument is the file path of the first source file
*  The second argument is the file path of the second source file
*  The third argument is the file path of the destination


File : 102-concat.js

```
$ cat fileA
C is fun!
$ cat fileB
Python is Cool!!!
$ ./102-concat.js fileA fileB fileC
$ cat fileC
C is fun!
Python is Cool!!!
$
```

Task 15: Write a file that modifies the value of myVar to 333

File : 103-let_me_const.js

```
guillaume@ubuntu:~/0x11$ cat 103-main.js
#!/usr/bin/node
myVar = 89;
require('./103-let_me_const')
console.log(myVar);
$ ./103-main.js
333
$

```
Task 16: Write a function that executes x times a function.

* The function must be visible from outside
* Prototype: function (x, theFunction)


File : 104-call_me_moby.js

```
$ cat 104-main.js
#!/usr/bin/node
const callMeMoby = require('./104-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
$ ./104-main.js
C is fun
C is fun
C is fun
$
```
Task 17: Write a function that increments and calls a function.

* The function must be visible from outside
* Prototype: function (number, theFunction)

File : 105-add_me_maybe.js

```
$ cat 105-main.js
#!/usr/bin/node
const addMeMaybe = require('./105-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
$ ./105-main.js
New value: 5
$

```
Task 18: Update this script by adding a new function incr that increments the integer value.

File : 106-object_fct.js

```
$ cat 106-object_fct.js
#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

$ ./106-object_fct.js
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
$
$
```
Task 19: Write a class Rectangle that defines a rectangle:

* You must use the function notation for defining your class
* The constructor must take 2 arguments: w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h
* If w or h is equal to 0 or not a positive integer, create an empty object
* Create an instance method called print() that prints the rectangle using the character X
* Create an instance method called rotate() that exchanges the width and the height of the rectangle
* Create an instance method called double() that multiples the width and the height of the rectangle by 2

File : 107-rectangle.js

```
$ cat 107-main.js
#!/usr/bin/node
const Rectangle = require('./107-rectangle').Rectangle;

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

$ ./107-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$
```
Task 20: Write a script that searches the second biggest integer in the list of arguments.

* You can assume all arguments can be converted to integer
* If no argument passed, print 0
* If the number of arguments is 1, print 0

File : 108-second_biggest.js

```
$ ./108-second_biggest.js
0
$ ./108-second_biggest.js 1
0
$ ./108-second_biggest.js 4 2 5 3 0 -3
4
$
```
Task 21: Write a class Square that defines a square and inherits from Rectangle of 107-rectangle.js:

* You must use the function notation for defining your class
* The constructor must take 1 argument: size
* The constructor of Rectangle must be called

File : 109-square.js

```
$ cat 109-main.js
#!/usr/bin/node
const Square = require('./109-square').Square;

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

$ ./109-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
$
```

Task 22: Write a class Square that defines a square and inherits from Square of 109-square.js:

* You must use the prototype notation for adding a new method
* Create an instance method called charPrint(c) that prints the rectangle using the character c
* If c is undefined, use the character X

File : 110-square.js

```
$ cat 110-main.js
#!/usr/bin/node
const Square = require('./110-square').Square;

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

$ ./110-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
$
```

# UseFull Links:


  [Writing JavaScript Code](https://docs.microsoft.com/en-us/scripting/javascript/writing-javascript-code)

  [Variables](https://docs.microsoft.com/en-us/scripting/javascript/variables-javascript)

  [Data Types](https://docs.microsoft.com/en-us/scripting/javascript/data-types-javascript)

  [Operators](https://docs.microsoft.com/en-us/scripting/javascript/operators-javascript)

  [Precedence Operator](https://docs.microsoft.com/en-us/scripting/javascript/operator-subtractprecedence-javascript)

  [Controlling Program Flow](https://docs.microsoft.com/en-us/scripting/javascript/controlling-program-flow-javascript)

  [Functions](https://docs.microsoft.com/en-us/scripting/javascript/functions-javascript)

  [Objects and Arrays](https://docs.microsoft.com/en-us/scripting/javascript/objects-and-arrays-javascript)

  [Intrinsic Objects](https://docs.microsoft.com/en-us/scripting/javascript/intrinsic-objects-javascript)

  [Module patterns](http://darrenderidder.github.io/talks/ModulePatterns/#/)

  [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)

  [Javascript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)

  [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)

  [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS)

  [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)

  [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance)

  [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
