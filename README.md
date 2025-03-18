## Meeting Posts

### Instructions
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

To shut down service:
```bash
deactivate
```

### How to call endpoints
Get all the posts: 
```bash
GET localhost:3000/all
```

Get all posts from specific user:
```bash
GET localhost:3000/<userId>
```

Upload post:
```bash
POST localhost:3000/upload
```

Sample Body Json:
```bash
{
    "userId": "123",
    "name": "Phoebe",
    "restaurant: "Coffeebean",
    "image_url": "xxx"
}
```

