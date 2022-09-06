import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import {map} from 'rxjs/operators'
import { Router } from '@angular/router';

@Component({
  selector: 'app-authenticate',
  templateUrl: './authenticate.component.html',
  styleUrls: ['./authenticate.component.css']
})
export class AuthenticateComponent implements OnInit {
   
  pageDisplayed :string = 'login'

  @ViewChild('loginForm') loginForm : NgForm

  @ViewChild('registerForm') registerForm : NgForm

  regSuccess : boolean = false;
  loggedIn : boolean = false;
  RegistrationResponse : string = '';

  constructor(private http : HttpClient, private router : Router) { }

  ngOnInit(): void {

  }
  
  OnToggle(page:string){
    if(page === 'register') this.pageDisplayed = page;
    else this.pageDisplayed = 'login'
  }
  
  Onlogin(){
     this.http.post<{access_token:string}>('http://127.0.0.1:5000/auth', this.loginForm.value).subscribe(resp=>{
      if(resp !==null) {
        window.localStorage.setItem("Token",resp.access_token)
        this.loggedIn = true
        this.router.navigate(['dashboard'])
      } 
      
    })
  } 

  OnRegister(){
    
    this.http.post('http://127.0.0.1:5000/register_user',this.registerForm.value)
    .pipe(map(respData =>{
        return Object.values(respData)[0];
      
      }))
    .subscribe(resp =>{
         this.RegistrationResponse = resp  ;
    })

    this.registerForm.reset()
    this.regSuccess = true;
  }

}
