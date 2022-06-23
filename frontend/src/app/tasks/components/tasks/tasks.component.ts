import { TasksService } from '@/tasks/services/tasks.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',

  styleUrls: ['./tasks.component.css'],
})
export class TasksComponent implements OnInit {
  taskListToken: any = [];
  token: any;
  constructor(private api: TasksService) {}

  ngOnInit(): void {
    this.token = localStorage.getItem('token');
    this.getTaskByToken(this.token);
  }

  getTaskByToken = (Token: string) => {
    this.api.getTaskByToken(Token).subscribe({
      next: (data) => {
        this.taskListToken = data;
        console.log('token list: ', this.taskListToken);
      },
      error: (e) => {
        console.log('errors: ', e);
      },
    });
  };
}
