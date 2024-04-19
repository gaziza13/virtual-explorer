import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PopularDestinationsComponent } from './popular-destinations/popular-destinations.component';

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent},
  { path: 'popular-destinations', component: PopularDestinationsComponent }
];

