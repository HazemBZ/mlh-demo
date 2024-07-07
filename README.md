
## Architecture

<p align="start">
    <img src="images/project-architecture.png" width='600'>
<p>


## Components

**Tasks Manager**: Orchestrates running Scenarios using a task queue;
 Arranges the run order of scenarios (in sequence, in parallel), 
 and handles  pre/post scenario runs (resources cleanup; notifying Web client with progress, etc)

**Task queue**: Runs jobs sent by the Tasks Manager

**Scenario**: A unit that handles every steps required to achieve the intended objective:
 - extracting data using scraping/received request
 - starting/stopping an agent that interact with a web app

**Agent**: A frontend client to interact with apps
  that dynamically generate their content (Single page apps, etc)

**Templates**: Data formats (form inputs, selection menu dictionaries, etc),
reverse engineered to correctly parse and transfer data to the targeted website 

## Setup

**Run containers**
```
docker-compose up 
```

## Testing

If you're really interested in a poc run, then you can test the system with
one of the automated interactions.

1.install httpie

2.Send a pre-populated post request

```
http localhost:8004/announce < request.json
```

3.Access "https://www.menzili.tn/connexion" using the "tilzxivqvzjmubrgsh@cazlp.com" as email and "tilzxivqvzjmubrgsh" password

4.You can use  run `docker-compose logs web` to get more logged info and access info about created tasks @`localhost:5555` for flower dashboard

