import React from 'react';

const StudentList = ({student, history}) => {
  return(
    <div className="student-item" onClick={() => { history.push(`/student?id=${student.id}`) }}>
      <div className="student-list-item">{student.id}</div>
      <div className="student-list-item">{student.name|| ''}</div>
      <div className="student-list-item">{student.school_id || ''}</div>
    </div>
  )
}
export default StudentList;