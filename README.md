lux-img
=======

Scrapes and downloads image on lux

Install Instructions
---------

1. You'll need to clone the repo

  ```sh
  $ git@github.com:abekim/lux-img.git
  ```

2. Second, download `pip` and `virtualenv`

  ```sh
  $ sudo easy_install pip  
  $ sudo pip install virtualenv
  ```

3. Setup an isolated environment with `virtualenv`

  ```sh
  $ virtualenv --no-site-packages env  
  $ source env/bin/activate
  ```

4. Install system dependencies

  On Mac OSX:

  ```sh
  $ ./setup.sh
  ```

5. Run

  ```sh
  $ python main.py
  ```

