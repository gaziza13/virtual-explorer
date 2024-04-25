import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { City } from '../models/city.model';
import { Tour } from '../models/tour.model';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private apiBaseUrl = 'http://127.0.0.1:8000/api/cart';

  constructor(private http: HttpClient) {}

  items: Tour[] = [];

  getAllfromCart(): Observable<City[]> {
    return this.http.get<[]>(`${this.apiBaseUrl}/cart/`);
  }

  clearCart(): Observable<City[]> {
    return this.http.delete<City[]>(`${this.apiBaseUrl}/cart/`);
  }
}
