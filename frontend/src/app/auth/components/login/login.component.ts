import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '@/auth/services/auth.service';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;

  constructor(private api: AuthService, private router: Router) {}

  ngOnInit(): void {
    this.loginForm = new FormGroup({
      username: new FormControl(''),
      password: new FormControl(''),
    });
  }
  login = (Username: string, Password: string) => {
    this.api.loginUser(Username, Password).subscribe({
      next: (data) => {
        console.log('data: ', data);
        this.router.navigate(['/home']);
      },
      error: (e) => {
        console.log('errors: ', e);
      },
    });
  };

  loginUser(): void {
    this.login(this.loginForm.value.username, this.loginForm.value.password);
  }
}
