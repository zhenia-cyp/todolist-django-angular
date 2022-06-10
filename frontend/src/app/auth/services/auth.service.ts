import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor(private http: HttpClient) {}

  regUser(Email: string, Username: string, Password: string): Observable<any> {
    const url = environment.apiUrl;
    const body = { email: Email, username: Username, password: Password };
    console.log('regUser: ', body);
    return this.http.post(url + '/api/v1/auth/users/', body);
  }

  loginUser(Username: string, Password: string): Observable<any> {
    const url = environment.apiUrl;
    const body = { username: Username, password: Password };
    console.log('loginUser: ', body);
    return this.http.post(url + '/api/v1/auth-token/token/login/', body);
  }
}
