import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Footer } from "./components/footer/footer";
import { Header } from './components/header/header';
import { Employees } from './components/employees/employees';

@Component({
  selector: 'app-root',
  imports: [Header, Footer, Employees],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('corporate-resource-manager');
}
