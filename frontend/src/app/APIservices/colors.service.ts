import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Color } from '../models/color.model';

@Injectable({
  providedIn: 'root'
})
export class ColorService {
  private apiBaseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) {}

  getAllColors(): Observable<Color[]> {
    return this.http.get<Color[]>(`${this.apiBaseUrl}/tags`);
  }
}
