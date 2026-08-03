import { Injectable } from '@angular/core';
import { Iemployee } from '../../../models/iemployee';

@Injectable({
  providedIn: 'root',
})
export class EmployeeService {

  private employees: Iemployee[] = [
    {id:1,
    name:"Maimo Hasegawa",
    jobtitle:"Sales Associate",
    department:"Finance",
    email:"maimo.hasegawa@example.com",
    phone:"555-1234",
    joindate:new Date("1990-05-15"),
    imgUrl:"https://picsum.photos/100"},

    {id:2,
    name:"Fuze Kramer",
    jobtitle:"Marketing Manager",
    department:"Marketing",
    email:"fuze.kramer@example.com",
    phone:"555-5678",
    joindate:new Date("1992-08-20"),
    imgUrl:"https://picsum.photos/100"}, 

    {id:3,
    name:"Jose L. Meina",
    jobtitle:"Project Manager",
    department:"Operations",
    email:"jose.meina@example.com",
    phone:"555-9012",
    joindate:new Date("1991-12-10"),
    imgUrl:"https://picsum.photos/100"},

    {id:4,
    name:"Kornelia Maciejewska",
    jobtitle:"Data Analyst",
    department:"Analytics",
    email:"kornelia.maciejewska@example.com",
    phone:"555-3456",
    joindate:new Date("1993-04-25"),
    imgUrl:"https://picsum.photos/100"}, 

    {id:5,
    name:"Ebelegbulam Amechi",
    jobtitle:"Financial Analyst",
    department:"Finance",
    email:"ebelegbulam.amechi@example.com",
    phone:"555-7890",
    joindate:new Date("1994-07-15"),
    imgUrl:"https://picsum.photos/100"}, 

    {id:6,
    name:"Kauan Castro",
    jobtitle:"Graphic Designer",
    department:"Design",
    email:"kauan.castro@example.com",
    phone:"555-9283",
    joindate:new Date("1994-07-15"),
    imgUrl:"https://picsum.photos/100"},

    {id:7,
    name:"Jamal Glacer",
    jobtitle:"Project Manager",
    department:"Operations",
    email:"jamal.glacer@example.com",
    phone:"293-2212",
    joindate:new Date("2004-07-15"),
    imgUrl:"https://picsum.photos/100"},

    {id:8,
    name:"Rania Alzaman",
    jobtitle:"Data Analyst",
    department:"Analytics",
    email:"rania.alzaman@example.com",
    phone:"555-1123",
    joindate:new Date("2000-07-15"),
    imgUrl:"https://picsum.photos/100"}
  ];

  constructor() {}

  getEmployees(): Iemployee[] {
    return this.employees;
  }

  getEmployeeById(id: number): Iemployee | undefined {
    return this.employees.find(emp => emp.id === id);
  }

}