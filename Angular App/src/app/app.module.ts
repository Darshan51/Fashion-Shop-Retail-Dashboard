import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from '@angular/common/http'
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { AuthenticateComponent } from './authenticate/authenticate.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { Routes } from '@angular/router';
import { RouterModule } from '@angular/router';
import { DirectAccessGuard } from './DirectAccess';

const routes : Routes = [
  {path : '', component : AuthenticateComponent},
  {path : 'dashboard', component : DashboardComponent},
  // {path : 'dashboard', component : DashboardComponent, canActivate:[DirectAccessGuard]},  
]


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    AuthenticateComponent,
    DashboardComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule ,
    FormsModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
