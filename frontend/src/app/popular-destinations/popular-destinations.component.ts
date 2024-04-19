import { Component, OnInit } from '@angular/core';
import { City } from '../models/city.model';
import { CityService } from '../APIservices/city.service';

@Component({
  selector: 'app-popular-destinations',
  standalone: true,
  // imports: [],
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
