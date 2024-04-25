import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { PopularDestinationsComponent } from './popular-destinations/popular-destinations.component';
import { CityService } from './APIservices/city.service';
import { ToursComponent } from './tours/tours.component';
import { AboutusComponent } from './aboutus/aboutus.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    PopularDestinationsComponent,
    ToursComponent,
    AboutusComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [
    CityService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
