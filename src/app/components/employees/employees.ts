import { Component } from '@angular/core';
import { Iemployee } from '../../models/iemployee';
import { DatePipe } from '@angular/common';
import { EmployeeService } from './services/employee';

@Component({
  selector: 'app-employees',
  imports: [DatePipe],
  templateUrl: './employees.html',
  styleUrl: './employees.css',
})
export class Employees {
  employees:Iemployee[]
  selectedEmployee: Iemployee | null = null;

  constructor(private employeeService: EmployeeService) {
    this.employees = this.employeeService.getEmployees();
  }

  openEmployee(emp: Iemployee): void {
    this.selectedEmployee = emp;
  }

  closeEmployee():void {
    this.selectedEmployee = null;
  }
}

