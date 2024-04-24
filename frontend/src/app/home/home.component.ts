import { CommonModule, NgFor } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { CityService } from '../APIservices/city.service';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { PopularDestinationsComponent } from '../popular-destinations/popular-destinations.component';
import { City } from '../models/city.model';


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterModule, NgFor, PopularDestinationsComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent  {
  
}
