import React from 'react';
import Nav from '../components/nav';

const Dashboard = ({history, students}) => {
  return(
    <div>
    <Nav />
    <div className="dashboard-page">
      <div className="dashboard-item">
        <div>
          <i aria-hidden="true" className="green users icon " style={{fontSize: "75px"}}></i>
          <div className="dashboard-text">
            <div>Total Users</div>
            <div style={{marginTop: "15px"}}>{students.length}</div>
          </div>
        </div>
      </div>
      <div className="dashboard-item" onClick={()=> history.push('/search')}>
        <div>
          <i aria-hidden="true" className="green search icon" style={{fontSize: "75px"}}></i>
          <div className="dashboard-text">
            <div>Search</div>
          </div>
        </div>
      </div>
    </div>
    </div>
  )
}
export default Dashboard;