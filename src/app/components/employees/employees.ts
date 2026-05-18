import { Component } from '@angular/core';
import { Iemployee } from '../../models/iemployee';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-employees',
  imports: [DatePipe],
  templateUrl: './employees.html',
  styleUrl: './employees.css',
})
export class Employees {
  employees:Iemployee[]

  constructor() {
    this.employees = [
      {id:1,
      name:"Maimo Hasegawa",
      jobtitle:"Sales Associate",
      email:"maimo.hasegawa@example.com",
      phone:"555-1234",
      joindate:new Date("1990-05-15"),
      imgUrl:"https://picsum.photos/100"},

      {id:2,
      name:"Fuze Kramer",
      jobtitle:"Marketing Manager",
      email:"fuze.kramer@example.com",
      phone:"555-5678",
      joindate:new Date("1992-08-20"),
      imgUrl:"https://picsum.photos/100"}, 

      {id:3,
      name:"Jose L. Meina",
      jobtitle:"Project Manager",
      email:"jose.meina@example.com",
      phone:"555-9012",
      joindate:new Date("1991-12-10"),
      imgUrl:"https://picsum.photos/100"},

      {id:4,
      name:"Kornelia Maciejewska",
      jobtitle:"Data Analyst",
      email:"kornelia.maciejewska@example.com",
      phone:"555-3456",
      joindate:new Date("1993-04-25"),
      imgUrl:"https://picsum.photos/100"}, 

      {id:5,
      name:"Ebelegbulam Amechi",
      jobtitle:"Financial Analyst",
      email:"ebelegbulam.amechi@example.com",
      phone:"555-7890",
      joindate:new Date("1994-07-15"),
      imgUrl:"https://picsum.photos/100"}, 

      {id:6,
      name:"Kauan Castro",
      jobtitle:"Graphic Designer",
      email:"kauan.castro@example.com",
      phone:"555-9283",
      joindate:new Date("1994-07-15"),
      imgUrl:"https://picsum.photos/100"},

      {id:7,
      name:"Jamal Glacer",
      jobtitle:"Project Manager",
      email:"jamal.glacer@example.com",
      phone:"293-2212",
      joindate:new Date("2004-07-15"),
      imgUrl:"https://picsum.photos/100"},

      {id:8,
      name:"Rania Alzaman",
      jobtitle:"Data Analyst",
      email:"rania.alzaman@example.com",
      phone:"555-1123",
      joindate:new Date("2000-07-15"),
      imgUrl:"https://picsum.photos/100"}
    ];
  }
}
