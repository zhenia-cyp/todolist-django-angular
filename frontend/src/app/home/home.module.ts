import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './components/home/home.component';
import { HeaderComponent } from '@/header/header/header.component';
import { FooterComponent } from '@/footer/components/footer/footer.component';
import { TasksComponent } from '@/tasks/components/tasks/tasks.component';

@NgModule({
  declarations: [
    HomeComponent,
    HeaderComponent,
    FooterComponent,
    TasksComponent,
  ],
  imports: [CommonModule],
  exports: [HomeComponent, HeaderComponent, FooterComponent, TasksComponent],
})
export class HomeModule {}
