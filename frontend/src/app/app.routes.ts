import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PopularDestinationsComponent } from './popular-destinations/popular-destinations.component';
import { AboutusComponent } from './aboutus/aboutus.component';
import { CartComponent } from './cart/cart.component';

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent},
  { path: 'about', component:  AboutusComponent},
  { path: 'cart', component:  CartComponent}
  // { path: 'popular-destinations', component: PopularDestinationsComponent }
];

