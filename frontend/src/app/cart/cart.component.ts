import { Component, OnInit } from '@angular/core';
import { CartService } from '../APIservices/cart.service';
import { CommonModule } from '@angular/common';
import { Tour } from '../models/tour.model';

@Component({
  selector: 'app-cart',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './cart.component.html',
  styleUrl: './cart.component.css'
})
export class CartComponent {
  Tour: Tour[] = [];
  // colors: Color[] = [];

  constructor(private cartService: CartService) {}

  ngOnInit() {
    this.getCartItems();
  }

  getCartItems() {
    this.cartService.getCartItems().subscribe({
      next: (data) => this.Tour = data,
      error: (error) => console.error('Error fetching cart items:', error)
    });
  }

  clearCart() {
    this.cartService.clearCart().subscribe({
      next: () => {
        console.log('Cart cleared successfully');
        this.Tour = []; // Clears the items on the UI as well
      },
      error: (error) => console.error('Error clearing cart:', error)
    });
  }
}
