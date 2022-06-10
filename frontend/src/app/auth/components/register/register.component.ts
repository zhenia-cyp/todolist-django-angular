import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { AuthService } from '@/auth/services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
})
export class RegisterComponent implements OnInit {
  registerForm!: FormGroup;
  result: any;

  constructor(private api: AuthService, private router: Router) {}

  ngOnInit(): void {
    this.registerForm = new FormGroup({
      email: new FormControl(''),
      username: new FormControl(''),
      password: new FormControl(''),
    });
  }

  regUser = (Email: string, Username: string, Password: string) => {
    this.api.regUser(Email, Username, Password).subscribe({
      next: (data) => {
        this.result = data;
        this.router.navigate(['/auth/login']);
      },
      error: (e) => {
        console.log('errors: ', e);
      },
    });
  };
  registerUser(): void {
    this.regUser(
      this.registerForm.value.email,
      this.registerForm.value.username,
      this.registerForm.value.password
    );
  }
}
