import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private baseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) { }

  getCartItems(): Observable<any> {
    const url = `${this.baseUrl}/get-cart-items/`; // Ensure this endpoint is configured in Django
    return this.http.get(url, {
      headers: { Authorization:
        'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MTk5NTM3LCJpYXQiOjE3MTQwMTU1MzcsImp0aSI6ImQxNGQ1NTkzNTU4NDQ0NTNhZjk3ZmNiOTg5YmQ5NDNlIiwidXNlcl9pZCI6MX0.61YOQjJRhY7VwxY0eeS4Jw-El6SpC-RsQXlOSc0I0rM' }
    });
  }

  addToCart(tourId: number, quantity: number = 1): Observable<any> {
    const url = `${this.baseUrl}/add-to-cart/`;
    const data = { tour_id: tourId, quantity: quantity };
    return this.http.post(url, data, {
      headers: { Authorization:
        'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MTk5NTM3LCJpYXQiOjE3MTQwMTU1MzcsImp0aSI6ImQxNGQ1NTkzNTU4NDQ0NTNhZjk3ZmNiOTg5YmQ5NDNlIiwidXNlcl9pZCI6MX0.61YOQjJRhY7VwxY0eeS4Jw-El6SpC-RsQXlOSc0I0rM' }
    });
  }

  clearCart(): Observable<any> {
    const url = `${this.baseUrl}/clear-cart/`;
    return this.http.post(url, {}, {
      headers: { Authorization:
        'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MTk5NTM3LCJpYXQiOjE3MTQwMTU1MzcsImp0aSI6ImQxNGQ1NTkzNTU4NDQ0NTNhZjk3ZmNiOTg5YmQ5NDNlIiwidXNlcl9pZCI6MX0.61YOQjJRhY7VwxY0eeS4Jw-El6SpC-RsQXlOSc0I0rM' }
    });
  }
}
