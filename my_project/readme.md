### tests
```
curl -X POST http://127.0.0.1:8000/register/ ^
-H "Content-Type: application/json" ^
-d "{\"username\": \"testuser\", \"email\": \"testuser@example.com\", \"password\": \"password123\"}"
```

```
curl -X POST http://127.0.0.1:8000/login/ ^
-H "Content-Type: application/json" ^
-d "{\"username\": \"testuser\", \"password\": \"password123\"}"
```
```
curl -X GET http://127.0.0.1:8000/items/ ^
-H "Authorization: Token 6e3c1254b401275747ec7f22ef1ff5d2b2b33f70"

```
```
curl -X POST http://127.0.0.1:8000/items/ ^
-H "Authorization: Token 6e3c1254b401275747ec7f22ef1ff5d2b2b33f70" ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"New Item\", \"description\": \"Item Description\"}"
```
```
curl -X POST http://127.0.0.1:8000/convert-image/ ^
-H "Authorization: Token 7ddd9106f1e8b23f64fe50cef16d0ebc29497cd4" ^
-H "Content-Type: application/json" ^
-d "{\"input_image_path\": \"C:/path/to/input/image.jpg\", \"output_image_path\": \"C:/path/to/output/grayscale_image.jpg\"}"
```

### Pytest
```python
pytest items/tests/pytest/
```