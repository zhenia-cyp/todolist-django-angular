import { Injectable } from '@angular/core';
import {environment} from '../../environments/environment';
import {HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  baseurl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  regUser(Email: string, Username: string, Password: string): Observable<any> {
    const body = {email: Email, username: Username, password: Password};
    return this.http.post(this.baseurl + '/api/v1/auth/users/', body);
  }
}
