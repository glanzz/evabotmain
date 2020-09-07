import React from 'react';
import { useEffect, useState } from 'react';
import Nav from '../components/nav';

const Student = ({history}) => {
  const [studentData, setStudentData] = useState({});
  const [reasonsData, setReasonsData] = useState([]);
  async function fetchData(id) {
    let studentResp = await fetch(`/students?id=${id}`)
    console.log(studentResp)
    studentResp.json().then(response=>{
      if (studentResp.status == 200) {
        const student = response;
        console.log(student)
        setStudentData(student);
      }
      else {
        alert(JSON.stringify(response));
      }
    })
    let reasonResp = await fetch(`/reasons?id=${id}`)
    reasonResp.json().then(response=>{
      if (reasonResp.status == 200) {
        const reasons = response.reasons;
        setReasonsData(reasons);
      }
      else {
        alert(JSON.stringify(response));
      }
    })
  }

  useEffect( ()=> {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    if (!id){
      history.push('/dashboard');
    }
    fetchData(id)
    }, []);

  
  return(
    <div>
      <Nav />
      <div class="ui card" style={{width: "80%", margin:"30px auto"}}>
        <div class="content">
          <div class="header"><i aria-hidden="true" class="user icon"></i> Student Details</div>
          </div>
          <div class="content">
            <div class="description">
              <ul>
                <li>
                  <div className="about-text">
                  <h4>Name</h4>:<span> </span> <span>{studentData.name}</span>
                  </div>
                </li>
                <li>
                  <div className="about-text">
                  <h4>School ID</h4>: <span> </span><span>{studentData.school_id || ''}</span>
                  </div>
                </li>
                <li>
                <div className="about-text">
                  <h4>Family Score</h4>: <span> </span><span>{studentData.family_score|| 0}</span>
                  </div>
                </li>
                <li>
                <div className="about-text">
                  <h4>Friends Score</h4>: <span> </span><span>{studentData.friends_score || 0}</span>
                  </div>
                </li>
                <li>
                <div className="about-text">
                  <h4>Teachers Score</h4>: <span> </span><span>{studentData.teachers_score || 0}</span>
                  </div>
                </li>
              </ul>
            </div>
          </div>
          <div class="extra content" >
            <h3 style={{color: "black"}}>Potential Questions</h3>
            <div>
              <div class="search-head">
                <div>Question</div>
                <div>Answer</div>
              </div>
            {
              reasonsData.map(reason => {
                return(
                  <div className="student-item">
                    <div className="qa-item">{reason.question || ''}</div>
                    <div className="qa-item">{reason.answer || ''}</div>
                  </div>
                )
              })
            }
          </div>
          </div>
        </div>
    </div>
  )
}
export default Student;