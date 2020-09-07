import React, {useEffect, useState} from 'react';
import {  BrowserRouter, Route, Switch } from 'react-router-dom';
import { createBrowserHistory } from "history";
import './App.css';
import Home from './pages/home';
import Dashboard from './pages/dashboard';
import Search from './pages/search';
import Student from './pages/student';
import 'semantic-ui-css/semantic.min.css';


function App() {
  const customHistory = createBrowserHistory();
  const [students, setStudents] = useState([]);
  useEffect(()=> {
    fetch('/students?all=True').then(
      res => {
          res.json().then(response=>{
          if (res.status == 200) {
            const students = response.students;
            setStudents(students);
          }
          else {
            alert(JSON.stringify(response));
          }
        })
      })
    }, students.length);
  return (
    <div>
      <BrowserRouter>
        <Switch>
            <Route path="/" history={customHistory}  component={Home} exact />
            <Route path="/dashboard" history={customHistory}   render={(props) => <Dashboard students={students} {...props}/>}  />
            <Route path="/search" history={customHistory} render={(props) => <Search students={students} {...props} /> }  />
            <Route path="/student" history={customHistory} render={(props) => <Student  {...props} /> }  />
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
