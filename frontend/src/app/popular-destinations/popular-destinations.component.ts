import { Component, OnInit } from '@angular/core';
import { forkJoin } from 'rxjs';
import { City } from '../models/city.model';
import { CityService } from '../APIservices/city.service';
import { ColorService } from '../APIservices/colors.service';
import { CommonModule, NgFor } from '@angular/common';
import { ToursComponent } from '../tours/tours.component';
import { Color} from '../models/color.model';
@Component({
  selector: 'app-popular-destinations',
  standalone: true,
  imports: [CommonModule, NgFor, ToursComponent],
  templateUrl: './popular-destinations.component.html',
  styleUrls: ['./popular-destinations.component.css'] // 'styleUrls' should be used instead of 'styleUrl'
})
export class PopularDestinationsComponent implements OnInit {
  cities: City[] = [];
  colors: Color[] = [];
  activeCity: City | null = null;

  constructor(
    private cityService: CityService,
    private colorService: ColorService
  ) {}

  ngOnInit(): void {
    forkJoin({
      cities: this.cityService.getAllCities(),
      colors: this.colorService.getAllColors()
    }).subscribe(results => {
      this.cities = results.cities;
      this.colors = results.colors; // Assuming colors is used somewhere in your component

      if (this.cities.length > 0) {
        this.setActiveCity(this.cities[0]);
      }
    });
  }

  setActiveCity(selectedCity: City): void {
    this.activeCity = selectedCity;
    // Implement logic to mark the city as active if needed
    // For example, if you have isActive flag on your City model
    this.cities.forEach(city => city.isActive = false);
    selectedCity.isActive = true;
  }
}
