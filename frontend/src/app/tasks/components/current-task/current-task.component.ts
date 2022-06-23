import { TasksService } from '@/tasks/services/tasks.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-current-task',
  templateUrl: './current-task.component.html',
  styleUrls: ['./current-task.component.css'],
})
export class CurrentTaskComponent implements OnInit {
  currentTask!: any;
  constructor(private api: TasksService, private router: ActivatedRoute) {}

  ngOnInit(): void {
    this.getIteamTask(this.router.snapshot.params['id']);
  }

  getIteamTask(Id: string) {
    this.api.getIteamTask(Id).subscribe({
      next: (data) => {
        this.currentTask = data;
      },
      error: (e) => {
        console.log('errors: ', e);
      },
    });
  }
}
