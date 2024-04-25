import { Component } from '@angular/core';
import { AppComponent } from '../app.component';
import { NavbarComponent } from '../navbar/navbar.component';

@Component({
  selector: 'app-aboutus',
  standalone: true,
  imports: [NavbarComponent],
  templateUrl: './aboutus.component.html',
  styleUrl: './aboutus.component.css'
})
export class AboutusComponent {

}
