import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class TasksService {
  baseurl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getTaskByToken(Token: string) {
    return this.http.get(this.baseurl + '/api/v1/tasks/list/task/user/', {
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Token ' + Token,
      },
    });
  }
}
