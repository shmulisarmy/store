store_items: dict[int, dict] = {
    1: { "id": 1, "name": 'Apple Watch', "price": 10, "quantity": 10, "imageUrl": 'https://picsum.photos/200/300?random=1' },
    2: { "id": 2, "name": 'MacBook Pro', "price": 20, "quantity": 20, "imageUrl": 'https://picsum.photos/200/300?random=2' },
    3: { "id": 3, "name": 'iPhone 13', "price": 30, "quantity": 30, "imageUrl": 'https://picsum.photos/200/300?random=3' },
    4: { "id": 4, "name": 'AirPods Pro', "price": 40, "quantity": 40, "imageUrl": 'https://picsum.photos/200/300?random=4' },
    5: { "id": 5, "name": 'iPad Pro', "price": 50, "quantity": 50, "imageUrl": 'https://picsum.photos/200/300?random=5' },
    6: { "id": 6, "name": 'Apple TV 4K', "price": 60, "quantity": 60, "imageUrl": 'https://picsum.photos/200/300?random=6' },
    7: { "id": 7, "name": 'Beats Solo Pro', "price": 70, "quantity": 70, "imageUrl": 'https://picsum.photos/200/300?random=7' },
    8: { "id": 8, "name": 'Apple Pencil', "price": 80, "quantity": 80, "imageUrl": 'https://picsum.photos/200/300?random=8' },
    9: { "id": 9, "name": 'Smart Keyboard', "price": 90, "quantity": 90, "imageUrl": 'https://picsum.photos/200/300?random=9' },
    10: { "id": 10, "name": 'AirTag', "price": 100, "quantity": 100, "imageUrl": 'https://picsum.photos/200/300?random=10' },
    11: { "id": 11, "name": 'Magic Mouse', "price": 110, "quantity": 110, "imageUrl": 'https://picsum.photos/200/300?random=11' },
    12: { "id": 12, "name": 'Magic Trackpad', "price": 120, "quantity": 120, "imageUrl": 'https://picsum.photos/200/300?random=12' },
    13: { "id": 13, "name": 'Magic Keyboard', "price": 130, "quantity": 130, "imageUrl": 'https://picsum.photos/200/300?random=13' },
    14: { "id": 14, "name": 'HomePod mini', "price": 140, "quantity": 140, "imageUrl": 'https://picsum.photos/200/300?random=14' },
    15: { "id": 15, "name": 'Apple AirPods', "price": 150, "quantity": 150, "imageUrl": 'https://picsum.photos/200/300?random=15' },
    16: { "id": 16, "name": 'Apple AirPods Max', "price": 160, "quantity": 160, "imageUrl": 'https://picsum.photos/200/300?random=16' },
    17: { "id": 17, "name": 'Apple TV HD', "price": 170, "quantity": 170, "imageUrl": 'https://picsum.photos/200/300?random=17' },
    18: { "id": 18, "name": 'Apple TV 4K', "price": 180, "quantity": 180, "imageUrl": 'https://picsum.photos/200/300?random=18' },
    19: { "id": 19, "name": 'Apple Pencil 2', "price": 190, "quantity": 190, "imageUrl": 'https://picsum.photos/200/300?random=19' },
    20: { "id": 20, "name": 'Apple Watch SE', "price": 200, "quantity": 200, "imageUrl": 'https://picsum.photos/200/300?random=20' },
}


full_data = { i: { **item, "description": f"This is a {item['name']}. It is a great product." } for i, item in enumerate([{ "id": i, "name": f"Product {i+1}", "price": i*10+10, "quantity": i*10+10, "imageUrl": f"https://picsum.photos/200/300?random={i+1}" } for i in range(1, 101)]) },
    
