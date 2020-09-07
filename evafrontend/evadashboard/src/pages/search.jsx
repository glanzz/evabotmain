import React, {} from 'react';
import Nav from '../components/nav';
import { useEffect , useState} from 'react';
import StudentList from '../components/student-list';

const Search = ({history, students}) => {
  const [filterValue, setFilterValue] = useState('');
  const [filterData, setFilterData] = useState([]);

  useEffect(()=> {
    setFilterData(students);
  },[students.length]);
  useEffect(()=> {
    handleFilter()
  }, [filterValue])
  const handleFilter= () => {
    let filteredData = students;
    if (filterValue){
      filteredData = students.filter(
        student =>
          student.school_id &&
          student.school_id.toLowerCase().includes(filterValue.toLowerCase()),
      );
    }
    setFilterData(filteredData)
  }
  
  return(
    <div>
      <Nav />
      <div className="search-page">
        <div className="search-box">
          <div class="ui action input">
            <input type="text" value={filterValue} placeholder="Enter College ID" onChange={(e)=> setFilterValue(e.target.value)}/>
            <button class="ui button" onClick={handleFilter}>Search</button>
          </div>
        </div>
        <div class="search-list">
          <div class="search-head">
            <div>ID</div>
            <div>Name</div>
            <div>School ID</div>
          </div>
          {
            filterData.map(data => {
              return <StudentList key={data.id} student={data} history={history}/>
            })
          }
        </div>
      </div>
    
    </div>
  )
}
export default Search;