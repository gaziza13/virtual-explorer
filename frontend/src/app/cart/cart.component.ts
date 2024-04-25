import { Component } from '@angular/core';
import { CartService } from '../APIservices/cart.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrl: './cart.component.css'
})
export class CartComponent {
  items = this.cartService.getAllfromCart();

  constructor (private cartService: CartService) {}

  clearCart(){
    this.items = this.cartService.clearCart();
  }
}
