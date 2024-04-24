import { Component, OnInit } from '@angular/core';
import { City } from '../models/city.model';
import { CityService } from '../APIservices/city.service';
import { CommonModule, NgFor } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ToursComponent } from '../tours/tours.component';

@Component({
  selector: 'app-popular-destinations',
  standalone: true,
  imports: [CommonModule, RouterModule, NgFor, ToursComponent],
  templateUrl: './popular-destinations.component.html',
  styleUrl: './popular-destinations.component.css'
})
export class PopularDestinationsComponent implements OnInit {
  cities: City[] = [];

  constructor(private cityService: CityService) {}

  ngOnInit(): void {
    this.cityService.getAllCities().subscribe(
      (data: City[]) => {
        this.cities = data;
      },
    );
  }
}
