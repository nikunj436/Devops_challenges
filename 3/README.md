requirement: 
        - python, Docker, Docker compose


- To run:
- with Docker compose(use any command from  below)
        - docker compose -f docker-compose.yaml up
        - docker compose -f docker-compose.yaml up -d
        - docker compose up 
        - docker compose up -d


- used in to initialization add key words
female-name.txt
# Names of women from lots of languages
#
# From Bob Baldwin's collection from MIT
# Augmented by Matt Bishop and Daniel Klein
#


- Query of any word will give max 10 suggestion which are words in Dictonary(redis cache). if there is no match then empty list will return 