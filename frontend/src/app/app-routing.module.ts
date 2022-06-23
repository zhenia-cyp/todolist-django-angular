import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/components/home/home.component';
import { CurrentTaskComponent } from './tasks/components/current-task/current-task.component';

const routes: Routes = [
  {
    path: 'auth',
    loadChildren: () => import('@/auth/auth.module').then((m) => m.AuthModule),
  },
  { path: 'home', component: HomeComponent },
  { path: 'current/task/:id', component: CurrentTaskComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
