import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutoresPage } from './pages/authors/authors.component';

export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'autores', component: AutoresPage}
];
