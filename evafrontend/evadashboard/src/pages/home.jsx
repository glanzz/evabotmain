import React, {useState} from 'react';

const Home = ({history}) => {
  const [password, setPassword] = useState('');
  function handleLogin() {
    if (password === "evapassword"){
      history.push('/dashboard')
    }
  }
  return(
    <div className="home-page">
      <div>
      <div className="ui teal header home-header ">DASHBOARD LOGIN</div>
      <div class="ui action input">
        <input type="password" placeholder="Enter Password" value={password} onChange={(e)=>setPassword(e.target.value)}/>
        <button class="ui button" onClick={handleLogin}>Submit</button>
      </div>
      </div>
    </div>
  )
}
export default Home;