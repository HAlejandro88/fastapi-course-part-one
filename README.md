
## Docker

```bash
docker run --name some-fast --network faastapi -v /Users/alejandrosoto/Desktop/python/FastApiPostgres:/usr/src/app -p 5003:80  restapifast
```

## Alembic
alembic is a pckage for creaate migrations

```bash
alembic init migration
```
### create mifration file
```bash
alembic revision --autogenerate -m "message"  
```

### trow the migration
```bash
alembic upgrade head    
```

## Run the application in develop
```bash
uvicorn main:app --reload 
```
