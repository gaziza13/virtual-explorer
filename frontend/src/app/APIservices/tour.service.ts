import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { City } from '../models/city.model';
import { Tour } from '../models/tour.model';

@Injectable({
  providedIn: 'root'
})
export class TourService {
  private apiBaseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) {}

  getAllTours(): Observable<Tour[]> {
    return this.http.get<Tour[]>(`${this.apiBaseUrl}/tours/`);
  }

  addTour(): Observable<Tour[]> {
    return this.http.get<Tour[]>(`${this.apiBaseUrl}/tours/`);
  }

}
