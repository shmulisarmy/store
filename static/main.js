let store_items = {
    1: { id: 1, name: 'Apple Watch', price: 10, quantity: 10, imageUrl: 'https://picsum.photos/200/300?random=1' },
    2: { id: 2, name: 'MacBook Pro', price: 20, quantity: 20, imageUrl: 'https://picsum.photos/200/300?random=2' },
    3: { id: 3, name: 'iPhone 13', price: 30, quantity: 30, imageUrl: 'https://picsum.photos/200/300?random=3' },
    4: { id: 4, name: 'AirPods Pro', price: 40, quantity: 40, imageUrl: 'https://picsum.photos/200/300?random=4' },
    5: { id: 5, name: 'iPad Pro', price: 50, quantity: 50, imageUrl: 'https://picsum.photos/200/300?random=5' },
    6: { id: 6, name: 'Apple TV 4K', price: 60, quantity: 60, imageUrl: 'https://picsum.photos/200/300?random=6' },
    7: { id: 7, name: 'Beats Solo Pro', price: 70, quantity: 70, imageUrl: 'https://picsum.photos/200/300?random=7' },
    8: { id: 8, name: 'Apple Pencil', price: 80, quantity: 80, imageUrl: 'https://picsum.photos/200/300?random=8' },
    9: { id: 9, name: 'Smart Keyboard', price: 90, quantity: 90, imageUrl: 'https://picsum.photos/200/300?random=9' },
    10: { id: 10, name: 'AirTag', price: 100, quantity: 100, imageUrl: 'https://picsum.photos/200/300?random=10' },
};

const cart = {
    1: 1,
    2: 1,
    3: 1
};


const shared = {
    total_price: 0
}


document.addEventListener('alpine:init', () => {
Alpine.data("storeAndCart", () => ({
    shared: shared,
store_items: store_items,
cart: cart,
addToCart(id) {
    console.log("addToCart", id);
    this.cart[id] = this.cart[id] ? this.cart[id] + 1 : 1
    this.shared.total_price += store_items[id].price
    console.log(this.cart);
    console.log(this.shared.total_price);
},


    deleteFromCart(id) {
        delete this.cart[id]
        this.shared.total_price -= store_items[id].price
        console.log(this.shared.total_price);
    },
    
}));

Alpine.data("singleItem", () => ({
    showingSingleItem: null,
    init() {
        // Watch the 'shared.total_price' property
        this.$watch(() => this.showingSingleItem, () => {
            alert(this.showingSingleItem.name);
        });
    },



}));
})