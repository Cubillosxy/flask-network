# flask-network
blog posting

---

<p align="center">
  <a href="https://opensource.org/licenses/MIT" alt="License: MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square"/>
  </a>
</p>

---


## Get started

 - clone repo : `git clone https://github.com/Cubillosxy/flask-network.git`
 - install docker: [Docker](https://www.docker.com/get-started)
 `docker-compose build .`
 `docker-compose up`
 
 - visit `http://localhost:5000/ `
 
 ----


## Database

dump:

    docker exec flask-network_db_1 bash -c 'pg_dump --dbname=postgres --username=postgres > /tmp/data/db.dump'

restore:

    docker exec flask-network_db_1 bash -c 'psql --dbname=postgres --username=postgres --command="DROP SCHEMA public CASCADE;CREATE SCHEMA public;" && pg_restore /tmp/data/db.dump --dbname=postgres --username=postgres --no-owner'
    
    # restore with psql
    docker exec -it flask-network_db_1 bash -c 'psql postgres --username=postgres < /tmp/data/db.dump'

Connect to the database shell using:

    docker exec -it flask-network_db_1 psql --dbname=postgres --username=postgres

<p align="center">This project is licensed under the  <a href='https://opensource.org/licenses/MIT' target="_blank">MIT License</a>.</br>
Copyright &copy; 2016 Edwin Cubillos</p>