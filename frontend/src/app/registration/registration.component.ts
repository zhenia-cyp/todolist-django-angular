import { Component, OnInit } from '@angular/core';
import {UserService} from '../services/user.service';
import {Router} from "@angular/router";

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  constructor(public api: UserService, private router: Router) { }

  ngOnInit(): void {
  }

  regUser = (Email: string, Username: string, Password: string) => {
    this.api.regUser(Email, Username, Password).subscribe({
      next: data => {
          console.log('DATA: ',data);
          this.router.navigate(['/home']);
      },
      error: e => {
          // ...         
      }
  });
  }

}
