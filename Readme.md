Note: Before proceeding further create .env file in project root folder using file 'docs/example_env.txt' and set accordingly.

## For Local Development Setup

**System Requirements**
- Configure PEP8 in your editor/IDE
- Python 3.9+
- Mongo DB 4+

**Install Dependencies**
``` 
$ pip install --no-cache-dir -r requirements.txt
```

**To Run this Service Locally**
```
$ alembic upgrade cc31de0cbd9d
$ uvicorn src.main:app --reload
```

## Test this service locally
```
$ coverage run -m pytest
$ curl -i http://localhost:8000/
```

## Check API documentation (powered by OpenAPI with Swagger UI)
``` 
$ curl -i http://localhost:8000/docs
$ curl -i http://localhost:8000/redoc