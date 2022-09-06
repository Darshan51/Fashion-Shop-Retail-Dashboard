import { Component, OnInit, ViewChild } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { SaleElement } from './sale-element';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  totalSale : any = 5000;
  totalProfit : any = '2000';
  uniqueVisitors:number = 500;
  saleList : SaleElement[] 
  base:string = 'http://127.0.0.1:5000/'
  
  headers = new HttpHeaders().set('Authorization', `JWT ${window.localStorage.getItem("Token")}`)


  constructor(private http : HttpClient) { }

  ngOnInit(): void {
    this.getTotalSale();
    this.getTotalProfit();
    this.getUniqueVisitors();
    this.getSaleDetail();
     
    console.log({'headers':this.headers})
    
  }
  
  getTotalSale(){
    
  
    this.http.get<{total_sale:number}>(this.base+'total_sale',{'headers':this.headers})
   .subscribe(resp=>{
       this.totalSale = resp.total_sale;
    })
    
  }

  getTotalProfit(){
    this.http.get<{'total_profit' : number}>(this.base+'total_profit',{'headers':this.headers})
    .subscribe(resp=>{
      this.totalProfit = resp.total_profit;
    })
  }
  
  getUniqueVisitors(){
    this.http.get<{total_visitors:number}>(this.base+'total_visitors',{'headers':this.headers})
  .subscribe(resp=>{
       this.uniqueVisitors = resp.total_visitors;
    })
  }
  
  getSaleDetail(){
    this.http.get<{sale_details:SaleElement[]}>(this.base+'sale_details',{'headers':this.headers})
   .subscribe(resp=>{
    this.saleList = resp.sale_details;  
   })
  }

}
