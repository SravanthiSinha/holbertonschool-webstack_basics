# 0x03. Python web scraping

* Task 0 : Write a Python script that fetches [url](https://intranet.hbtn.io/status)

  File: 0-hbtn_status.py

  ```
  $ ./0-hbtn_status.py | cat -e
  Body response:$
      - type: <class 'str'>$
      - content: OK$
  $
  ```

* Task 1 : Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

  File : 1-hbtn_header.py

  ```
  $ ./1-hbtn_header.py https://intranet.hbtn.io
  5e52e160-c822-4669-8b3a-8b3bbca7b090
  $
  $ ./1-hbtn_header.py https://intranet.hbtn.io
  eaceaf35-bc0f-4f74-994a-7be0728ec654
  $
  ```

* Task 2: Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

  File : 2-post_email.py

  ```
  $ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
  Your email is: hr@holbertonschool.com
  $
  ```

* Task 3: Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
    * If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code

  File : 3-error_code.py

  ```
  $ ./3-error_code.py http://0.0.0.0:5000
  Index
  $ ./3-error_code.py http://0.0.0.0:5000/status_401
  Error code: 401
  $ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
  Error code: 404
  $ ./3-error_code.py http://0.0.0.0:5000/status_500
  Error code: 500
  $
  ```

* Task 4: Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

    * The letter must be sent in the variable q
    * If no argument is given, set q=""
    * If the response body is properly JSON formatted and not empty, display the id and name like this: `[<id>] <name>`
    * Otherwise:
      * Display Not a valid JSON is the JSON is invalid
      * Display No result is the JSON is empty

  File: 4-json_api.py
  ```
  $ ./4-json_api.py
  No result
  $ ./4-json_api.py a
  [8446] amnirqhtfjq
  $ ./4-json_api.py 2
  No result
  $ ./4-json_api.py b
  [7094] bmofakakhke
  $
  ```

* Task 5: Write a Python script that takes in a string and sends a search request to the [Star Wars API](https://swapi.co/documentation)

  * Use the [Star Wars API search people endpoint](https://swapi.co/documentation#search)
  * Use the string argument as the search value of the request
  * The body response must be JSON and converted to a Python dictionary.
  * Display: Number of result: <count>
  * Display the name of each result (see example below)

  File : 5-starwars.py

  ```
  $ ./5-starwars.py r2
  Number of result: 1
  R2-D2
  $ ./5-starwars.py lu
  Number of result: 2
  Luke Skywalker
  Luminara Unduli
  $ ./5-starwars.py ju
  Number of result: 0
  $ ./5-starwars.py g
  Number of result: 16
  Leia Organa
  Biggs Darklighter
  Greedo
  Wedge Antilles
  IG-88
  Qui-Gon Jinn
  Nute Gunray
  Rugor Nass
  Gasgano
  Adi Gallia
  $
  ```

* Task 6 : Write a Python script that takes your Github credentials (username and password) and uses the Github API to display your id

  File: 6-my_github.py

  ```
  $ ./6-my_github.py roses cisfun
  2531536
  $ ./6-my_github.py rose wrong_pwd
  None
  $
  ```


## UseFull Links:

* [HTTP (HyperText Transfer Protocol)](https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
* [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
* [Quickstart with Requests package](http://docs.python-requests.org/en/master/user/quickstart/)

[Requests package](http://docs.python-requests.org/en/master/)
