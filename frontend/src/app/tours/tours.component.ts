import { Component, OnInit } from '@angular/core';
import { Tour } from '../models/tour.model';
import { CommonModule, NgFor } from '@angular/common';
import { RouterModule } from '@angular/router';
import { TourService } from '../APIservices/tour.service';

@Component({
  selector: 'app-tours',
  standalone: true,
  imports: [CommonModule, RouterModule, NgFor],
  templateUrl: './tours.component.html',
  styleUrl: './tours.component.css'
})
export class ToursComponent implements OnInit{
  tours: Tour[] = [];
  filteredTours: Tour[] = [];
  selectedCity: string = ''; 

  constructor(private tourService: TourService) {}

  ngOnInit(): void {
    this.fetchTours(); 
  }

  fetchTours(): void {
    this.tourService.getAllTours().subscribe({
      next: (data: Tour[]) => {
        this.tours = data;
        this.filterTours(); 
      },
      error: (error: any) => {
        console.error('Error fetching tours:', error);
      }
    });
  }
  

  filterTours(): void {
    if (this.selectedCity) {
      this.filteredTours = this.tours.filter(tour => tour.city === this.selectedCity);
    } else {
      this.filteredTours = this.tours;
    }
  }

  onSelectCity(city: string): void {
    this.selectedCity = city;
    this.filterTours();
  }
}
